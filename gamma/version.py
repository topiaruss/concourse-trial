try:
    from setuptools_scm import get_version
    __version__ = get_version()
except ImportError:
    print("No setuptools_scm - no version")
    __version__ = ''
