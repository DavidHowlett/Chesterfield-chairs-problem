import functools
import sys

chairs = 90
days = 450
sys.setrecursionlimit(3000)


@functools.lru_cache(maxsize=days + chairs)
def prob(chairs_sat_on, day):
    if chairs_sat_on == 0 and day == 0:
        # I know that on the first day no chairs will have been sat on
        return 1
    if chairs_sat_on < 0:
        # you can't sit on a negative number of chairs
        return 0
    if day < chairs_sat_on:
        # you can't sit on more chairs then there has been days
        return 0
    return (
        prob(chairs_sat_on, day - 1) * chairs_sat_on / chairs
        + prob(chairs_sat_on - 1, day - 1) * (1 + chairs - chairs_sat_on) / chairs
    )


print(prob(chairs, days))
