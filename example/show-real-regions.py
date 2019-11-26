#!/usr/bin/env python3
"""An example of using the `real regions` strategy"""

from hypothesis import given, settings, Verbosity
from hypothesis_aws import regions


@given(regions())
@settings(max_examples=30, verbosity=Verbosity.verbose)
def test_display_region(region):
    assert region == region
