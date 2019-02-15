from experiment import Experiment

from pytest import approx


def test_probability_of_a_head():
    e = Experiment()
    p = e.flip_coin_x_times(100_000)
    assert p == approx(0.5, abs=0.01)


def test_probability_of_hh():
    e = Experiment()
    p = e.flip_coin_2x_n_times(100_000)
    assert p == approx(0.25, abs=0.01)


def test_probability_of_ththh():
    e = Experiment()
    p = e.flip_coin_with_pattern_n_times([0, 1, 0, 1, 1], 100_000, 5)
    assert p == approx((0.5)**5, abs=0.01)


def test_probability_of_hhhh():
    e = Experiment()
    p = e.flip_coin_with_pattern_n_times([1, 1, 1, 1], 100_000, 4, 0.3)
    assert p == approx((0.3)**4, abs=0.01)


def test_probability_of_odd_3_4_less_3():
    e = Experiment()
    pattern = [[1, 3, 5], [3], [4], [1, 2]]
    p = e.roll_die_with_pattern_n_times(pattern, 100_000, 4, (0.3, 0.05, 0.05, 0.3, 0.1, 0.2))
    assert p == approx(.45 * .05 * .30 * .35, abs=0.01)


def test_probability_of_odd_rgyrr():
    e = Experiment()
    p = e.pick_ball_with_pattern_n_times('rgyrr', 100_000, 5, ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'y', 'y'])
    assert p == approx(.009, abs=0.01)
