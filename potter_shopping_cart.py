# -*- coding: utf-8 -*-

POTTER_VOL_1 = 1

BOOK_PRICE = 100


class Cart(object):

    def __init__(self):
        self._books = {}

    def add_book(self, book_id):
        self._books[book_id] = self._books.get(book_id, 0) + 1

    def get_price(self):
        return BOOK_PRICE * sum(self._books.itervalues(), 0)
