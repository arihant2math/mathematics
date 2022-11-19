from mathematics.algebra.term import Term
from mathematics.algebra.variable import Variable


def test_eq():
    t1 = Term([Variable("x")], 4)
    t2 = Term([Variable("x")], 4)
    t3 = Term([Variable("x"), Variable("y")], 4)
    t4 = Term([Variable("y"), Variable("x")], 4)
    assert t1 == t2
    assert t1 != t3
    assert t3 == t4


def test_multiply():
    t = Term([Variable("x")], 4)
    assert t * 4 == Term([Variable("x")], 16)
