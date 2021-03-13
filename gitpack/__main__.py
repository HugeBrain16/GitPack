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
parser.add_argument('cmd',choices=['install','download','uninstall'],type=str)
parser.add_argument('user',type=str,help='repository author.')
parser.add_argument('repository',type=str,help='package\'s repository.')

parser.add_argument('-d','--directory',type=str,help='download directory')
parser.add_argument('-q','--quiet',action='store_true',help='disable installation progress messages.')
parser.add_argument('--keep_source',action='store_true',help='keep the source file after installation complete.')

args = parser.parse_args()

if args.cmd == 'install': Pack.install(args.user,args.repository,args.keep_source,args.quiet)
elif args.cmd == 'uninstall': Pack.uninstall(args.user,args.repository,args.keep_source,args.quiet)
elif args.cmd == 'download': 
	if args.directory: Pack.download(args.user,args.repository,args.directory,args.quiet)
	elif not args.directory: Pack.download(args.user,args.repository,quiet=args.quiet)