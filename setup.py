import setuptools

def read(fname):
	with open(fname,'r') as f:
		return f.read()

setuptools.setup(
name='GitPack',
version='0.0.3',
author='HugeBrain16',
author_email='joshtuck373@gmail.com',
description='A script for installing python packages from github',
license='MIT',
keywords='package-installer github',
url='https://github.com/HugeBrain16/GitPack',
packages=setuptools.find_packages(),
long_description=read('README.md'),
long_description_content_type='text/markdown',
classifiers=[
		"Development Status :: 4 - Beta",
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers'
	]
)