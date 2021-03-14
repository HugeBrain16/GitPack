"""
install GitPack to site-package, without egg file, if gitpack installed with setup.py with no gitpack already installed,
it would install an egg file which has no temp directory for installing packages, i'm really bad at explaining things, so...

if you don't have gitpack installed, execute this script to install gitpack :)
"""

import subprocess, site, sys, os, shutil
from distutils.dir_util import copy_tree

print('Installing gitpack...')
subprocess.check_call([sys.executable, 'setup.py', 'build'])
for d in os.listdir('build/lib'):
	try:
		os.mkdir(f'{site.getsitepackages()[1]}\\{d}')
	except FileExistsError:
		shutil.rmtree(f'{site.getsitepackages()[1]}\\{d}')
		os.mkdir(f'{site.getsitepackages()[1]}\\{d}')
	copy_tree(f'build/lib/{d}',f"{site.getsitepackages()[1]}\\{d}")

try:
	shutil.rmtree(f'{site.getsitepackages()[1]}\\GitPack-HugeBrain16.gitpack-info')
except: pass
os.mkdir(f'{site.getsitepackages()[1]}\\GitPack-HugeBrain16.gitpack-info')
with open(f'{site.getsitepackages()[1]}\\GitPack-HugeBrain16.gitpack-info\\LIBS','a+') as f:
	for d in os.listdir('build/lib/'):
		f.write(f"{d}\r")

shutil.copy2('gitpack.ini',f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info')

print('gitpack installed!')