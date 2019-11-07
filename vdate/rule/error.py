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


class EmptyError(RuleError):
    """Empty
    """
    pass


class NotEmptyError(RuleError):
    """Not empty
    """
    pass


class NotLessError(RuleError):
    """Is not less than
    """


class NotLessOrEqualsError(RuleError):
    """Is not less or equals
    """


class NotGreaterError(RuleError):
    """Is not greater than
    """


class NotGreaterOrEqualsError(RuleError):
    """Is not greater or equals
    """


class EqualsError(RuleError):
    """Equals
    """


class NotEqualsError(RuleError):
    """Not equals
    """


class NotNumberError(RuleError):
    """Is not a number error
    """


class NotIntegerError(NotNumberError):
    """Is not an integer number error
    """


class NotFloatError(NotNumberError):
    """Is not a float number error
    """


class NotDecimalError(NotNumberError):
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
