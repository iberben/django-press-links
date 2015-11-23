from django.contrib import admin
from django.db import models
from press_links.models import Entry, Link

from parler.admin import TranslatableAdmin

from django_summernote.widgets import SummernoteWidget


class LinkAdmin(TranslatableAdmin):
    model = Link
    search_fields = ('link', 'link_text')
    list_display = ('entry', 'link', 'link_new_page')
    list_filter = ('link_new_page',)
admin.site.register(Link, LinkAdmin)


class EntryAdmin(TranslatableAdmin):
    model = Entry
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)
    list_display = ('title', 'pub_date', 'status',)
    list_filter = ('site', 'status',)
    # prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'excerpt',)
    # inlines = [LinkInline]
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

admin.site.register(Entry, EntryAdmin)
