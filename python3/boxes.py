""" Creating universal boxes.

These functions should have originally come from honza/vim-snippets, on
GitHub, but required updating for readability and my own understanding.
"""
import string

import vim  # noqa


def _parse_comments(s):
    """ Parses vim's comments option to extract comment format. """
    i = iter(s.split(","))

    rv = []
    try:
        while True:
            # get the flags and text of a comment part
            flags, text = next(i).split(':', 1)

            if len(flags) == 0:
                rv.append(('OTHER', text, text, text, ""))
            # parse 3-part comment, but ignore those with O flag
            elif 's' in flags and 'O' not in flags:
                ctriple = ["TRIPLE"]
                indent = ""

                if flags[-1] in string.digits:
                    indent = " " * int(flags[-1])
                ctriple.append(text)

                flags, text = next(i).split(':', 1)
                assert flags[0] == 'm'
                ctriple.append(text)

                flags, text = next(i).split(':', 1)
                assert flags[0] == 'e'
                ctriple.append(text)
                ctriple.append(indent)

                rv.append(ctriple)
            elif 'b' in flags:
                if len(text) == 1:
                    rv.insert(0, ("SINGLE_CHAR", text, text, text, ""))
    except StopIteration:
        return rv


def get_comment_format():
    """ Returns a 4-element tuple (first_line, middle_lines, end_line, indent)
    representing the comment format for the current file.

    It first looks at the 'commentstring', if that ends with %s, it uses that.
    Otherwise it parses '&comments' and prefers single character comment
    markers if there are any.
    """
    commentstring = vim.eval("&commentstring")
    if commentstring.endswith("%s"):
        c = commentstring[:-2]
        return (c.rstrip(), c.rstrip(), c.rstrip(), "")
    comments = _parse_comments(vim.eval("&comments"))
    for c in comments:
        if c[0] == "SINGLE_CHAR":
            return c[1:]
    return comments[0][1:]


def make_box(
    text_width, body_width=None, level=1
) -> tuple[str, str, str, str]:

    first_line, middle_lines, end_line, indent = (
        s.strip() for s in get_comment_format()
    )

    middle_lines = middle_lines if not middle_lines else level * middle_lines
    middle_0 = middle_lines[0] if middle_lines else ''
    body_width_inner = (
        body_width - 3 - max(len(first_line), len(indent + end_line))
        if body_width
        else text_width + 2
    )

    starting_line = (
        first_line
        + middle_lines
        + (body_width_inner * middle_0)
        + ((level - 1) * middle_0)
    )
    nspaces = 0
    middle_line_start = (indent + middle_lines + " ") + (" " * nspaces)
    middle_line_end = " " + (" " * 0) + middle_lines
    end_line = (
        indent
        + middle_lines
        + (body_width_inner * middle_0)
        + ((level - 1) * middle_0)
        + end_line
    )

    return starting_line, middle_line_start, middle_line_end, end_line
