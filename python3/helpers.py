import vim  # noqa


def expand(snip, jump_pos=1):
    if snip.tabstop != jump_pos:
        return

    vim.eval(r'feedkeys("\<C-R>=UltiSnips#ExpandSnippet()\<CR>")')
