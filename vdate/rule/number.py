"""VDate Number Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union, SupportsInt, SupportsFloat
from .error import IsNotNumberError, IsNotIntegerError, IsNotDecimalError
from .._gettext import _
from .base import Rule

NumberType = Union[SupportsInt, SupportsFloat]


class IsNumberRule(Rule):
    """Number validation rule
    """

    def validate(self):
        """Validate the rule
        """
        if not any([hasattr(self._value, m) for m in ('__int__', '__float__')]):
            raise IsNotNumberError(_('Is not a number'), self._value)


class IsIntegerRule(IsNumberRule):
    """Integer Validation Rule.
    """

    def validate(self):
        """Validate the rule
        """
        if not hasattr(self._value, '__int__'):
            raise IsNotIntegerError(_('Is not an integer number'))


class IsDecimalRule(IsNumberRule):
    """Float Validation Rule.
    """

    def validate(self):
        """Validate the rule
        """
        if not hasattr(self._value, '__float__'):
            raise IsNotDecimalError(_('Is not an float number'))
