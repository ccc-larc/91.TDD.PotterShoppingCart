# -*- coding: utf-8 -*-
import unittest
from potter_shopping_cart import Cart, POTTER_VOL_1


class PotterShoppingCartTest(unittest.TestCase):

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
        # arrange
        cart = Cart()

        # act
        cart.add_book(POTTER_VOL_1)

        # assert
        expected = 100
        self.assertEqual(cart.get_price(), expected)


if __name__ == '__main__':
    unittest.main()
