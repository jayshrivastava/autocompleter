# lru-autocompleter

A thread-safe text autocompletion library. 

It suggests phrases by frequency and best match, and evicts stale phrases via an LRU scheme.

## Usage

Strings must be sanitized prior to insertion (alphabetical characters including spacing)

`commit(phrase: str, frequency: int) -> None or str`  
If the phrase is cached, it is refreshed in the LRU cache. If it does not exist, it is inserted. Upon insertion, if the cache is at capacity, it will evict and return the least recently used phrase; otherwise, it will return `None`. 
The frequency of the inserted will be incremented as well. Search results are sorted by this frequency.

`search(phrase: str, m: int) -> List[str]`  
Searches the cache for phrases matching the input phrase. Will return the top `n` cached phrases sorted by frequency (sort is not stable). Will not commit the input phrase. You must call `commit` to cache a search value.

### Searching By Frequency
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

### LRU Caching
```python3
from autocomplete import Autocompleter

capacity = 2
phrases = ['autocomplete', 'autocompletion']
frequencies = [1,2]
autocompleter = Autocompleter(capacity, phrases, frequencies)

evicted = autocompleter.commit("autocompletion library", 3)
#  'autocomplete'
autocompleter.search('', 2)
#  ['autocompletion library', 'autocompletion']

autocompleter.commit('autocompletion library', 1)
# None
autocompleter.commit('auto', 20)
# 'autocompletion'

```


## Contributing

PRs, Bug Reports, Feature Requests are welcome via Github. 
`python3 -m unittest` must pass

## Authors

Jayant Shrivastava  
[Email](jshrivastava03@gmail.com) [Github](https://www.github.com/jayshrivastava)

## License

This project is open sourced under the [MIT License](LICENSE.md)