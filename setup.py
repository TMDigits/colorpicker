from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='colorpicker',
    version='0.1.0',
    description='A color picker from any screen pixel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TMDigits/colorpicker',
    author='TMD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='pixel, colorpicker, design',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6, <4',
    install_requires=[
        'wxpython',
        'pynput',
    ],
    extras_require={
        'dev': ['check-manifest', 'autopep8', 'pyinstaller'],
        'test': ['coverage', 'pytest', 'tox', 'flake8'],
    },

    entry_points={
        'console_scripts': [
            'colorpicker=colorpicker:create_window',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/TMDigits/colorpicker/issues',
        'Say Thanks!': 'https://saythanks.io/to/TMDigits',
        'Source': 'https://github.com/TMDigits/colorpicker',
    },
)
