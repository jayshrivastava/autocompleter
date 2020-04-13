from autocomplete.trie import Trie
from typing import List

class Autocompleter:
    def __init__(self, capacity: int, phrases: List[str], frequencies: List[int]):
        self.trie = Trie(phrases, frequencies)

    def search(self, phrase: str, results_size: int) -> List[str]:
        return self.trie.search(phrase, results_size)

    def insert(self, phrase: str, freq: int = 1) -> List[str]:
        return self.trie.insert(phrase, freq)
