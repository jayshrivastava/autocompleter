from autocomplete import Autocompleter

capacity = 10000
phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
frequencies = [120, 100, 30, 121]
autocompleter = Autocompleter(capacity, phrases, frequencies)

print(autocompleter.search('auto', 4))

autocompleter.insert("autocomplete", 2)
print(autocompleter.search('auto', 4))
