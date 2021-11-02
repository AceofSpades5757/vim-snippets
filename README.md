[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Description

Collection of snippets used in conjunction with UltiSnips for Vim and Neovim.

Cleaned for public use and readability.

# Contents

`snips`

* Has snippets inside, layed out as used by UltiSnips.

# Credit

* [UltiSnips](https://github.com/SirVer/ultisnips)
* [Community Snippets](https://github.com/honza/vim-snippets)

# Globals (Python)

To find the Python imports used, check the `python` folder which would be located in your `.vim`/`vimfiles` directory (see `:help pythonx-directory` in Vim).

* Windows: `%USERPROFILE%\vimfiles\python3\my_module.py`
* Linux: `~/.vim/python3/my_module.py`

``` UltiSnip
global !p

from my_module import my_function
from my_module import my_var
from my_module import MyClass

endglobal
```
