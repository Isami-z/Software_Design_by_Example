from glob_any import Any
from glob_either import Either
from glob_lit import Lit
from glob_match import Matchers
from glob_onemore import OneMore


def test_mathchers():
    lit = Lit("a")
    either = Either(Lit("b"), Lit("c"))
    # any = Any()

    match = Matchers()
    match.add(lit)
    match.add(OneMore("*"))
    match.add(either)

    match.build()

    assert match.match("a**b") is not None


# test_mathchers()
lit = Lit("a")
either = Either(Lit("b"), Lit("c"))
any = Any()

match = Matchers()
match.add(lit)
match.add(any)
match.add(either)

match.build()

assert match.match("a**b") is not None
