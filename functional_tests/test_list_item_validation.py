from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list(self):
        self.fail("write me!")