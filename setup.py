"""myhue setup tools, based on the sampleprojet on Github

See:
  https://packaging.python.org/guides/distributing-packages-using-setuptools/
  https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='myhue_Twilip',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Twirlip-of-the-Mists/myhue', 
    author='Twirlip of the Mists', 
    author_email='Sandor.at.the.Zoo@gmail.com',
    classifiers=[
        # How mature is this project? 
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Home Automation',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='hue',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6, <4',
    install_requires=[
        'click',
        'qhue',
        'click_config_file',
        'PyYAML',
        'dicttoxml',
    ],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    #data_files=[('my_data', ['data/data_file'])],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'myhue=myhue:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Twirlip-of-the-Mists/myhue/issues',
        #'Funding': 'https://donate.pypi.org',
        #'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/Twirlip-of-the-Mists/myhue/',
    },
)
