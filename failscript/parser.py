# from pprint import pprint

import sys
from pathlib import Path

import lark

with open('failscript.lark', 'r', encoding='utf-8') as f:
    grammar = lark.Lark(f, start="start", debug=True, regex=True)

    script: str = (
        'print "please supply a script file name on the command line";'
    )

    args = [script] if len(sys.argv) < 2 else sys.argv[1:]

    for s in args:
        fn: str = ''
        d: str = ''
        if Path(s).exists():
            fn += s
            with open(s, 'r', encoding='utf-8') as g:
                d += g.read()
        else:
            d += s
        tree = grammar.parse(d)
        if fn:
            print("\n")
            print(fn, end="\n--\n")
        print(tree.pretty())
