from distutils.core import setup

from distutils.core import setup
setup(
  name = 'pyRAMSpec',
  packages = ['pyRAMSpec'], # this must be the same as the name above
  version = '0.1',
  description = 'A cross platform ram specification identification',
  author = 'Xing Wang',
  author_email = 'wangxing.pku@gmail.com',
  url = 'https://github.com/wx1988/pyRAMSpec',
  download_url = '', # I'll explain this in a second
  keywords = ['system', 'RAM', 'cross platform'], # arbitrary keywords
  classifiers = [],
)

# NOTE: this is the old
#import py2exe
#setup(console=['get_specification.py'])
