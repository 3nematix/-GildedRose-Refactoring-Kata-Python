# -*- coding: utf-8 -*-

class ItemStorage(object):

    def add(self, item_name, sell_in, quality):
        if item_name == "Aged Brie":
            return AgedBrie(item_name, sell_in, quality)
        if item_name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item_name, sell_in, quality)
        if item_name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(item_name, sell_in, quality)
        if item_name == "Conjured Mana Cake":
            return Conjured(item_name, sell_in, quality)
        else:
            return Item(item_name, sell_in, quality)


class Item(object):
    def __init__(self, item_name, sell_in, quality):
        self.item_name = str(item_name)
        self.quality = quality
        self.sell_in = sell_in

    def __str__(self):
        return "%s, %s, %s" % (self.item_name, self.sell_in, self.quality)

    def update_quality(self):
        # Now we can easily update the quality of the item
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1


class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1


class Sulfuras(Item):
    def update_quality(self):
        pass


class Conjured(Item):
    def update_quality(self):
        self.quality = (self.quality - 2) if self.quality > 2 else 0
        self.sell_in = self.sell_in - 1


class Backstage(Item):
    def update_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in = self.sell_in - 1
