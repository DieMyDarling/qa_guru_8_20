import requests
from allure import step, attach
from allure_commons.types import AttachmentType
from selene.api import *


class TestAddItemsToCart:
    """
    Набор тестов для добавления товаров в корзину.
    """

    product_details = browser.element('td.product')
    shopping_cart = browser.element('#topcartlink')
    unit_price = browser.element('.product-unit-price')
    product_subtotal = browser.element('.product-subtotal')
    order_total = browser.element('.product-price.order-total')

    @staticmethod
    def add_item_to_cart(api_url, data=None):
        """
        Добавление товара в корзину с использованием предоставленного API URL и данных.

        :param api_url: API URL для добавления товара в корзину.
        :param data: Дополнительные данные для отправки с запросом (по умолчанию None).
        """
        with step('Добавление товара в корзину'):
            results = requests.post(url=api_url, data=data)
            cookies = results.cookies.get('Nop.customer')
            attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)
            browser.open('/')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})

    def navigate_to_cart(self):
        """
        Переход в корзину.
        """
        with step('Переход в корзину'):
            self.shopping_cart.should(be.clickable).click()

    def verify_product_details(self, expected_name, expected_unit_price, expected_subtotal, expected_order_total):
        """
        Проверка деталей продукта в корзине.

        :param expected_name: Ожидаемое название продукта.
        :param expected_unit_price: Ожидаемая цена за единицу продукта.
        :param expected_subtotal: Ожидаемая промежуточная сумма продукта.
        :param expected_order_total: Ожидаемая общая сумма заказа после добавления продукта.
        """
        with step('Проверка деталей продукта'):
            self.product_details.should(have.text(expected_name))
            self.unit_price.should(have.text(expected_unit_price))
            self.product_subtotal.should(have.text(expected_subtotal))
            self.order_total.should(have.text(expected_order_total))

    def test_build_pc(self, api_url):
        """
        Тест добавления компьютера в корзину.

        :param api_url: API URL для добавления продукта в корзину.
        """

        self.add_item_to_cart(api_url=f'{api_url}/addproducttocart/details/74/1',
                              data={'product_attribute_74_5_26': '81',
                                    'product_attribute_74_6_27': '83',
                                    'product_attribute_74_3_28': '86',
                                    'addtocart_74.EnteredQuantity': '1'})

        browser.open('/')
        self.navigate_to_cart()

        self.verify_product_details(
            expected_name='Build your own expensive computer',
            expected_unit_price='1815.00',
            expected_subtotal='1815.00',
            expected_order_total='1815.00'
        )

    def test_14_1_inch_laptop(self, api_url):
        """
        Тест добавления "14.1-inch Laptop" в корзину.

        :param api_url: API URL для добавления продукта в корзину.
        """

        self.add_item_to_cart(api_url=f'{api_url}/addproducttocart/catalog/31/1/1')

        browser.open('/')
        self.navigate_to_cart()

        self.verify_product_details(
            expected_name='14.1-inch Laptop',
            expected_unit_price='1590.00',
            expected_subtotal='1590.00',
            expected_order_total='1590.00'
        )

    def test_computing_and_internet_book(self, api_url):
        """
        Тест добавления книги "Computing and Internet" в корзину.

        :param api_url: API URL для добавления продукта в корзину.
        """

        self.add_item_to_cart(api_url=f'{api_url}/addproducttocart/catalog/13/1/1')

        browser.open('/')
        self.navigate_to_cart()

        self.verify_product_details(
            expected_name='Computing and Internet',
            expected_unit_price='10.00',
            expected_subtotal='10.00',
            expected_order_total='10.00'
        )

    def test_digital_camera(self, api_url):
        """
        Тест добавления "Digital SLR Camera - Black" в корзину.

        :param api_url: API URL для добавления продукта в корзину.
        """

        self.add_item_to_cart(api_url=f'{api_url}/addproducttocart/details/18/1')

        browser.open('/')
        self.navigate_to_cart()

        self.verify_product_details(
            expected_name='Digital SLR Camera - Black',
            expected_unit_price='670.00',
            expected_subtotal='670.00',
            expected_order_total='670.00'
        )

    def test_black_and_white_diamond_heart(self, api_url):
        """
        Тест добавления "Black & White Diamond Heart" в корзину.

        :param api_url: API URL для добавления продукта в корзину.
        """

        self.add_item_to_cart(api_url=f'{api_url}/addproducttocart/catalog/14/1/1')

        browser.open('/')
        self.navigate_to_cart()

        self.verify_product_details(
            expected_name='Black & White Diamond Heart',
            expected_unit_price='130.00',
            expected_subtotal='130.00',
            expected_order_total='130.00'
        )
