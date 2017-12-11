"""
To be run by the concourse pipeline before building componenent Dockers.
This script puts a version.py containing a version string into each
directory that contains a Dockerfile, so the Dockerfile CPs the
version into the image for debug logging.
"""
import glob

from setuptools_scm import get_version

dirs = [d.split('/')[0] for d in glob.glob('*/Dockerfile')]
for d in dirs:
    w_to = '%s/version.py' % d
    version = get_version(root="..",
                          relative_to=__file__,
                          write_to=w_to)
