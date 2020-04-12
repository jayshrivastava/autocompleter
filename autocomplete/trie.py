from threading import Lock
from collections import deque
from heapq import heappush, heappop
from typing import List

def idx(c):
        if c == ' ':
            return 26
        return ord(c) - ord('a')
    
def char(i: int):
    if i == 26:
        return ' '
    return chr(i + ord('a'))

class Trie:
    def __init__(self, phrases: List[str], frequencies: List[int]):
        assert len(phrases) == len(frequencies), "Phrases and frequencies must have the same length"
        self.root = self.TrieNode()
        self.mutex = Lock()
        for i in range(len(phrases)):
            self.insert(phrases[i], frequencies[i])

    class TrieNode():
        def __init__(self):
            self.children = [None for _ in range(0, 27)]
            self.n_children = 0
            self.freq = 0
    
    def insert(self, word: str, freq: int = 1):
        self.mutex.acquire()
        traverse = self.root
        for c in word:
            traverse.n_children += 1
            if not traverse.children[idx(c)]:
                traverse.children[idx(c)] = self.TrieNode()
            traverse = traverse.children[idx(c)]
        self.mutex.release()
        traverse.freq += freq

    def exists(self, word: str) -> bool:
        self.mutex.acquire()
        traverse = self.root
        for c in word:
            if not traverse.children[idx(c)]:
                self.mutex.release()
                return False
            traverse = traverse.children[idx(c)]
        self.mutex.release()
        return traverse.freq != 0

    # if a word is deleted concurrently, the 2nd deletion is a noop
    def delete(self, word: str):
        self.mutex.acquire()
        # verify existence
        traverse = self.root
        for c in word:
            if not traverse.children[idx(c)]:
                self.mutex.release()
                return
            traverse = traverse.children[idx(c)]
        
        # delete
        traverse = self.root
        prev = None
        prev_c = None
        for c in word:
            traverse.n_children -= 1
            if traverse.n_children == 0 and prev:
                prev.children[idx(prev_c)] = None
                self.mutex.release()
                return
            prev = traverse
            prev_c = c
            traverse = traverse.children[idx(c)]

        traverse.freq = 0
        self.mutex.release()
        
    def search(self, word: str, n_results: int) -> List[str]:
        self.mutex.acquire()
        # verify existence
        traverse = self.root
        for c in word:
            if not traverse.children[idx(c)]:
                self.mutex.release()
                return []
            traverse = traverse.children[idx(c)]

        q = deque([(traverse, word)])
        results = []
        while(q):
            traverse, word = q.popleft()
            if traverse.freq > 0:
                heappush(results, (traverse.freq, word))
                if len(results) > n_results:
                    heappop(results)
            for i in range(0, 27):
                if traverse.children[i]:
                    q.append((traverse.children[i], word + char(i)))
        self.mutex.release()
        return list(map(lambda result:result[1], sorted(results, key=lambda result:result[0], reverse=True)))
        

