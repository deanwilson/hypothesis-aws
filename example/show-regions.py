#!/usr/bin/env python3

from hypothesis import given, settings, Verbosity
from hypothesis_aws import fake_regions


@given(fake_regions())
@settings(max_examples=10, verbosity=Verbosity.verbose)
def test_display_region(region):
    assert region == region
