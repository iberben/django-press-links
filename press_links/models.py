from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from press_links.enums import STATUS_CHOICES, LIVE_STATUS, DRAFT_STATUS
from django.utils import timezone

from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableQuerySet


class EntryManager(models.Manager):
    def get_queryset(self):
        return EntryQuerySet(self.model)

    def live(self):
        """
        Returns a list of all published entries.

        :rtype: django.db.models.QuerySet
        """
        return self.filter(pub_date__lte=timezone.now(), status=LIVE_STATUS) \
            .filter(site=Site.objects.get_current())


class EntryQuerySet(TranslatableQuerySet):
    pass


class Entry(TranslatableModel):
    author = models.ForeignKey(User, verbose_name=_('author'),
                               related_name='%(app_label)s_%(class)s_related')
    slug = models.SlugField(max_length=255, unique_for_date='pub_date',
                            verbose_name='slug')
    pub_date = models.DateTimeField(default=timezone.now,
                                    verbose_name=_('publication date'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS,
                                 verbose_name=_('status'))
    site = models.ManyToManyField(Site,
                                  verbose_name=_('Sites where the entry is published'),
                                  related_name='%(app_label)s_%(class)s_related')

    objects = EntryManager()

    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_('title')),
        source=models.CharField(max_length=255, blank=True,
                                verbose_name=_('the source for the entry')),
        excerpt=models.TextField(blank=True, verbose_name=_(u'Excerpt'))
    )

    @models.permalink
    def get_absolute_url(self):
        return ('press_links_entry_detail', (), {'slug': self.slug})

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
        verbose_name = _('Press Entry')
        verbose_name_plural = _('Press Entries')

    def __unicode__(self):
        return self.title


class Link(TranslatableModel):
    link_new_page = models.BooleanField(default=False, verbose_name=_('open link in new page'))
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'))

    translations = TranslatedFields(
        link=models.CharField(max_length=255,
                              verbose_name=_('link address (add http:// for external link)')),
        link_text=models.CharField(max_length=255,
                                   verbose_name=_('text for link'))
    )

    class Meta:
        verbose_name = _('Press Link')
        verbose_name_plural = _('Press Links')
