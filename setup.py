from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='coveragecalc',
      version='0.1',
      description='Exports xlsx IDC coverage from a given spreadsheet with IDC output fields',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
      ],
      keywords='pandas IDC coverage hit-rates',
      url='https://github.com/myu-wp/coveragecalc',
      author='Mike Yu',
      author_email='myu@whitepages.com',
      license='MIT',
      packages=['coveragecalc'],
      install_requires=[
        'pandas',
        'numpy',
        'openpyxl',
      ],
      entry_points={
        'console_scripts': ['coveragecalc=coveragecalc.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)