import time
import random

def waiting_game():
    target = random.randint(2, 4)
    print(f"\nYour target is: {target} seconds")

    input("\n --- Press Enter to Begin ---")
    start = time.perf_counter() # return a float value of the current time in fractional seconds

    input(f"\n...Press Enter again after {target} seconds...")
    elapsed = time.perf_counter() - start # compare the current time to the earlier time

    print(f"\nElapsed time: {elapsed :.3f} seconds")
    if elapsed == target:
        print('Unbelievable! Perfect timing!')
    elif elapsed < target:
        print(f"{target - slapsed :.3f} seconds too fast")
    else:
        print(f"{elapsed - target :.3f} seconds too slow")

print(waiting_game())