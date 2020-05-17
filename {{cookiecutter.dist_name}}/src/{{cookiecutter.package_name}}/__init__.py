"""{{cookiecutter.project_short_description}}"""
from ._version import get_versions


def a_method(a: int) -> int:
    """Return the double of `a`."""
    return 2 * a


__version__ = get_versions()["version"]
del get_versions
