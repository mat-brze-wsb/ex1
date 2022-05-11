from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
import unittest


class TestFormater(unittest.TestCase):

    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_text_lower_case(self):
        low = plain_text_lower_case("MESSAGE", "NAME")
        name = low.split(" ")[0]
        msg = low.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())


