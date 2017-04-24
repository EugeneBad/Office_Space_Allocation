import unittest
from .dojo import Dojo


class DojoTest(unittest.TestCase):
    def setUp(self):
        some_dojo = Dojo

    def test_dojo_inherits_from_dict(self):
        self.assertTrue(issubclass(Dojo, dict), msg='The Dojo class should inherit from the dict class')