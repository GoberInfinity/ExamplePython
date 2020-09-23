"""
Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.
"""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hv = HashTable.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = HashTable.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                if string in self.table[hv]:
                    return hv
        return -1

    @staticmethod
    def calculate_hash_value(string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0]) * 100) + ord(string[1])


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(HashTable.calculate_hash_value("UDACITY"))

# Test lookup edge case
# Should be -1
print(hash_table.lookup("UDACITY"))

# Test store
hash_table.store("UDACITY")
# Should be 8568
print(hash_table.lookup("UDACITY"))

# Test store edge case
hash_table.store("UDACIOUS")
# Should be 8568
print(hash_table.lookup("UDACIOUS"))
