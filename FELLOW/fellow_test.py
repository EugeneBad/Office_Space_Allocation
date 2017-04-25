import unittest
from PERSON.person import Person
from FELLOW.fellow import Fellow

class FellowTest(unittest.TestCase):

    def setUp(self):
        self.in_fellow = Fellow('Scott', 'Y')
        self.out_fellow = Fellow('Aretha', 'N')

    def test_Fellow_inherits_Person(self):
        self.assertTrue(issubclass(Fellow, Person), msg='Fellow should inherit Person')

    def test_Fellow_type(self):
        self.assertEqual(self.in_fellow.type, 'fellow', msg='Fellow type should be fellow')
        self.assertEqual(self.out_fellow.type, 'fellow', msg='Fellow type should be fellow')

    def test_Fellow_name(self):
        self.assertEqual(self.in_fellow.name, 'Scott', msg='Fellow name is wrong')
        self.assertEqual(self.out_fellow.name, 'Aretha', msg='Fellow name is wrong')

    def test_Fellow_accommodation(self):
        self.assertEqual(self.in_fellow.accomodation, 'Y', msg="Fellow's accommodation status is wrong")
        self.assertEqual(self.out_fellow.accomodation, 'N', msg="Fellow's accommodation status is wrong")
