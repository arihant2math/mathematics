from mathematics.algebra.Number import Number


def test_eq_true():
    assert Number(5) == Number(5)


def test_eq_false():
    assert not (Number(5) == Number(7))


def test_add():
    assert Number(5) + Number(2) == Number(7)


def test_sub():
    assert Number(10) - Number(3) == Number(7)


def test_mul():
    assert Number(10) * Number(3) == 30


def test_div():
    assert Number(30) / Number(3) == Number(10)


def test_pow():
    assert Number(3) ** Number(4) == 81


def test_or():
    assert Number(3) or Number(5)


def test_digit_sum():
    assert (Number(5235)).digit_sum() == Number(15)


def test_digit_product():
    assert (Number(5215)).digit_product() == Number(50)
