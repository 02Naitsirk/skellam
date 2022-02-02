from scipy.stats import skellam
import matplotlib.pyplot as plt
import numpy as np


def win_probability(points_a, points_b, time_passed, total_time):
    deficit = points_b - points_a
    time_remaining = total_time - time_passed

    rate_a = points_a / time_passed
    rate_b = points_b / time_passed

    expected_points_remaining_a = rate_a * time_remaining
    expected_points_remaining_b = rate_b * time_remaining

    point_difference_rv = skellam(expected_points_remaining_a, expected_points_remaining_b)

    prob_tie = point_difference_rv.pmf(deficit)  # if losing team makes up its deficit exactly
    prob_a_wins = 1 - point_difference_rv.cdf(deficit)
    prob_b_wins = 1 - prob_a_wins - prob_tie

    return [prob_a_wins, prob_b_wins, prob_tie]


points_a = 19
points_b = 20
total_time = 90

print(win_probability(points_a, points_b, total_time / 3, total_time))

fig, ax = plt.subplots(1, 1)

x = np.arange(total_time / 3, total_time, 0.01)
ax.plot(x, win_probability(points_a, points_b, x, total_time)[0], label='team A wins')
ax.plot(x, win_probability(points_a, points_b, x, total_time)[1], label='team B wins')
ax.plot(x, win_probability(points_a, points_b, x, total_time)[2], label='tie')
ax.legend()
plt.ylim([0, 1])
plt.show()
