from box import Box

from coin import Coin

from die import Die


class Experiment:
    def flip_coin_x_times(self, x):
        # return the probability of head
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x

    def flip_coin_2x_n_times(self, n):
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    def flip_coin_with_pattern_n_times(self, pattern, n, flips, bias=0.5):
        c = Coin(bias)
        experiments = [[c.flip() for f in range(flips)] == pattern for e in range(n)]
        return sum(experiments) / n

    def roll_die_with_pattern_n_times(self, patterns, n, rolls, bias=(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)):
        d = Die(bias)
        experiments = [sum((d.roll() in p for p in patterns)) == len(patterns) for e in range(n)]
        return sum(experiments) / n

    def pick_ball_with_pattern_n_times(self, patterns, n, picks, balls):
        b = Box(balls)
        experiments = []
        for _ in range(n):
            b.reset()
            experiments.append(sum((b.pick() == patterns[p] for p in range(picks))) == picks)
        return sum(experiments) / n
