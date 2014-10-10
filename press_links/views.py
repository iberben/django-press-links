import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from press_links.models import Entry
from press_links.enums import DRAFT_STATUS, HIDDEN_STATUS

from templatable_view import templatable_view


@templatable_view('press_links/entry_list.html')
def entries(request):
    """
    A list of the entries.
    """
    press_list = Paginator(Entry.objects.live(), 10)

    page = request.GET.get('page')
    try:
        items = press_list.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = press_list.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = press_list.page(paginator.num_pages)

    return {
        'object_list': items,
        'site_url': Site.objects.get_current().domain,
    }


@templatable_view('press_links/entry_detail.html')
def entry(request, slug):
    """
    The detail view of an entry.
    """
    # Get entry
    object = get_object_or_404(Entry, slug=slug, site=Site.objects.get_current())
    if object.status == DRAFT_STATUS and not request.user.is_staff or object.status == HIDDEN_STATUS:
        raise Http404

    # Context
    return {
        'object':object
    }

