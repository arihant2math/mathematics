import number_theory


class TestClass:
    def test_is_prime_edge(self):
        x = number_theory.is_prime(1)
        assert x == False

    def test_is_prime_edge_two(self):
        x = number_theory.is_prime(0)
        assert x == False

    def test_is_prime_edge_three(self):
        x = number_theory.is_prime(-1254)
        assert x == False

    def test_is_prime(self):
        x = number_theory.is_prime(37871)
        assert x == True
