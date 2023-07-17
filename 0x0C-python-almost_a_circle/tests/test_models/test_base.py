"""Unittest for  `Base` class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """Handling  `Base` class test cases"""
    def test_with_no_arguments(self):
        """Tests with no argument passed to object"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_argument(self):
        """Test with one object created but with the argument"""
        Base._Base__nb_objects = 0
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_multiple_obj_with_arg_last(self):
        """Test with multiple objects with the one with
        the argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_and_without_argument(self):
        """Test with multiple objects with the object with argument
        and one without the  argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_with_multiple_with_arg_and_one_last_without(self):
        """Tests for multiple object with the arguments then one last
        doesn't have any argument"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_with_multiple_obje_with_arg(self):
        """Test with multiple objects both with the arguments"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_for_private_attribute(self):
        """Check if the attribute exists in an object"""
        self.assertFalse(hasattr(Base, '__nb_objects'))


    def test_save_to_file_Rectangle_none(self):
        """Test saving to the file with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_save_to_file_Rectangle(self):
        """Tests saving of json representation of the  objects to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(r2.to_dictionary(), my_list[1])

    def test_save_to_file_Rectangle_empty_list(self):
        """Test saving to the file with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_save_to_file_Square(self):
        """Tests saving of json representation of the objects to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        s2 = Square(2)
        Square.save_to_file([r1, s2])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(s2.to_dictionary(), my_list[1])

    def test_save_to_file_rectangle_only(self):
        """Tests saving of json representation of the objects to file
        for `Rectangle` only"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])

    def test_save_to_file_Square_only_square(self):
        """Test saving to the  file with only `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(s1.to_dictionary(), my_list[0])

    def test_save_to_file_Square_none(self):
        """Test saving to the file with none"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_create_Rectangle(self):
        """Testing creating of the new `Rectangle` instance"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertDictEqual(r1_dictionary, r2.to_dictionary())

    def test_create_Square(self):
        """Testing creating of the  new `Square` instance"""
        Base._Base__nb_objects = 0
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertDictEqual(s1_dictionary, s2.to_dictionary())

    def test_save_to_file_Square_only_square(self):
        """Test saving to the  file with only `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(s1.to_dictionary(), my_list[0])

    def test_load_from_file_rectangle(self):
        """Test loading from file for the `Rectangle`"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_input[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_input[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
