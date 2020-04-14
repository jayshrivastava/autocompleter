import unittest

from autocomplete.lrucache import LRUCache

class TestLRUCache(unittest.TestCase):

    def test_constructor_throws_zero_capacity(self):
        self.assertRaises(AssertionError, LRUCache, 0, [])

    def test_returns_empty_key_value_when_nothing_is_evicted(self):
        cache = LRUCache(1, [])
        self.assertEqual(cache.put("t1"),(None))

    def test_evicts_stale_key_when_over_capacity(self):
        cache = LRUCache(1, [])
        cache.put("t1")
        self.assertEqual(cache.put("t2"),"t1")

    def test_calling_put_method_refreshes_stale_key(self):
        cache = LRUCache(2, ['t1','t2'])
        cache.put("t1")
        self.assertEqual(cache.put("t3"),"t2")
