#!/usr/bin/env python3

from hypothesis import given, settings, Verbosity
from hypothesis_aws import fake_instance_ids


# fake_instance_ids() defaults to all so you should get long and short IDS
@given(fake_instance_ids())
@settings(max_examples=20, verbosity=Verbosity.verbose)
def test_all_instance_ids(instance_id):
    assert instance_id == instance_id


@given(fake_instance_ids(id_type="short"))
@settings(max_examples=20, verbosity=Verbosity.verbose)
def test_short_instance_ids(instance_id):
    assert instance_id == instance_id


@given(fake_instance_ids(id_type="long"))
@settings(max_examples=20, verbosity=Verbosity.verbose)
def test_long_instance_ids(instance_id):
    assert instance_id == instance_id
