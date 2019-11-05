"""Number Rules Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.error import IsNotNumberError, IsNotIntegerError, IsNotFloatError
from vdate.rule.number import IsNumber, IsInteger, IsFloat
from .base import BaseTest


class TestRuleNumber(BaseTest):
    """Length VDate rules tests
    """
    _not_numbers = (None, str(), list(), set(), dict())

    def test_number(self):
        for v in self._not_numbers:
            with pytest.raises(IsNotNumberError):
                IsNumber(v).validate()

    def test_integer(self):
        for v in self._not_numbers:
            with pytest.raises(IsNotIntegerError):
                IsInteger(v).validate()

    def test_float(self):
        for v in self._not_numbers:
            with pytest.raises(IsNotFloatError):
                IsFloat(v).validate()
