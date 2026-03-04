"""Tests for lite-csv-dict."""

import os
import tempfile
import pytest
from lite_csv_dict import dict


class TestDict:
    """Test suite for dict."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = dict(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            dict("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = dict(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
