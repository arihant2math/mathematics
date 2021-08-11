from mathematics.algebra.Imaginary import Imaginary


def test_imaginary_str():
    assert str(Imaginary("3i+1")) == "1+3i"


def test_imaginary_eq():
    assert Imaginary("3i+1") == Imaginary("1+3i")


def test_imaginary_add():
    first = Imaginary("3i+1")
    second = Imaginary("3i+1")
    ans = Imaginary("6i+2")
    assert (first + second) == ans


def test_imaginary_sub():
    first = Imaginary("5i+2")
    second = Imaginary("3i+1")
    ans = Imaginary("2i+1")
    assert (first - second) == ans
