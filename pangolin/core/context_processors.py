from django.conf import settings
from django.utils.timezone import now

from .utils import intspace, set_param


def extra(request):
    ctx = {
        'dir': dir, 'list': list, 'len': len, 'enumerate': enumerate, 'range': range,
        'settings': settings,
        'now': now, 'intspace': intspace, 'set_param': set_param}
    return ctx
