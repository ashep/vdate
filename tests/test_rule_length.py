"""Length rules tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from vdate.rule.length import LengthRule, MinLengthRule, MaxLengthRule
from vdate.rule.error import LengthRuleError
from .base import BaseTest


class TestRuleLength(BaseTest):
    """Length VDate rules tests
    """

    def test_length(self):
        with pytest.raises(TypeError):
            LengthRule().validate()

        min_len = self.rand_int(1, 10)
        max_len = self.rand_int(10, 20)
        min_list = self.rand_list(min_len, min_len + 1)
        max_list = self.rand_list(max_len, max_len + 1)

        # Testing LengthRule
        length_rule = LengthRule(min_len, max_len)
        assert length_rule.set_value(min_list).validate() is None
        assert length_rule.set_value(max_list).validate() is None
        with pytest.raises(LengthRuleError):
            assert length_rule.set_value(min_list[:-1]).validate() is None
        with pytest.raises(LengthRuleError):
            length_rule.set_value(max_list + [self.rand_int()]).validate()

        # Testing MinLengthRule
        min_length_rule = MinLengthRule(min_len)
        assert min_length_rule.set_value(min_list).validate() is None
        with pytest.raises(LengthRuleError):
            min_length_rule.set_value(min_list[:-1]).validate()

        # Testing MaxLengthRule
        max_length_rule = MaxLengthRule(max_len)
        assert max_length_rule.set_value(max_list).validate() is None
        with pytest.raises(LengthRuleError):
            max_length_rule.set_value(max_list + [self.rand_int()]).validate()
