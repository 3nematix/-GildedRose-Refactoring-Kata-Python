# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # Update the quality for each of the items
        for item in self.items:
            item.update_quality()
