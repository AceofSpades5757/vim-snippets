import linecache
import re

import vim  # noqa


def get_all_snippet_info() -> list[dict]:

    vim.command('call UltiSnips#SnippetsInCurrentScope(1)')
    current_ulti_dict_info = vim.eval('g:current_ulti_dict_info')

    snippets = []
    for name, info in current_ulti_dict_info.items():

        path, line_number = info['location'].rsplit(':', 1)
        description = info['description']

        snippets.append(
            dict(
                name=name,
                path=path,
                line_number=int(line_number),
                description=description,
            )
        )

    return snippets


def get_snippet_contents(snippet_name: str) -> str:

    snippets = get_all_snippet_info()

    snippet_info = None
    for snip in snippets:
        if snip['name'] == snippet_name:
            snippet_info = snip

    if snippet_info is None:
        return ''

    re_startsnippet = re.compile(r'^snippet.*$')
    re_endsnippet = re.compile(r'^\s*endsnippet\s*$')

    snippet_path = snippet_info['path']
    line_number = int(snippet_info['line_number'])

    start_block = line = linecache.getline(
        str(snippet_path), int(line_number)
    ).rstrip('\n')
    line_number += 1
    if not re_startsnippet.match(start_block):
        return ''

    snippet_content = []
    while not re_endsnippet.match(line):

        line = linecache.getline(str(snippet_path), int(line_number)).rstrip(
            '\n'
        )
        snippet_content.append(line)

        line_number += 1

        if re_endsnippet.match(line):
            break

    # remove end_block
    snippet_content.pop()

    return '\n'.join(snippet_content)
