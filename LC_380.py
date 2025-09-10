# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
from typing import Dict, List

class RandomizedSet:
    def __init__(self):
        # list to store the values for O(1) random access
        self.arr: List[int] = []
        # dict mapping value -> index in self.arr for O(1) lookup/removal
        self.pos: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        # If value already exists, return False
        if val in self.pos:
            return False
        # Append value to the end of the array
        self.pos[val] = len(self.arr)      # record index for val
        self.arr.append(val)               # add to array
        return True

    def remove(self, val: int) -> bool:
        # If value does not exist, return False
        if val not in self.pos:
            return False
        # Get index of the value to remove
        idx = self.pos[val]
        # Get the last element in the array
        last_val = self.arr[-1]
        # Move last element into the 'idx' position (if not already last)
        self.arr[idx] = last_val
        self.pos[last_val] = idx
        # Pop the last element (which is now duplicated at idx)
        self.arr.pop()
        # Delete the mapping for removed value
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # Return a uniformly random element from the array
        return random.choice(self.arr)


# CoderPad/HackerRank Test
import random
from typing import Dict, List, Optional

class RandomizedSet:
    def __init__(self) -> None:
        # Stores current values to enable O(1) random access
        self.arr: List[int] = []
        # Maps value -> index in arr for O(1) membership and removal
        self.pos: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        # Prevent duplicates
        if val in self.pos:
            return False
        # Append and record its index
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Fast fail when not present
        if val not in self.pos:
            return False
        # Index of the target value
        idx: int = self.pos[val]
        # Last element in the array
        last_val: int = self.arr[-1]
        # Swap last element into idx position to keep removal O(1)
        self.arr[idx] = last_val
        self.pos[last_val] = idx
        # Remove last slot
        self.arr.pop()
        # Drop mapping for removed value
        del self.pos[val]
        return True

    def getRandom(self) -> Optional[int]:
        # Edge case: empty set -> return None (safer for live pads)
        if not self.arr:
            return None
        # Uniformly choose one index
        rand_index: int = random.randint(0, len(self.arr) - 1)
        return self.arr[rand_index]

# --- Minimal I/O harness for quick manual testing in CoderPad/HackerRank ---
if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))   # True
    print(rs.remove(2))   # False
    print(rs.insert(2))   # True
    print(rs.getRandom() is not None)  # True (likely 1 or 2)
    print(rs.remove(1))   # True
    print(rs.insert(2))   # False (already exists)
    print(rs.getRandom()) # 2 or None if empty (here it's 2)