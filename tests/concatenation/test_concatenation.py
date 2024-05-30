#!/usr/bin/env python

"""Tests for `PythonProfilingCode` package."""

import pytest
from src.modules.profilingCode.concatenation.avoidlistcomprehensioniniterationsbad import avoidlistcomprehensioniniterationsbad
from src.modules.profilingCode.concatenation.avoidlistcomprehensioniniterationsgood import avoidlistcomprehensioniniterationsgood
from src.modules.profilingCode.concatenation.avoiddoublequotecheckbad import avoiddoublequotecheckbad
from src.modules.profilingCode.concatenation.avoiddoublequotecheckgood import avoiddoublequotecheckgood


@pytest.mark.usefixtures("setup")
class TestConcatenation:
    def test_avoidlistcomprehensioniniterationsbad(self):
        assert avoidlistcomprehensioniniterationsbad(5) == 'NameNameNameNameName'

    def test_avoidlistcomprehensioniniterationsgood(self):
        assert avoidlistcomprehensioniniterationsgood(5) == 'NameNameNameNameName'

    def test_avoiddoublequotecheckgood(self):
        assert avoiddoublequotecheckgood(5) == ['Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen'
    ]

    def test_avoiddoublequotecheckbad(self):
        assert avoiddoublequotecheckbad(5) == ['Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen',
    'Renault',
    'Fiat',
    'Citroen'
    ]

