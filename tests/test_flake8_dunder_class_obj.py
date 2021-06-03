# -*- coding: utf-8 -*-
"""
Test flake8_dunder_class_obj.

Basic tests for flake8_dunder_class_obj
"""

import flake8_dunder_class_obj


def test_flake8_dunder_class_obj_version():
    """Check __version__."""
    assert flake8_dunder_class_obj.__version__.startswith("0.")
