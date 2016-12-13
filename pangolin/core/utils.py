import re

from purl import URL

from django.utils.encoding import force_text


def intspace(value):
    """
    45570 => 45 570
    450840 => 450 840
    1450000 => 1 450 000
    """
    orig = force_text(value)
    new = re.sub(r'^(-?\d+)(\d{3})', '\g<1> \g<2>', orig)
    if orig == new:
        return new
    return intspace(new)


def set_param(request=None, url=None, **kwargs):
    if not request and not url:
        return '/'
    url = URL(path=request.path, query=request.META['QUERY_STRING']) if request else URL(url)
    for k, v in kwargs.items():
        url = url.query_param(k, v)
    return url.as_string()
