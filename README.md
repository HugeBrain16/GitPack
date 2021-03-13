# GitPack

GitPack is a github python package installer.</br>
how it works is just basically downloading the main branch of the repository,</br>
then using subprocess to build the package and install it.

### Usage

to install a package type the following command:<\br>
- `gitpack.py <repo-author> <repo-name>`
- `gitpack.py HugeBrain16 iniparser2`

#### Optional arguments

###### General optional arguments
- `-V --version` show version
- `-h --help`

###### Additional arguments
- `-q --quiet`, Disable some installation progress messages.
- `--keep_source`, Keep the package source after installation complete (without token name).

the supported packages usually have the `setup.py` file in the main branch.