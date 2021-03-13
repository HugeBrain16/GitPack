# GitPack

GitPack is a github python package installer.
</br>
how it works is just basically downloading the main branch of the repository,</br>
then using subprocess to build the package and install it.

### Installation
`python setup.py install --user`

### Usage

to install a package type the following command:</br>
- `python -m gitpack install <repo-author> <repo-name>`

for example:
- `python -m gitpack install HugeBrain16 iniparser2`
uninstall:
- `python -m gitpack uninstall <repo-author> <repo-name>`

### Updating GitPack
to update GitPack type the command below, make sure that you already have GitPack Installed:</br>
`python -m gitpack install HugeBrain16 GitPack`

### Arguments

#### Required
- `install` || `download` || `uninstall`
- `user`
- `repository`

#### Optional arguments

###### General optional arguments
- `-V --version` show version
- `-h --help`

###### Additional arguments
- `-d --directory`, Package download directory
- `-q --quiet`, Disable some installation progress messages.
- `--keep_source`, Keep the package source after installation complete (without token name).

the supported packages usually have the `setup.py` file in the 'default' branch.
