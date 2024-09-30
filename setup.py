# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

from djangosaml2idp import __version__

setup(
    name='djsaml2-idp-app',
    version=__version__,
    description='SAML 2.0 Identity Provider for Django',
    keywords="django,pysaml2,sso,saml2,federated authentication,authentication,idp",
    author='Abhishek Baddi',
    author_email='abybaddi009@gmail.com',
    maintainer="Abhishek Baddi",
    long_description="\n\n".join([
        open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    ]),
    install_requires=[
        'django>=2.2',
        'pysaml2>=6.5.1',
        'pytz',
        'arrow',
    ],
    extras_require={
        "testing": [
            "pytest",
            "pytest-runner",
            "pytest-django",
            "pytest-cov",
            "pytest-pythonpath",
            "pytest-mock",
            "requests-mock"
        ]
    },
    python_requires=">=3.6",
    license='Apache Software License 2.0',
    packages=find_packages(exclude=["tests*", "docs", "example_setup"]),
    url='https://github.com/abybaddi009/djangosaml2idp/',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
