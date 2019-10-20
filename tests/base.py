"""
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import sys
import string
from random import choice, randrange


class BaseTest:
    def rand_int(self, min_value: int = None, max_value: int = None) -> int:
        return randrange(min_value or -sys.maxsize, max_value or sys.maxsize)

    def rand_str(self) -> str:
        return ''.join([choice(string.printable) for n in range(8)])

    def rand_list(self, min_length: int = 0, max_length: int = 100) -> list:
        return [self.rand_int() for _ in range(randrange(min_length, max_length))]
