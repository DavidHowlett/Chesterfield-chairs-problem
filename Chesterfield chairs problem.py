"""
My friend Tom ate lunch in Chesterfield House common room on about 450 lunchtimes.
The room has 90 chairs. Each lunch he randomly selects a chair to sit in.
What is the probably that he has sat in every chair?

Thomas Keeling posed this problem in about 2008. I worked with him on an analytical
solution but we were unable to find one. I came back to the problem years later
after learning python. Below is my solution.
"""

import functools

chairs = 90
days = 450


@functools.lru_cache()
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


# prints 0.5479785390056
print(prob(chairs, days))
