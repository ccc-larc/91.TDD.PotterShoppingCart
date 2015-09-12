# -*- coding: utf-8 -*-

POTTER_VOL_1 = 1
POTTER_VOL_2 = 2

BOOK_PRICE = 100


class Cart(object):

    def __init__(self):
        self._books = {}

    def add_book(self, book_id):
        self._books[book_id] = self._books.get(book_id, 0) + 1

    def get_price(self):
        book_count = sum(self._books.itervalues(), 0)
        if book_count == 2:
            discount = 0.95
        else:
            discount = 1.0
        return BOOK_PRICE * book_count * discount
