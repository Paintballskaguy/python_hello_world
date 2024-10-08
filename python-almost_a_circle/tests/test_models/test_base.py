import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_auto_assign_id(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_assign_custom_id(self):
        """Test custom ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None input."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        """Test to_json_string with valid dictionary."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None input."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with valid JSON string."""
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{"id": 89}])

if __name__ == '__main__':
    unittest.main()
