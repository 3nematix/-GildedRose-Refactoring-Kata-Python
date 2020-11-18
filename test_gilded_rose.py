from gilded_rose import GildedRose
from storage import ItemStorage
import unittest

storage = ItemStorage()

# * Write your tests below *

class GildedRoseTest(unittest.TestCase):
    def test_regular_quality(self):
        items = [storage.add("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # We would fail any test if the value would be not equal...
        self.assertEqual(39, items[0].quality)

    def test_regular_sell_in(self):
        items = [storage.add("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)

    def test_regular_sell_in_passed(self):
        items = [storage.add("bread", 0,  40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_regular_sell_in_negative(self):
        items = [storage.add("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)

    def test_regular_quality_negative(self):
        items = [storage.add("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality(self):
        items = [storage.add("Aged Brie", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_aged_brie_sell_in(self):
        items = [storage.add("Aged Brie", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_quality_exceeded(self):
        items = [storage.add("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_unvariated(self):
        items = [storage.add("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)

    def test_sulfuras_sell_in_unvariated(self):
        items = [storage.add("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_quality(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", 15, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)

    def test_backstage_quality_double_increase(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, items[0].quality)

    def test_backstage_quality_triple_increase(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", 2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(43, items[0].quality)

    def test_backstage_quality_expires(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", -6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_exceeded(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_sell_in(self):
        items = [storage.add(
            "Backstage passes to a TAFKAL80ETC concert", 6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_conjured_quality(self):
        items = [storage.add("Conjured Mana Cake", 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_sell_in(self):
        items = [storage.add("Conjured Mana Cake", 6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
