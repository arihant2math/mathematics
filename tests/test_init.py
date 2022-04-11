from mathematics import pi_function as pi, sigma_function as sigma


def test_sigma():
    assert sigma(lambda x: x, 1, 10) == 55
    assert sigma(lambda x: x**2, 1, 10) == 385


def test_pi():
    assert pi(lambda x: x, 1, 10) == 3628800
    assert pi(lambda x: x**2, 1, 10) == 13168189440000
