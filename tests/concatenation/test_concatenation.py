#!/usr/bin/env python

"""Tests for `PythonProfilingCode` package."""

import pytest
from src.modules.profilingCode.concatenation.methodejoin1 import methodejoin1
from src.modules.profilingCode.concatenation.methodejoin2 import methodejoin2
from src.modules.profilingCode.concatenation.methodejoin3 import methodejoin3


@pytest.mark.usefixtures("setup")
class TestConcatenation:
    def test_methodejoin1(self):
        assert methodejoin1(5) == 'NameNameNameNameName'

    def test_methodejoin2(self):
        assert methodejoin2(5) == 'NameNameNameNameName'

    def test_methodejoin3(self):
        assert methodejoin3(5) == '0 x 10 = 0 ; 1 x 10 = 10 ; 2 x 10 = 20 ; 3 x 10 = 30 ; 4 x 10 = 40 ; '
