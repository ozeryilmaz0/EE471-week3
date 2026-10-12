"""You Will All Conform -- from Programming for the Puzzled by Srini Devadas.

The input is a line of people whose caps face either forwards ('F') or
backwards ('B'). The program prints the fewest commands needed to make
every cap face the same direction.
"""

from typing import List, Tuple

FORWARD = 'F'
BACKWARD = 'B'
END_SENTINEL = 'END'

# An interval is (start position, end position, cap direction).
Interval = Tuple[int, int, str]

SAMPLE_CAPS_1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
                 'B', 'B', 'F', 'F', 'B', 'F']
SAMPLE_CAPS_2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
                 'B', 'B', 'F', 'F', 'F', 'F']


def find_intervals(caps: List[str]) -> List[Interval]:
    """Split the line into maximal runs of caps facing the same direction.

    Args:
        caps: Cap directions, one per person.

    Returns:
        A list of (start, end, direction) tuples, in order of position.
    """
    padded_caps = caps + [END_SENTINEL]
    intervals = []
    run_start = 0
    for position in range(1, len(padded_caps)):
        if padded_caps[position] != padded_caps[run_start]:
            intervals.append((run_start, position - 1, padded_caps[run_start]))
            run_start = position
    return intervals


def choose_direction_to_flip(intervals: List[Interval]) -> str:
    """Return the direction whose intervals are fewer (BACKWARD on a tie).

    Args:
        intervals: The runs produced by find_intervals.

    Returns:
        FORWARD or BACKWARD, the direction of the intervals to flip.
    """
    forward_count = sum(1 for _, _, direction in intervals
                        if direction == FORWARD)
    backward_count = len(intervals) - forward_count
    return FORWARD if forward_count < backward_count else BACKWARD


def print_flip_command(start: int, end: int) -> None:
    """Tell the people in positions start..end to flip their caps."""
    print('People in positions', start, 'through', end, 'flip your caps!')


def please_conform(caps: List[str]) -> None:
    """Print the fewest flip commands using a two-pass approach.

    The first pass finds all intervals; the second prints commands for
    the intervals of the less common direction.

    Args:
        caps: Cap directions, one per person.
    """
    intervals = find_intervals(caps)
    direction_to_flip = choose_direction_to_flip(intervals)
    for start, end, direction in intervals:
        if direction == direction_to_flip:
            print_flip_command(start, end)


def please_conform_one_pass(caps: List[str]) -> None:
    """Print the flip commands in a single pass over the caps.

    Every interval whose direction differs from the first person's cap
    is flipped. A command is started when such an interval begins and
    finished when it ends.

    Args:
        caps: Cap directions, one per person. Must not be empty.
    """
    first_direction = caps[0]
    padded_caps = caps + [first_direction]
    for position in range(1, len(padded_caps)):
        if padded_caps[position] == padded_caps[position - 1]:
            continue
        if padded_caps[position] != first_direction:
            print('People in positions', position, end='')
        else:
            print(' through', position - 1, 'flip your caps!')


def main() -> None:
    """Run the two-pass algorithm on the first sample line of caps."""
    please_conform(SAMPLE_CAPS_1)


if __name__ == "__main__":
    main()
