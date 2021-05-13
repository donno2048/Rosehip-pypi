from setuptools import setup,find_packages
setup(
    name='rosehip',
    include_package_data=True,
    version='1.0.6',
    description=open('README.md').readlines()[0].replace('\n', ''),
    long_description='\n'.join([i.replace('\n', '') for i in open('README.md').readlines()[1:]]),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url='https://github.com/donno2048/Rosehip-pypi',
    package_data={'rosehip': ['Rosehip'],},
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Operating System :: Microsoft :: Windows','License :: OSI Approved :: MIT License','Programming Language :: Python :: 3'],
    install_requires=['roin'],
    entry_points={ 'console_scripts': [ 'rosehip=Rosehip.__init__:laptop' ] }
)
