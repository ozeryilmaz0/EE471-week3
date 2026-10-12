"""Solve the cap-conforming puzzle with minimal flip instructions."""

from __future__ import annotations

Cap = str
Interval = tuple[int, int, Cap]

# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps.
# Output is a set of commands (printed out) to get either all F's or all B's.
# Fewest commands are the goal.

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']


def find_intervals(caps: list[Cap]) -> list[Interval]:
    """Return contiguous runs of identical cap directions."""
    intervals: list[Interval] = []
    start_index = 0
    extended_caps = caps + ['END']

    for index in range(1, len(extended_caps)):
        if extended_caps[start_index] != extended_caps[index]:
            intervals.append((start_index, index - 1, extended_caps[start_index]))
            start_index = index

    return intervals


def choose_flip_direction(intervals: list[Interval]) -> Cap:
    """Select the minority cap direction to minimize the number of flips."""
    forward_count = sum(1 for _, _, direction in intervals if direction == 'F')
    backward_count = sum(1 for _, _, direction in intervals if direction == 'B')
    return 'F' if forward_count < backward_count else 'B'


def pleaseConform(caps: list[Cap]) -> None:
    """Print instructions to flip the minority cap direction in each run."""
    intervals = find_intervals(caps)
    flip_direction = choose_flip_direction(intervals)

    for start, end, direction in intervals:
        if direction == flip_direction:
            print('People in positions', start, 'through', end, 'flip your caps!')


def pleaseConformOnepass(caps: list[Cap]) -> None:
    """Print instructions to flip grouped runs using a single pass."""
    extended_caps = caps + [caps[0]]

    for index in range(1, len(extended_caps)):
        if extended_caps[index] != extended_caps[index - 1]:
            if extended_caps[index] != caps[0]:
                print('People in positions', index, end='')
            else:
                print(' through', index - 1, 'flip your caps!')


def main() -> None:
    """Run the program using the default sample configuration."""
    pleaseConform(cap1)


if __name__ == '__main__':
    main()
