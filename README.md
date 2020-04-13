# lru-autocompleter

A thread-safe autocompletion library backed by a LRU cache.

## Usage

See example.py 

### Searching and Inserting
```python3
from autocomplete import Autocompleter

capacity = 10000
phrases = ['autocomplete', 'autocompletion', 'autocompleter', 'autocompletion library']
frequencies = [120, 100, 30, 200]
autocompleter = Autocompleter(capacity, phrases, frequencies)

autocompleter.search('auto', 4)
#  ['autocompletion library', 'autocomplete', 'autocompletion', 'autocompleter']

autocompleter.insert("autocomplete", 2)
autocompleter.search('auto', 4)
#  ['autocomplete', 'autocompletion library', 'autocompletion', 'autocompleter']
```

## Contributing

PRs, Bug Reports, Feature Requests are welcome via Github. 
`python3 -m unittest` must pass

## Authors

Jayant Shrivastava  
[Email](jshrivastava03@gmail.com) [Github](https://www.github.com/jayshrivastava)

## License

This project is open sourced under the [MIT License](LICENSE.md)