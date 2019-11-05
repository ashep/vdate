"""Vdate Base Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any
from abc import ABC, abstractmethod
from .._gettext import _
from .error import IsEmptyError, IsNotEmptyError

_EMPTY_OBJECTS = (None, '', [], {}, set(), tuple())


class Rule(ABC):
    """Base rule
    """

    def __init__(self, value: Any = None):
        """Init
        """
        self._value = value

    @property
    def value(self) -> Any:
        """Rule's value
        """
        return self._value

    @value.setter
    def value(self, value: Any):
        """Rule's value
        """
        self._value = value

    def get_value(self) -> Any:
        """Get rule's value
        """
        return self._value

    def set_value(self, value: Any):
        """Set rule's value
        """
        self._value = value

        return self

    @abstractmethod
    def validate(self) -> Any:
        """Validate the rule
        """
        raise NotImplementedError()


class Pass(Rule):
    """Pass rule
    """

    def validate(self):
        """Validate the rule
        """
        pass


class IsEmpty(Rule):
    """Empty rule
    """

    def validate(self):
        """Validate the rule
        """
        if self._value not in _EMPTY_OBJECTS:
            raise IsNotEmptyError(_('Must be empty'), self._value)


class IsNotEmpty(Rule):
    """Not empty rule
    """

    def validate(self):
        """Validate the rule
        """
        if self._value in _EMPTY_OBJECTS:
            raise IsEmptyError(_('Cannot be empty'), self._value)
