#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
        self.assertRaises(TypeError, Base, 1, 2)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
