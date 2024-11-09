import random


class RandomizedSet:

    def __init__(self):
        self.value_to_index = {}  # Dictionary to store the value to index mapping
        self.values_list = []  # List to store the values for O(1) access

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False  # Value already exists, insertion fails
        else:
            # Insert value and store its index
            self.value_to_index[val] = len(self.values_list)
            self.values_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False  # Value does not exist, removal fails
        # Get index of the element to be removed
        index_to_remove = self.value_to_index[val]
        # Swap the last element with the element to remove (to maintain O(1) removal)
        last_element = self.values_list[-1]
        self.values_list[index_to_remove] = last_element
        self.value_to_index[last_element] = index_to_remove
        # Remove the last element from the list and dictionary
        self.values_list.pop()
        del self.value_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values_list)
