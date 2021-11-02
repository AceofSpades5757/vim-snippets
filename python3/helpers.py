import vim  # noqa


def expand(snip, jump_pos=1):
    """ Expands snippet.

    Used with post_jump to automatically expand the snippet.

    Examples
    --------
    Alias Example

            snippet my_snippet_1 "Example snippet."
            What my snippet will expand to.
            endsnippet

            post_jump "expand(snip)"
            snippet my_snippet_2 "Using the post_jump, this acts for an alias to my_snippet_1."
            my_snippet_1$1
            endsnippet
    """
    if snip.tabstop != jump_pos:
        return

    vim.eval(r'feedkeys("\<C-R>=UltiSnips#ExpandSnippet()\<CR>")')


def expand_anon(snip):

    start_line = snip.snippet_start[0]
    end_line = snip.snippet_end[0]

    spaces = vim.eval(f'indent({start_line})')
    shiftwidth = vim.eval('&shiftwidth')
    indent = int(int(spaces) / int(shiftwidth))

    anonomous_snippet = snip.buffer[
        snip.snippet_start[0] : snip.snippet_end[0]
    ]
    anonomous_snippet = '\n'.join(anonomous_snippet).strip()

    snip.buffer[start_line:end_line] = ''

    anonomous_snippet = anonomous_snippet.splitlines()
    for i in range(len(anonomous_snippet)):
        anonomous_snippet[i] = indent * '\t' + anonomous_snippet[i]
    anonomous_snippet = '\n'.join(anonomous_snippet)

    snip.expand_anon(anonomous_snippet)
