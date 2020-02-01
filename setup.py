from setuptools import setup
import pathlib


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
  name = 'pyfixerio',
  packages = ['pyfixerio'],
  version = '0.1.2',
  license='MIT',
  description = 'a python API wrapper for the free fixer.io API',
  # long_description = README,
  #long_description_content_type = 'text/markdown',
  author = 'ME-64',
  author_email = 'miloelliott64@gmail.com',
  url = 'https://github.com/ME-64/pyfixerio',
  keywords = ['API wrapper', 'FX', 'foreign exchange'],
  include_package_data = True,
  install_requires=[           
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',




  ],
)
