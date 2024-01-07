import unittest

from devbg2024.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)


if __name__ == '__main__':
    unittest.main()