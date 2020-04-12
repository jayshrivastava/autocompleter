from autocomplete.trie import Trie
from typing import List

class Autocompleter:
    def __init__(self, capacity: int, phrases: List[str], frequencies: List[int]):
        self.trie = Trie(phrases, frequencies)

    def search(self, phrase: str, size: int) -> List[str]:
        return self.trie.search(phrase, size)

    