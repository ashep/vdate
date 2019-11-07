"""Comparing Rules Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.compare import Less, LessOrEquals, Greater, GreaterOrEquals, Equals, NotEquals
from vdate.rule.error import NotLessError, NotLessOrEqualsError, NotGreaterError, NotGreaterOrEqualsError, \
    NotEqualsError, EqualsError
from .base import BaseTest


class TestRuleCompare(BaseTest):
    def test_less(self):
        n = self.rand_int()
        r = Less(n)

        r.set_value(n - 1).validate()

        with pytest.raises(NotLessError):
            r.set_value(n).validate()

        with pytest.raises(NotLessError):
            r.set_value(n + 1).validate()

    def test_less_or_equals(self):
        n = self.rand_int()
        r = LessOrEquals(n)

        r.set_value(n - 1).validate()
        r.set_value(n).validate()

        with pytest.raises(NotLessOrEqualsError):
            r.set_value(n + 1).validate()

    def test_greater(self):
        n = self.rand_int()
        r = Greater(n)

        r.set_value(n + 1).validate()

        with pytest.raises(NotGreaterError):
            r.set_value(n).validate()

        with pytest.raises(NotGreaterError):
            r.set_value(n - 1).validate()

    def test_greater_or_equals(self):
        n = self.rand_int()
        r = GreaterOrEquals(n)

        r.set_value(n).validate()
        r.set_value(n + 1).validate()

        with pytest.raises(NotGreaterOrEqualsError):
            r.set_value(n - 1).validate()

    def test_equals(self):
        for t1 in BaseTest.BASE_TYPES:
            v = self.rand_of_type(t1)
            r = Equals(v)

            for t2 in BaseTest.BASE_TYPES:
                if t2 == t1:
                    r.set_value(v).validate()
                else:
                    with pytest.raises(NotEqualsError):
                        r.set_value(self.rand_of_type(t2)).validate()

    def test_not_equals(self):
        for t1 in BaseTest.BASE_TYPES:
            v = self.rand_of_type(t1)
            r = NotEquals(v)

            for t2 in BaseTest.BASE_TYPES:
                if t2 != t1:
                    r.set_value(self.rand_of_type(t2)).validate()
                else:
                    with pytest.raises(EqualsError):
                        r.set_value(v).validate()

