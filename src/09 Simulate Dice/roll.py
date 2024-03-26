from random import randint  # for simulating the rice roll
from collections import Counter  # Keep track of how often each outcome occurs

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        # roll each dice of x sides
        # sum the outcomes and add 1 to the respective counts index
        counts[sum((randint(1, sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) + 1):
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')

roll_dice(4, 6, 6)
