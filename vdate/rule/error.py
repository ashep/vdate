"""Vdate Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Any


class RuleError(Exception):
    """Base rule error
    """

    def __init__(self, msg: str, rule_value: Any = None):
        """Init
        """
        self._msg = msg
        self._rule_value = rule_value

    def __str__(self) -> str:
        """__str__()
        """
        return self._msg

    @property
    def msg(self) -> str:
        """Get error's message
        """
        return self._msg

    @property
    def rule_value(self) -> Any:
        """Get rule's value
        """
        return self._rule_value


class IsEmptyError(RuleError):
    """Empty
    """
    pass


class IsNotEmptyError(RuleError):
    """Not empty
    """
    pass


class IsNotLess(RuleError):
    """Is not less than
    """


class IsNotLessOrEquals(RuleError):
    """Is not less or equals
    """


class IsNotGreater(RuleError):
    """Is not greater than
    """


class IsNotGreaterOrEquals(RuleError):
    """Is not greater or equals
    """


class EqualsError(RuleError):
    """Equals
    """


class NotEqualsError(RuleError):
    """Not equals
    """


class IsNotNumberError(RuleError):
    """Is not a number error
    """


class IsNotIntegerError(IsNotNumberError):
    """Is not an integer number error
    """


class IsNotFloatError(IsNotNumberError):
    """Is not a float number error
    """


class IsNotDecimalError(IsNotNumberError):
    """Is not a decimal number error
    """


class LengthRuleError(RuleError):
    """Length rule error
    """


class TooShortError(LengthRuleError):
    """Too short error
    """


class TooLongError(LengthRuleError):
    """Too long error
    """
