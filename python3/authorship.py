from types import SimpleNamespace

import vim  # noqa


# SimpleNamespace can be replaced with a class.
# These are variables set in vimrc.
# * `let g:snips_author = "My Name"`
# * `let g:snips_email = "my.email@email.com"`
# * `let g:snips_github = "MyGitHubUsername123"`

if not vim.eval('has("nvim")'):  # Vim
    author = SimpleNamespace(
        name=vim.vars.get('snips_author').decode('utf-8'),
        email=vim.vars.get('snips_email').decode('utf-8'),
        github=vim.vars.get('snips_github').decode('utf-8'),
    )
else:  # Neovim
    author = SimpleNamespace(
        name=vim.vars.get('snips_author'),
        email=vim.vars.get('snips_email'),
        github=vim.vars.get('snips_github'),
    )
