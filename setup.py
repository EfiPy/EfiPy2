from setuptools import setup, find_packages

setup (
  name          = 'EfiPy2',
  version       = '0.1.0',
  description   = 'EFI python wrapper',
  author        = 'Max Wu',
  author_email  = 'EfiPy.Core@gmail.com',
  url           = 'https://github.com/EfiPy/EfiPy2',
  packages      = find_packages (where='Src'),
  package_dir   = {"": "Src", }
  )
