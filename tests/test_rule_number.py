"""Number Rules Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.error import NotNumberError, NotIntegerError, NotFloatError, NotDecimalError
from vdate.rule.number import IsNumber, IsInteger, IsFloat, IsDecimal
from .base import BaseTest


class TestRuleNumber(BaseTest):
    """Length VDate rules tests
    """
    _not_numbers = (None, str(), list(), set(), dict())

    def test_number(self):
        for v in self._not_numbers:
            with pytest.raises(NotNumberError):
                IsNumber(v).validate()

    def test_integer(self):
        for v in self._not_numbers:
            with pytest.raises(NotIntegerError):
                IsInteger(v).validate()

    def test_float(self):
        for v in self._not_numbers:
            with pytest.raises(NotFloatError):
                IsFloat(v).validate()

    def test_decimal(self):
        for v in self._not_numbers:
            with pytest.raises(NotDecimalError):
                IsDecimal(v).validate()
