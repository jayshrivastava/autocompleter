import unittest

from autocomplete import Autocompleter

class TestAutocompleter(unittest.TestCase):

    def test_search_results(self):
        capacity = 10
        phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
        frequencies = [120, 100, 30, 200]
        autocompleter = Autocompleter(capacity, phrases, frequencies)

        self.assertEqual(autocompleter.search('auto', 4), ['autocompletion library', 'autocomplete', 'autocompletion', 'autocompleter'])

    def test_search_results(self):
        autocompleter = Autocompleter(10, [], [])
        autocompleter.insert("test")
        self.assertEqual(autocompleter.search('te', 1), ['test'])
        autocompleter.insert("testing", 2)
        self.assertEqual(autocompleter.search('te', 2), ['testing', 'test'])