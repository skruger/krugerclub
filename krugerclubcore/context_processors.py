from django.contrib.sites import shortcuts
from wagtail.models import Site

def site_info(request):
    return {
        'site_info': Site.find_for_request(request)
    }
