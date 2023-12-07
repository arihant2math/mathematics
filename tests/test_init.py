from mathematics import pi_function as pi, sigma_function as sigma


def test_sigma():
    assert sigma(lambda x: x, range(1, 11)) == 55
    assert sigma(lambda x: x**2, range(1, 11)) == 385


def test_pi():
    assert pi(lambda x: x, range(1, 11)) == 3628800
    assert pi(lambda x: x**2, range(1, 11)) == 13168189440000
