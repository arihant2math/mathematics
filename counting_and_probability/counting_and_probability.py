class Probability:
    def __init__(self, desired_outcomes, all_outcomes):
        self.desired_outcomes = desired_outcomes
        self.all_outcomes = all_outcomes

    def value(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return v

    def complement(self):
        v = len(set(self.desired_outcomes)) / len(set(self.all_outcomes))
        return 1 - v


def are_mututally_exclusive(A, B):
    a_intersection_b = (set(A.desired_outcomes)).intersection(set(B.desired_outcomes))
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


def a_and_b_two_tries_independent(A, B):
    return A.value() * B.value()


def a_given_b(a, b, universal_set):
    a_intersection_b = (set(a.desired_outcomes)).intersection(set(b.desired_outcomes))
    prob_a_intersection_b = len(a_intersection_b) / len(universal_set)
    prob_a_given_b = prob_a_intersection_b / b.value()
    return prob_a_given_b


def Bayes_A_given_B(A, B, universal_set):
    prob_b_given_a = a_given_b(B, A, universal_set)
    numerator = prob_b_given_a * A.value()
    val = numerator / B.value()
    return val
