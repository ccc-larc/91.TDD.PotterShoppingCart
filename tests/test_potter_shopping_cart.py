# -*- coding: utf-8 -*-
import unittest
from potter_shopping_cart import Cart, POTTER_VOL_1, POTTER_VOL_2, POTTER_VOL_3, POTTER_VOL_4, POTTER_VOL_5, BookSet


class PotterShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_v1x1_should_price_100(self):
        """
        Scenario: 第一集買了一本，其他都沒買，價格應為 100 * 1 = 100 元
            Given 第一集買了 1 本
            And 第二集買了 0 本
            And 第三集買了 0 本
            And 第四集買了 0 本
            And 第五集買了 0 本
            When 結帳
            Then 價格應為 100 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)

        # assert
        expected = 100
        self.assertEqual(self.cart.get_price(), expected)

    def test_v1x1_v2x1_should_price_190(self):
        """
        Scenario: 第一集買了一本，第二集也買了一本，價格應為100*2*0.95=190
            Given 第一集買了 1 本
            And 第二集買了 1 本
            And 第三集買了 0 本
            And 第四集買了 0 本
            And 第五集買了 0 本
            When 結帳
            Then 價格應為 190 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)
        self.cart.add_book(POTTER_VOL_2)

        # assert
        expected = 190
        self.assertEqual(self.cart.get_price(), expected)

    def test_v1x1_v2x1_v3x1_should_price_270(self):
        """
        Scenario: 一二三集各買了一本，價格應為100*3*0.9=270
            Given 第一集買了 1 本
            And 第二集買了 1 本
            And 第三集買了 1 本
            And 第四集買了 0 本
            And 第五集買了 0 本
            When 結帳
            Then 價格應為 270 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)
        self.cart.add_book(POTTER_VOL_2)
        self.cart.add_book(POTTER_VOL_3)

        # assert
        expected = 270
        self.assertEqual(self.cart.get_price(), expected)

    def test_v1x1_v2x1_v3x1_v4x1_should_price_320(self):
        """
        Scenario: 一二三四集各買了一本，價格應為100*4*0.8=320
            Given 第一集買了 1 本
            And 第二集買了 1 本
            And 第三集買了 1 本
            And 第四集買了 1 本
            And 第五集買了 0 本
            When 結帳
            Then 價格應為 320 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)
        self.cart.add_book(POTTER_VOL_2)
        self.cart.add_book(POTTER_VOL_3)
        self.cart.add_book(POTTER_VOL_4)

        # assert
        expected = 320
        self.assertEqual(self.cart.get_price(), expected)

    def test_v1x1_v2x1_v3x1_v4x1_v5x1_should_price_375(self):
        """
        Scenario: 一次買了整套，一二三四五集各買了一本，價格應為100*5*0.75=375
            Given 第一集買了 1 本
            And 第二集買了 1 本
            And 第三集買了 1 本
            And 第四集買了 1 本
            And 第五集買了 1 本
            When 結帳
            Then 價格應為 375 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)
        self.cart.add_book(POTTER_VOL_2)
        self.cart.add_book(POTTER_VOL_3)
        self.cart.add_book(POTTER_VOL_4)
        self.cart.add_book(POTTER_VOL_5)

        # assert
        expected = 375
        self.assertEqual(self.cart.get_price(), expected)

    def test_v1x1_v2x1_v3x2_should_price_370(self):
        """
        Scenario: 一二集各買了一本，第三集買了兩本，價格應為100*3*0.9 + 100 = 370
            Given 第一集買了 1 本
            And 第二集買了 1 本
            And 第三集買了 2 本
            And 第四集買了 0 本
            And 第五集買了 0 本
            When 結帳
            Then 價格應為 370 元
        """
        # act
        self.cart.add_book(POTTER_VOL_1)
        self.cart.add_book(POTTER_VOL_2)
        self.cart.add_book(POTTER_VOL_3)
        self.cart.add_book(POTTER_VOL_3)

        # assert
        expected = 370
        self.assertEqual(self.cart.get_price(), expected)


class BookSetTest(unittest.TestCase):

    def test_group_books_to_set_1book(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1}),
        ]
        self.assertListEqual(booksets, expected)

    def test_group_books_to_set_2books(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
            POTTER_VOL_2: 1,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1, POTTER_VOL_2}),
        ]
        self.assertListEqual(booksets, expected)

    def test_group_books_to_set_3books(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
            POTTER_VOL_2: 1,
            POTTER_VOL_3: 1,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1, POTTER_VOL_2, POTTER_VOL_3}),
        ]
        self.assertListEqual(booksets, expected)

    def test_group_books_to_set_4books(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
            POTTER_VOL_2: 1,
            POTTER_VOL_3: 1,
            POTTER_VOL_4: 1,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1, POTTER_VOL_2, POTTER_VOL_3, POTTER_VOL_4}),
        ]
        self.assertListEqual(booksets, expected)

    def test_group_books_to_set_5books(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
            POTTER_VOL_2: 1,
            POTTER_VOL_3: 1,
            POTTER_VOL_4: 1,
            POTTER_VOL_5: 1,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1, POTTER_VOL_2, POTTER_VOL_3, POTTER_VOL_4, POTTER_VOL_5}),
        ]
        self.assertListEqual(booksets, expected)

    def test_group_books_to_set_3books_and_1book(self):
        # arrange
        books = {
            POTTER_VOL_1: 1,
            POTTER_VOL_2: 1,
            POTTER_VOL_3: 2,
        }

        # act
        booksets = BookSet.group_books_to_set(books)

        # assert
        expected = [
            BookSet({POTTER_VOL_1, POTTER_VOL_2, POTTER_VOL_3}),
            BookSet({POTTER_VOL_3}),
        ]
        self.assertListEqual(booksets, expected)


if __name__ == '__main__':
    unittest.main()
