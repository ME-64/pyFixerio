from setuptools import setup
setup(
  name = 'pyfixerio'
  packages = ['pyfixerio']
  version = '0.0.1'
  license='MIT'
  description = 'a python API wrapper for the free fixer.io API'
  author = 'YOUR NAME'
  author_email = 'your.email@domain.com'
  url = 'https://github.com/ME-64/pyfixerio'
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['wrapepr', 'FX', 'foreignexchange']
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
