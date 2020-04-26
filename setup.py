from setuptools import setup, find_packages
from pathlib import Path

meta = {}
exec(Path('procesark/__init__.py').read_text(), meta)

setup(
    name='procesark',
    version=meta['__version__'],
    author='Knowark',
    description='Process Coordinator and Scheduler',
    python_requires='>=3.6.0',
    packages=find_packages(),
    scripts='./scripts/procesark',
    install_requires=['aiohttp==3.*,>=3.6.2', 'uvloop==0.*,>=0.14.0'],
    extras_require={
        "dev": ["pytest==5.*,>=5.4.1", "pytest-asyncio==0.*,>=0.11.0"]
    }
)
