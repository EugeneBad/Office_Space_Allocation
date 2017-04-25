import unittest
from DOJO import dojo


class DojoTest(unittest.TestCase):
    def setUp(self):
        self.some_dojo = dojo.Dojo()

    def test_dojo_inherits_from_dict(self):
        self.assertTrue(issubclass(dojo.Dojo, dict), msg='The Dojo class should inherit from the dict class')

    def test_dojo_object_is_a_dictionary(self):
        self.assertTrue(isinstance(self.some_dojo, dict), msg='The Dojo class is not creating dictionary objects')

    def test_dojo_object_has_office_spaces_dictionary(self):
        self.assertEqual(type(self.some_dojo['office_spaces']), dict,
                         msg='The Dojo object has no office_spaces dictionary')

    def test_dojo_object_has_living_spaces_dictionary(self):
        self.assertEqual(type(self.some_dojo['living_spaces']), dict,
                         msg='The Dojo object has no living_spaces dictionary')

    def test_dojo_object_has_unallocated_dictionary(self):
        self.assertEqual(type(self.some_dojo['unallocated']), dict,
                         msg='The Dojo object has no living_spaces dictionary')
