# Copyright (c) 2021 HugeBrain16

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
						GITPACK

GitPack is a script for installing python packages from github repositories.

"""

import argparse

__version__ = '0.0.1'
__author__ = 'HugeBrain16 <joshtuck373@gmail.com>'

# exceptions
class RequestError(Exception):
	pass

class PackageError(Exception):
	pass

class Pack:
	def install(user, repo, keep_source=False, quiet=False):
		import requests, zipfile, os, sys, subprocess, shutil, random

		print('Preparing to install package...') # huehue

		# check user
		if not quiet: print('Checking github user...')
		r = requests.get(f'https://github.com/{user}')
		if r.status_code == 404:
			raise RequestError('could not find user `{}`'.format(user))
		elif r.status_code != 200:
			raise RequestError('could not check user `{}`, error code: {}'.format(user,r.status_code))

		# check repo
		if not quiet: print('Checking github user repository...')
		r = requests.get(f'https://github.com/{user}/{repo}')
		if r.status_code == 404:
			raise RequestError('could not find repository `{}` from user `{}`'.format(repo,user))
		elif r.status_code != 200:
			raise RequestError('could not check repository `{}` from user `{}`, error code: {}'.format(repo,user,r.status_code))

		# download repo
		if not quiet: print('Downloading package...')
		r = requests.get(f'https://github.com/{user}/{repo}/archive/main.zip',stream=True)
		char = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
				'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
				'1','2','3','4','5','6','7','8','9','0']
		ret_char = list()
		for i in range(8):
			ret_char.append(random.choice(char))
		token = ''.join(ret_char)
		if not keep_source:
			with open(f'{token}_{repo}.zip','wb') as f:
				f.write(r.raw.read())
		elif keep_source:
			with open(f'{repo}.zip','wb') as f:
				f.write(r.raw.read())

		# extract
		if not quiet: print('Extracting Package...')
		if not keep_source:	
			with zipfile.ZipFile(f'{token}_{repo}.zip','r') as f:
				f.extractall()
		elif keep_source:
			with zipfile.ZipFile(f'{repo}.zip','r') as f:
				f.extractall()

		# check dir
		if not quiet: print('Installing package...')
		if not 'setup.py' in os.listdir(f'{repo}-main'):
			if not keep_source: os.remove(f'{token}_{repo}.zip')
			shutil.rmtree(f'{repo}-main')
			raise PackageError('`setup.py` file not found in main branch.')

		# check dependencies
		if not quiet: print('Checking dependencies...')
		if 'requirements.txt' in os.listdir(f'{repo}-main'):
			if not quiet: print('Installing dependencies...')
			if not quiet: subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', f'{repo}-main/requirements.txt'])
			if quiet: subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', f'{repo}-main/requirements.txt'])

		# installing
		os.chdir(f'{repo}-main/') # hmm...
		if not quiet: subprocess.check_call([sys.executable, 'setup.py', 'install', '--user'])
		else: subprocess.check_call([sys.executable, 'setup.py', '-q', 'install', '--user'])
		os.chdir('../') #hmm......

		# clean temp files
		if not quiet: print('Cleaning up...')
		if not keep_source: os.remove(f'{token}_{repo}.zip')
		shutil.rmtree(f'{repo}-main')
		print('Package has been successfully installed!')

parser = argparse.ArgumentParser(description='Install python packages from github.')
parser.add_argument('-V','--version',action='version',version=f'GitPack v{__version__}')
parser.add_argument('user',type=str,help='repository author.')
parser.add_argument('repository',type=str,help='package\'s repository.')

parser.add_argument('-q','--quiet',action='store_true',help='disable installation progress messages.')
parser.add_argument('--keep_source',action='store_true',help='keep the source file after installation complete.')

args = parser.parse_args()

Pack.install(args.user,args.repository,args.keep_source,args.quiet)