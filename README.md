# GitPack

GitPack is a github python package installer.

### Installation
`python install.py`, i recommended to not install gitpack with `setup.py` if you don't have gitpack installed

### Usage

to install a package type the following command:</br>
- `python -m gitpack install <repo-author> <repo-name>`

for example:
- `python -m gitpack install HugeBrain16 iniparser2`</br>
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
