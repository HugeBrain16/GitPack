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
from .pack import Pack
import argparse
from .__init__ import __version__, __author__

parser = argparse.ArgumentParser(description='Install python packages from github.')
parser.add_argument('-V','--version',action='version',version=f'GitPack v{__version__}')
_s = parser.add_subparsers(dest='cmd')
for cmd in ['install','uninstall','download']:
	_p_s = _s.add_parser(cmd)
	_p_s.add_argument('user',type=str,help='repository author')
	_p_s.add_argument('repository',type=str,help='repository name')
for cmd in ['list']:
	_p_s = _s.add_parser(cmd)

parser.add_argument('-d','--directory',type=str,help='download directory')
parser.add_argument('-q','--quiet',action='store_true',help='disable installation progress messages.')
parser.add_argument('--keep_source',action='store_true',help='keep the source file after installation complete.')
parser.add_argument('--branch',type=str,help='repository branch')
parser.add_argument('-U','--update',action='store_true',help='Update package')

args = parser.parse_args()

if args.cmd == 'install':
	if not args.branch: Pack.install(args.user,args.repository,keep_source=args.keep_source,quiet=args.quiet,update=args.update)
	else: Pack.install(args.user,args.repository,args.branch,args.keep_source,args.quiet,args.update)
elif args.cmd == 'uninstall': Pack.uninstall(args.user,args.repository,args.quiet)
elif args.cmd == 'download': 
	if args.directory: 
		if not args.branch: Pack.download(args.user,args.repository,dir=args.directory,quiet=args.quiet)
		else: Pack.download(args.user,args.repository,args.branch,args.directory,args.quiet)
	elif not args.directory:
		if not args.branch: Pack.download(args.user,args.repository,quiet=args.quiet)
		else: Pack.download(args.user,args.repository,args.branch,quiet=args.quiet)
elif args.cmd == 'list': Pack.list()