"""Base Rules Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.base import Rule, Pass, IsEmpty, IsNotEmpty, EmptyError, NotEmptyError
from vdate.rule.error import RuleError
from .base import BaseTest


class TestRuleBase(BaseTest):
    """Base VDate rules tests
    """

    def test_base(self):
        with pytest.raises(TypeError):
            Rule()

    def test_base_error(self):
        msg = self.rand_str()
        v = self.rand_str()
        e = RuleError(msg, v)

        assert str(e) == e.msg
        assert e.rule_value == v

    def test_value(self):
        r = Pass()

        v = self.rand_str()
        r.set_value(v)
        assert r.get_value() == r.value == v

        v = self.rand_str()
        r.value = v
        assert r.get_value() == r.value == v

    def test_pass(self):
        Pass().validate()

    def test_empty(self):
        r = IsEmpty()

        for v in (None, '', [], {}, set(), tuple()):
            r.set_value(v).validate()

        for v in (0, 0.0, False):
            with pytest.raises(NotEmptyError):
                r.set_value(v).validate()

    def test_non_empty(self):
        r = IsNotEmpty()

        for v in (0, 0.0, False):
            r.set_value(v).validate()

        for v in (None, '', [], {}, set(), tuple()):
            with pytest.raises(EmptyError):
                r.set_value(v).validate()
