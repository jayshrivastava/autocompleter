from autocomplete import Autocompleter

capacity = 10000
phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
frequencies = [120, 100, 30, 200]
autocompleter = Autocompleter(capacity, phrases, frequencies)

print(autocompleter.search('auto', 4))