# -*- coding: utf-8 -*-
from copy import deepcopy

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
        booksets = BookSet.group_books_to_set(self._books)

        price = 0
        for bookset in booksets:
            book_count = bookset.get_book_count()
            discount = _get_bookset_discount(bookset)
            price += BOOK_PRICE * book_count * discount
        return price


class BookSet(object):

    def __init__(self, books):
        assert iter(books)
        self._bookset = set(books)

    def __eq__(self, other):
        if not isinstance(other, BookSet):
            return False
        return self._bookset == set(other.iter_book_id())

    def get_book_count(self):
        return len(self._bookset)

    def iter_book_id(self):
        for book_id in self._bookset:
            yield book_id

    @staticmethod
    def group_books_to_set(books):
        books = deepcopy(books)

        booksets = []
        while sum(books.itervalues(), 0):
            bookset = BookSet(books)
            booksets.append(bookset)
            for book_id in bookset.iter_book_id():
                books[book_id] -= 1
                if books[book_id] == 0:
                    del books[book_id]

        return booksets


def _get_bookset_discount(bookset):
    assert isinstance(bookset, BookSet)

    book_count = bookset.get_book_count()

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
