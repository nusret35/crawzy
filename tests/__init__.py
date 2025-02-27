import unittest
import os
from ..crawzy.main import extract


class TestExtractFunction(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_text_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_extract_creates_text_dir(self):
        extract(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))


if __name__ == "__main__":
    unittest.main()
