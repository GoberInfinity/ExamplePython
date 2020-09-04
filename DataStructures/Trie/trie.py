# -*- coding: utf-8 -*-
"""
Implementation of a Trie with a dictionaryy
"""

from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = defaultdict()
        self.name = "lo"

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if not current:
            return True
        return False


test = Trie()
test.insert("foo")
test.insert("bar")
test.insert("baz")
test.insert("barz")
test.insert("foo")
print(test.search("foo"))
print(test.root)
