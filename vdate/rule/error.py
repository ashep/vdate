"""VDate Errors
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
    """Empty error
    """
    pass


class IsNotEmptyError(RuleError):
    """Not empty error
    """
    pass


class NumberRuleError(RuleError):
    """Number rule error
    """


class IsNotNumberError(NumberRuleError):
    """Is not a number error
    """


class IsNotIntegerError(NumberRuleError):
    """Is not an integer number error
    """


class IsNotDecimalError(NumberRuleError):
    """Is not a decimal number error
    """


class TooSmallError(NumberRuleError):
    """Too small number error
    """


class TooBigError(NumberRuleError):
    """Too big number error
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
