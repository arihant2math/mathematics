from mathematics.algebra.Imaginary import Imaginary


def test_imaginary_imaginary_part_only():
    assert str(Imaginary("3i")) == "0+3i"


def test_imaginary_real_part_only():
    assert str(Imaginary("5")) == "5+0i"


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


def test_imaginary_mul():
    first = Imaginary("5i+6")
    second = Imaginary("3i+7")
    ans = Imaginary("27+53i")
    assert (first * second) == ans


def test_imaginary_mod():
    first = Imaginary("5i+2")
    second = Imaginary("3i+1")
    ans = Imaginary("2i")
    assert (first % second) == ans
