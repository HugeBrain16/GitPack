# exceptions
class RequestError(Exception):
	pass

class PackageError(Exception):
	pass

class Pack:
	def install(user, repo, keep_source=False, quiet=False):
		import requests, zipfile, os, sys, subprocess, shutil, random, site
		from distutils.dir_util import copy_tree

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
		if not quiet: print('Preparing to download package...')

		# get main branch ig
		r = requests.get(f'https://api.github.com/repos/{user}/{repo}/branches')
		g_branch = r.json()
		branch = g_branch[0]['name']

		r = requests.get(f'https://github.com/{user}/{repo}/archive/{branch}.zip',stream=True)
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
		if not 'setup.py' in os.listdir(f'{repo}-{branch}'):
			if not keep_source: os.remove(f'{token}_{repo}.zip')
			shutil.rmtree(f'{repo}-{branch}')
			raise PackageError('`setup.py` file not found in default branch.')

		# check dependencies
		if not quiet: print('Checking dependencies...')
		if 'requirements.txt' in os.listdir(f'{repo}-{branch}'):
			if not quiet: print('Installing dependencies...')
			if not quiet: subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', f'{repo}-{branch}/requirements.txt'])
			if quiet: subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', f'{repo}-{branch}/requirements.txt'])

		# installing
		os.chdir(f'{repo}-{branch}/') # hmm...
		if not quiet: subprocess.check_call([sys.executable, 'setup.py', 'build'])
		else: subprocess.check_call([sys.executable, 'setup.py', '-q', 'build'])
		for d in os.listdir('build/lib/'):
			try:
				os.mkdir(f'{site.getsitepackages()[1]}\\{d}')
			except FileExistsError:
				shutil.rmtree(f'{site.getsitepackages()[1]}\\{d}')
				os.mkdir(f'{site.getsitepackages()[1]}\\{d}')
			copy_tree(f'build/lib/{d}',f"{site.getsitepackages()[1]}\\{d}")
		
		try:
			shutil.rmtree(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info')
		except: pass
		os.mkdir(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info')
		with open(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info\\LIBS','a+') as f:
			for d in os.listdir('build/lib/'):
				f.write(f"{d}\r")

		os.chdir('../') #hmm......

		# clean temp files
		if not quiet: print('Cleaning up...')
		if not keep_source: os.remove(f'{token}_{repo}.zip')
		shutil.rmtree(f'{repo}-{branch}')
		print('Package has been successfully installed!')

	def uninstall(user, repo, keep_source=False, quiet=False):
		import requests, zipfile, os, sys, subprocess, shutil, random, site
		from distutils.dir_util import copy_tree

		keep_source=False # Override

		print('Preparing to uninstall package...') # huehue

		if not os.path.exists(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info') or not os.path.exists(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info\\LIBS'):
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
			if not quiet: print('Preparing to download package, download required to fetch module because the dist info folder did not exists...')

			# get main branch ig
			r = requests.get(f'https://api.github.com/repos/{user}/{repo}/branches')
			g_branch = r.json()
			branch = g_branch[0]['name']

			r = requests.get(f'https://github.com/{user}/{repo}/archive/{branch}.zip',stream=True)
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

			# uninstalling
			os.chdir(f'{repo}-{branch}/') # hmm...
			if not quiet: subprocess.check_call([sys.executable, 'setup.py', 'build'])
			else: subprocess.check_call([sys.executable, 'setup.py', '-q', 'build'])
			for d in os.listdir('build/lib/'):
				try:
					shutil.rmtree(f'{site.getsitepackages()[1]}\\{d}')
				except FileExistsError: pass
			os.chdir('../') #hmm......

			# clean temp files
			if not quiet: print('Cleaning up...')
			if not keep_source: os.remove(f'{token}_{repo}.zip')
			try:
				shutil.rmtree(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info')
			except:
				pass
			shutil.rmtree(f'{repo}-{branch}')
			print('Package has been successfully uninstalled!')

		else:
			# if dist info folder exists uninstall without fetching dist info from downloads
			with open(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info\\LIBS','r') as f:
				libs=f.readlines()
				for l in libs:
					try:
						shutil.rmtree(f'{site.getsitepackages()[1]}\\{l.strip()}')
					except: pass
			shutil.rmtree(f'{site.getsitepackages()[1]}\\{repo}-{user}.gitpack-info')
			print('Package has been successfully uninstalled!')

	def download(user, repo, dir='.', quiet=False):
		import requests, os
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
		if not quiet: print('Preparing to download package...')

		# get main branch ig
		r = requests.get(f'https://api.github.com/repos/{user}/{repo}/branches')
		g_branch = r.json()
		branch = g_branch[0]['name']

		if not os.path.exists(dir): return print('ERROR: Directory `{}` not found!'.format(dir))

		r = requests.get(f'https://github.com/{user}/{repo}/archive/{branch}.zip',stream=True)
		if dir.endswith(('/','\\')):
			with open(f'{dir}{repo}.zip','wb') as f:
				f.write(r.raw.read())
		else:
			with open(f'{dir}/{repo}.zip','wb') as f:
				f.write(r.raw.read())

		print('Package downloaded!')