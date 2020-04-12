import unittest

from autocomplete.trie import Trie

class TestTrie(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(AssertionError, Trie, ['test'], [1,2])

        trie = Trie(['test'], [1])
        self.assertTrue(trie.exists('test'))

    def test_insertion_and_existance(self):
        trie = Trie(['test'], [1])
        trie.insert('testing')
        self.assertTrue(trie.exists('testing'))

    def test_no_existance(self):
        trie = Trie(['test'], [1])
        self.assertFalse(trie.exists('testing'))

    def test_deletion(self):
        trie = Trie(['test', 'testing', 'testing methodology'], [1,3,2])
        trie.delete('testing')
        self.assertFalse(trie.exists('testing'))
        self.assertTrue(trie.exists('test'))
        self.assertTrue(trie.exists('testing methodology'))

    def test_search(self):
        trie = Trie(['test', 'testing', 'testing methodology'], [1,3,2])
        self.assertEqual(trie.search('tes', 3), ['testing', 'testing methodology', 'test'])
        self.assertEqual(trie.search('tes', 2), ['testing', 'testing methodology'])
        self.assertEqual(trie.search('testi', 3), ['testing', 'testing methodology'])

