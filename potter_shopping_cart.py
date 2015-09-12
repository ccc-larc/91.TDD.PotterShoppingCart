# -*- coding: utf-8 -*-

POTTER_VOL_1 = 1
POTTER_VOL_2 = 2
POTTER_VOL_3 = 3
POTTER_VOL_4 = 4
POTTER_VOL_5 = 5

BOOK_PRICE = 100


class Cart(object):

    def __init__(self):
        self._books = {}

    def add_book(self, book_id):
        self._books[book_id] = self._books.get(book_id, 0) + 1

    def get_price(self):
        book_count = sum(self._books.itervalues(), 0)
        discount = _get_bookset_discount(set(self._books))
        return BOOK_PRICE * book_count * discount


def _get_bookset_discount(bookset):
    assert isinstance(bookset, set)

    book_count = len(bookset)

    if book_count == 2:  # 兩本套書
        return 0.95
    elif book_count == 3:  # 三本套書
        return 0.9
    elif book_count == 4:  # 四本套書
        return 0.8
    elif book_count == 5:  # 五本套書
        return 0.75
    else:  # 非套書
        return 1.0
