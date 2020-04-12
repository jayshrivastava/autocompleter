import unittest

from autocomplete import Autocompleter

class TestAutocompleter(unittest.TestCase):

    def test_search_results(self):
        capacity = 10000
        phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
        frequencies = [120, 100, 30, 200]
        autocompleter = Autocompleter(capacity, phrases, frequencies)

        self.assertEqual(autocompleter.search('auto', 4), ['autocompletion library', 'autocomplete', 'autocompletion', 'autocompleter'])