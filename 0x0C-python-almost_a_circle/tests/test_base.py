#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_base_structure(self):
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertIsNotNone(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_no_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_base_initialize(self):
        self.assertIsNotNone(Base())
        self.assertIsNotNone(Base(5))

    def test_base_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base().id, 2)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)
