from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'bpython',
    'pyramid > 1.6a2',
]

entry_points = {
    'pyramid.pshell_runner': [
        'bpython = pyramid_bpython:bpython_shell_runner',
    ],
}

setup(
    name='pyramid_bpython',
    version='0.1',
    description='pyramid bpython pshell',
    long_description=README,
    author='Michael Merickel',
    author_email='pylons-discuss@googlegroups.com',
    url='https://github.com/Pylons/pyramid_bpython',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ],
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    zip_safe=False,
    py_modules=['pyramid_bpython'],
    install_requires=requires,
    entry_points=entry_points,
)
