

from sys import stderr

from panflute import *
headers = set()


def duplicated(e, _):
    if not isinstance(e, Header):
        return
    h = stringify(e)

    if h in headers:
        stderr.write("повтор заголовка: " + h + '\n')
    headers.add(h)

def level(e, _):
    if not isinstance(e, Header):
        return
    if   e.level > 2:
        return Header(Str(stringify(e).upper()), level=e.level)

def bold(f):
    f.replace_keyword("BOLD", Strong(Str("BOLD")))

if __name__ == "__main__":
    run_filters([duplicated, level], prepare=bold)