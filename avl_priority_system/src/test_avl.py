import unittest
from src.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.root = None

    def test_insert(self):
        self.root = self.tree.insert(self.root, 10, 1)
        self.assertEqual(self.root.key, 10)

        self.root = self.tree.insert(self.root, 20, 2)
        self.root = self.tree.insert(self.root, 5, 3)

        self.assertEqual(self.root.key, 10)
        self.assertEqual(self.root.right.key, 20)
        self.assertEqual(self.root.left.key, 5)

if __name__ == '__main__':
    unittest.main()
