import vim  # noqa


def expand(snip, jump_pos=1):
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
