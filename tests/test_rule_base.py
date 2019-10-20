"""Base rules tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.base import BaseRule, PassRule, EmptyRule, NonEmptyRule
from vdate.rule.error import EmptyRuleError, NonEmptyRuleError
from .base import BaseTest


class TestRuleBase(BaseTest):
    """Base VDate rules tests
    """

    def test_base(self):
        with pytest.raises(TypeError):
            BaseRule()

    def test_value(self):
        r = PassRule()

        v = self.rand_str()
        r.set_value(v)
        assert r.get_value() == r.value == v

        v = self.rand_str()
        r.value = v
        assert r.get_value() == r.value == v

    def test_pass(self):
        PassRule().validate()

    def test_empty(self):
        r = EmptyRule()

        for v in (None, '', [], {}, set(), tuple()):
            r.set_value(v).validate()

        for v in (0, 0.0, False):
            with pytest.raises(EmptyRuleError):
                r.set_value(v).validate()

    def test_non_empty(self):
        r = NonEmptyRule()

        for v in (0, 0.0, False):
            r.set_value(v).validate()

        for v in (None, '', [], {}, set(), tuple()):
            with pytest.raises(NonEmptyRuleError):
                r.set_value(v).validate()
