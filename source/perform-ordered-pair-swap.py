from typing import Any
from typing import Tuple

# TODO: Repair all of the program defects near the TODO markers in the following source code


def ordered_pair_swap(pair_one: Tuple[Any, Any], pair_two: Tuple[Any, Any]) -> Tuple[Tuple[Any, Any], Tuple[Any, Any]]:
    """Swap the contents of one ordered pair with another ordered pair."""
    # TODO: create the first tuple so that it contains the swapped contents of the second tuple
    swapped_one = (pair_two[0], pair_two[1])
    # TODO: create the second tuple so that it contains the swapped contents of the first tuple
    swapped_two = (pair_one[0], pair_one[1])
    # TODO: return the two tuples in the opposite order in which they were input
    return (swapped_two, swapped_one)


# create the two ordered pairs
first_ordered_pair = ("A", 1)
second_ordered_pair = ("B", 2)

# display the original tuple of ordered pairs
not_swapped_ordered_pairs = (first_ordered_pair, second_ordered_pair)
print(f"Original tuple of ordered pairs: {not_swapped_ordered_pairs}")

# perform the ordered pair swap
first_swapped_ordered_pair = ordered_pair_swap(first_ordered_pair, second_ordered_pair)
print(f"Swapped tuple of ordered pairs: {first_swapped_ordered_pair}")

# TODO: extract the ordered pairs from the returned tuple and display them
second_swapped_ordered_pair = ordered_pair_swap(first_swapped_ordered_pair[0], first_swapped_ordered_pair[1])
print(f"Swapped (again) tuple of ordered pairs: {second_swapped_ordered_pair}")
