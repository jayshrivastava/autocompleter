import unittest

from autocomplete import Autocompleter

class c(unittest.TestCase):

    def test_constructor_throws_insufficient_capacity(self):
        self.assertRaises(AssertionError, Autocompleter, 0, ['test'], [1])
    
    def test_constructor_throws_length_mismatch(self):
        self.assertRaises(AssertionError, Autocompleter, 0, ['test'], [1, 2])

    def test_search_results(self):
        capacity = 10
        phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
        frequencies = [120, 100, 30, 200]
        autocompleter = Autocompleter(capacity, phrases, frequencies)

        self.assertEqual(autocompleter.search('auto', 4), ['autocompletion library', 'autocomplete', 'autocompletion', 'autocompleter'])
        self.assertEqual(autocompleter.search('', 1), ['autocompletion library'])

    def test_search_results(self):
        autocompleter = Autocompleter(10, [], [])
        autocompleter.commit("test")
        self.assertEqual(autocompleter.search('te', 1), ['test'])
        autocompleter.commit("testing", 2)
        self.assertEqual(autocompleter.search('te', 2), ['testing', 'test'])

    def test_lru_eviction(self):
        capacity = 4
        phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
        frequencies = [1, 2, 3, 4]
        autocompleter = Autocompleter(capacity, phrases, frequencies)
        self.assertEqual(autocompleter.commit("test"), 'autocomplete') # returns the lru value
        self.assertEqual(autocompleter.commit("testing", 2), 'autocompletion') # returns the lru value
        
        self.assertEqual(autocompleter.search('', 4), ['autocompletion library', 'autocompleter', 'testing', 'test'])
