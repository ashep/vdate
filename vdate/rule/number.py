"""Vdate Number Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union, SupportsInt, SupportsFloat
from decimal import Decimal
from .error import IsNotNumberError, IsNotIntegerError, IsNotFloatError
from .._gettext import _
from .base import Rule

NumberType = Union[SupportsInt, SupportsFloat]


class IsNumber(Rule):
    """Number validation rule
    """

    def validate(self):
        """Validate the rule
        """
        if not any([hasattr(self._value, m) for m in ('__int__', '__float__')]):
            raise IsNotNumberError(_('Is not a number'), self._value)


class IsInteger(IsNumber):
    """Integer validation rule
    """

    def validate(self):
        """Validate the rule
        """
        if not hasattr(self._value, '__int__'):
            raise IsNotIntegerError(_('Is not an integer number'))


class IsFloat(IsNumber):
    """Float validation rule
    """

    def validate(self):
        """Validate the rule
        """
        if not hasattr(self._value, '__float__'):
            raise IsNotFloatError(_('Is not a float number'))


class IsDecimal(IsNumber):
    """Decimal validation rule
    """

    def validate(self):
        """Validate the rule
        """
        if not isinstance(self._value, Decimal):
            raise IsNotFloatError(_('Is not a decimal number'))
