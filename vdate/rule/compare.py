"""Vdate Comparative Rules
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any
from enum import Enum
from .._gettext import _
from .base import Rule
from .error import IsNotLess, IsNotGreater, IsNotLessOrEquals, IsNotGreaterOrEquals, EqualsError, NotEqualsError


class CompareOperator(Enum):
    """Compare operators
    """
    LT = '<'
    LTE = '<='
    GT = '>'
    GTE = '>='
    EQ = '=='
    NEQ = '!='


class Compare(Rule):
    """Base comparative rule
    """

    def __init__(self, cmp_op: CompareOperator, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(value)

        self._cmp_op = cmp_op
        self._compare_to = compare_to

    def validate(self):
        """Validate the rule
        """
        if self._cmp_op == CompareOperator.LT:
            if self._value >= self._compare_to:
                raise IsNotLess(_('Must be less than {}').format(self._compare_to))
        elif self._cmp_op == CompareOperator.LTE:
            if self._value > self._compare_to:
                raise IsNotLessOrEquals(_('Must be less or equal to {}').format(self._compare_to))
        elif self._cmp_op == CompareOperator.GT:
            if self._value <= self._compare_to:
                raise IsNotGreater(_('Must be greater than {}').format(self._compare_to))
        elif self._cmp_op == CompareOperator.GTE:
            if self._value < self._compare_to:
                raise IsNotGreaterOrEquals(_('Must be greater or equal to {}').format(self._compare_to))
        elif self._cmp_op == CompareOperator.EQ:
            if self._value != self._compare_to:
                raise NotEqualsError(_('Must be equal to {}').format(repr(self._compare_to)))
        elif self._cmp_op == CompareOperator.NEQ:
            if self._value == self._compare_to:
                raise EqualsError(_('Must not be equal to {}').format(repr(self._compare_to)))


class Less(Compare):
    """Less than
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.LT, compare_to, value)


class LessOrEquals(Compare):
    """Less or equals
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.LTE, compare_to, value)


class Greater(Compare):
    """Greater than
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.GT, compare_to, value)


class GreaterOrEquals(Compare):
    """Greater or equals
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.GTE, compare_to, value)


class Equals(Compare):
    """Equals
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.EQ, compare_to, value)


class NotEquals(Compare):
    """Not equals
    """

    def __init__(self, compare_to: Any, value: Any = None):
        """Init
        """
        super().__init__(CompareOperator.NEQ, compare_to, value)
