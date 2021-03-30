#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
from io import StringIO
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re
import inspect
import console
import pep8
import os


class TestBaseDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestConsole(unittest.TestCase):
    """Tests for the console"""
    classes = {"Amenity": Amenity, "City": City, "BaseModel": BaseModel,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def test_create_simple(self):
        """Test create command"""
        cmd1 = 'create State name="California"'
        cmd2 = 'create State name="California" age=9 name=yolo'
        commands = [cmd1, cmd2]
        ids = []
        for cmd in commands:
            ID = ''
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(cmd)
                ID = str(f.getvalue())
            ids.append(ID[:-1])
        key = "State." + ids[0]
        dict = storage.all()[key]
        self.assertTrue('name' in dict.__dict__)
