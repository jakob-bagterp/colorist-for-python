import os
import sys

import pytest


def test_python_version_matches_ci_matrix() -> None:
    """Ensure that each CI job tests the Python version of its matrix entry, e.g. that a job for Python 3.14 isn't silently tested on Python 3.11."""

    expected_version = os.environ.get("EXPECTED_PYTHON_VERSION")
    if not expected_version:
        pytest.skip("EXPECTED_PYTHON_VERSION isn't set, e.g. when running the tests locally.")
    assert f"{sys.version_info.major}.{sys.version_info.minor}" == expected_version
