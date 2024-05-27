#!/usr/bin/env python

"""Tests for `PythonProfilingCode` package."""
import pytest


@pytest.fixture()
def setup():
    print("hi")
    yield
    print("end")
