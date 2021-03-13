# GitPack

GitPack is a github python package installer.
</br>
how it works is just basically downloading the main branch of the repository,</br>
then using subprocess to build the package and install it.

### Installation
`python setup.py install --user`

### Usage

to install a package type the following command:</br>
- `python -m gitpack <repo-author> <repo-name>`
</br>
for example:</br>
- `python -m gitpack HugeBrain16 iniparser2`

#### Optional arguments

###### General optional arguments
- `-V --version` show version
- `-h --help`

###### Additional arguments
- `-q --quiet`, Disable some installation progress messages.
- `--keep_source`, Keep the package source after installation complete (without token name).

the supported packages usually have the `setup.py` file in the 'default' branch.