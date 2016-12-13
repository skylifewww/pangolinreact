from jinja2 import Environment

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext
from django.utils.timezone import now
from django.template.defaultfilters import timesince, timeuntil

from pangolin.core.utils import intspace, set_param


def environment(**options):
    env = Environment(**options)
    env.filters['timesince'] = timesince
    env.filters['timeuntil'] = timeuntil
    env.globals.update({
        'dir': dir, 'list': list, 'len': len, 'enumerate': enumerate, 'range': range,
        'settings': settings,
        'now': now, 'intspace': intspace, 'set_param': set_param,
        'static': staticfiles_storage.url, 'url': reverse, '_': ugettext, 'get_messages': get_messages,
    })
    return env
