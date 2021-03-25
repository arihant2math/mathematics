class Probability:
    """
    This implements basic probability functions
    """
    def __init__(self, desired_outcomes, all_outcomes):
        self.desired_outcomes = desired_outcomes
        self.all_outcomes = all_outcomes

    def value(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return v

    def complement(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return 1 - v


def are_mutually_exclusive(a, b):
    a_intersection_b = (set(a.desired_outcomes)).intersection(set(b.desired_outcomes))
    if a_intersection_b == 0:
        return True
    else:
        return False


def a_or_b(a, b, universal_set):
    a_intersection_b = (set(a.desired_outcomes)).intersection(set(b.desired_outcomes))
    prob_a_intersection_b = len(a_intersection_b) / len(universal_set)
    a_or_b_ans = a.value() + b.value() - prob_a_intersection_b
    return a_or_b_ans


def a_and_b_single_try_independent(a, b, universal_set):
    a_intersection_b = (set(a.desired_outcomes)).intersection(set(b.desired_outcomes))
    prob_a_intersection_b = len(a_intersection_b) / len(universal_set)
    return prob_a_intersection_b


def a_and_b_two_tries_independent(a, b):
    return a.value() * b.value()


def a_given_b(a, b, universal_set):
    a_intersection_b = (set(a.desired_outcomes)).intersection(set(b.desired_outcomes))
    prob_a_intersection_b = len(a_intersection_b) / len(universal_set)
    prob_a_given_b = prob_a_intersection_b / b.value()
    return prob_a_given_b


def bayes_a_given_b(a, b, universal_set):
    prob_b_given_a = a_given_b(b, a, universal_set)
    numerator = prob_b_given_a * a.value()
    val = numerator / b.value()
    return val
