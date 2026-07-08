# Copyright 2026 Open Robotics
"""Tests for pagefind.yml loading."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, 'plugins')

from pagefind_config import load_search_result_meta_order  # noqa: E402


def test_load_search_result_meta_order_from_repo_pagefind_yml() -> None:
    confdir = str(Path(__file__).resolve().parent.parent)
    order = load_search_result_meta_order(confdir)
    assert order['product'] == 'Product'
    assert order['distribution'] == 'Distribution'
    assert order['area'] == 'Area'
    assert order['experience'] == 'Level'
    assert list(order.keys()).index('product') < list(order.keys()).index('area')


def test_load_search_result_meta_order_missing_file_returns_empty() -> None:
    assert load_search_result_meta_order('/nonexistent/path') == {}
