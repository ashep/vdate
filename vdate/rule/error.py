"""VDate Rule Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class RuleError(Exception):
    """Base rule error
    """
    pass


class EmptyRuleError(RuleError):
    """Empty rule error
    """
    pass


class NonEmptyRuleError(RuleError):
    """Non empty rule error
    """
    pass
