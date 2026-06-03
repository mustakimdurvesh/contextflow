from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='contextflow',
    version='0.1.0',
    author='Mustakimur Rahman Durvesh',
    author_email='contact@example.com',
    description='Distributed Context Management Library for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mustakimdurvesh/contextflow',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.8',
    install_requires=[
        'msgpack>=1.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=3.0',
            'black>=22.0',
            'flake8>=4.0',
            'mypy>=0.950',
        ],
        'fastapi': ['fastapi>=0.95.0', 'starlette>=0.26.0'],
        'flask': ['flask>=2.0'],
    },
)
