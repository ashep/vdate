"""VDate gettext helper
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import os
import gettext

localedir = os.path.join(os.path.dirname(__file__), 'locale')
_ = gettext.translation('messages', localedir, fallback=True).gettext
