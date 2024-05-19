#!/bin/usr/python3

import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_is_unique(self):
        # Create multiple instances of BaseModel and ensure their IDs are unique
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_set(self):
        # Check if created_at is set to the current datetime
        model = BaseModel()
        self.assertIsNotNone(model.created_at)

    def test_updated_at_is_updated(self):
        # Check if updated_at is updated after calling save()
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_contains_expected_keys(self):
        # Check if to_dict() returns a dictionary with the expected keys
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_str_representation(self):
        # Check if __str__() returns the expected string format
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()
