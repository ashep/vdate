"""VDate Base Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any
from abc import ABC, abstractmethod
from .._gettext import _
from .error import IsEmptyError, IsNotEmptyError, NotEqualsError, EqualsError, TooBigError, TooSmallError

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


class PassRule(Rule):
    """Pass rule
    """

    def validate(self):
        """Validate the rule
        """
        pass


class IsEmptyRule(Rule):
    """Empty rule
    """

    def validate(self):
        """Validate the rule
        """
        if self._value not in _EMPTY_OBJECTS:
            raise IsEmptyError(_('Must be empty'), self._value)


class IsNonEmptyRule(Rule):
    """Not empty rule
    """

    def validate(self):
        """Validate the rule
        """
        if self._value in _EMPTY_OBJECTS:
            raise IsNotEmptyError(_('Cannot be empty'), self._value)


class CompareRule(Rule):
    def __init__(self, compare_to: Any, cmp_op: str, value: Any = None):
        """Init.
        """
        super().__init__(value)

        self._compare_to = compare_to
        self._cmp_op = cmp_op

    def validate(self):
        """Validate the rule
        """
        if self._cmp_op == '<':
            if self._value >= self._compare_to:
                raise TooBigError(_('Is too big'))
        elif self._cmp_op == '<=':
            if self._value > self._compare_to:
                raise TooBigError(_('Is too big'))
        elif self._cmp_op == '>':
            if self._value <= self._compare_to:
                raise TooSmallError(_('Is too small'))
        elif self._cmp_op == '>=':
            if self._value < self._compare_to:
                raise TooSmallError(_('Is too small'))
        elif self._cmp_op == '==':
            if self._value != self._compare_to:
                raise NotEqualsError(_('Not equals {}').format(repr(self._compare_to)))
        elif self._cmp_op == '!=':
            if self._value == self._compare_to:
                raise EqualsError(_('Equals {}').format(repr(self._compare_to)))
        else:
            raise ValueError('Unknown comparing operator: {}'.format(self._cmp_op))
