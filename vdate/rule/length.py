"""VDate Length Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any
from sys import maxsize
from .base import Rule
from .error import TooShortError, TooLongError
from .._gettext import _


class LengthRule(Rule):
    """Length Rule
    """

    def __init__(self, min_length: int = 0, max_length: int = maxsize, value: Any = None):
        """Init
        """
        super().__init__(value)

        self._min_length = min_length
        self._max_length = max_length

    def validate(self):
        """Validate the rule
        """
        try:
            value_len = len(self._value)
        except TypeError:
            raise TypeError("This rule doesn't support values of type '{}'".format(type(self._value).__name__))

        if self._min_length is not None and value_len < self._min_length:
            raise TooShortError(_('Length cannot be less than {}').format(self._min_length), self._value)

        if self._max_length is not None and value_len > self._max_length:
            raise TooLongError(_('Length cannot be greater than {}').format(self._max_length), self._value)


class MinLengthRule(LengthRule):
    """Minimum Length Rule
    """

    def __init__(self, min_length: int, value: Any = None):
        """Init
        """
        super().__init__(min_length, value=value)


class MaxLengthRule(LengthRule):
    """Maximum Length Rule
    """

    def __init__(self, max_length: int, value: Any = None):
        """Init
        """
        super().__init__(max_length=max_length, value=value)
