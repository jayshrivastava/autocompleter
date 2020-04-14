from autocomplete.trie import Trie
from autocomplete.lrucache import LRUCache
from typing import List

class Autocompleter:
    def __init__(self, capacity: int, phrases: List[str], frequencies: List[int]):
        assert capacity >= len(phrases), "Cannot insert more phrases than capacity"
        self.trie = Trie(phrases, frequencies)
        self.cache = LRUCache(capacity, phrases)

    def search(self, phrase: str, results_size: int) -> List[str]:
        return self.trie.search(phrase, results_size)

    def commit(self, phrase: str, freq: int = 1):
        assert phrase != "", "Should not insert an empty string"

        self.trie.insert(phrase, freq)
        removed = self.cache.put(phrase)
        if removed:
            self.trie.delete(removed)
        return removed
         
    