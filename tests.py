"""
Project07
CSE 331 F22 (Onsay)
Bank Premsri
tests.py
"""
import math
import unittest
import types
from math import log2
from solution import Node, AVLTree, is_avl_tree, pretty_print_binary_tree
from xml.dom import minidom

NAMES = {0: 'Aaron', 1: 'Abigail', 2: 'Adam', 3: 'Alan', 4: 'Albert', 5: 'Alexander', 6: 'Alexis', 7: 'Alice',
         8: 'Amanda', 9: 'Amber', 10: 'Amy', 11: 'Andrea', 12: 'Andrew', 13: 'Angela', 14: 'Ann', 15: 'Anna',
         16: 'Anthony', 17: 'Arthur', 18: 'Ashley', 19: 'Austin', 20: 'Barbara', 21: 'Benjamin', 22: 'Betty',
         23: 'Beverly', 24: 'Billy', 25: 'Bobby', 26: 'Brandon', 27: 'Brenda', 28: 'Brian', 29: 'Brittany', 30: 'Bruce',
         31: 'Bryan', 32: 'Carl'}


class AVLTreeTests(unittest.TestCase):

    def test_rotate(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.right_rotate(avl.origin))
        self.assertIsNone(avl.left_rotate(avl.origin))

        """
        (1) test basic right
        initial structure:
            3
           /
          2
         /
        1
        final structure:
          2
         / \
        1   3
        """
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.size = 3

        node = avl.right_rotate(avl.origin)


        self.assertIsInstance(node, Node)
        # root value and parent
        self.assertEqual(2, avl.origin.value)
        self.assertIsNone(avl.origin.parent)
        # root left value and parent
        self.assertTrue(avl.origin.left.value == 1 and avl.origin.left.parent == avl.origin)
        # shouldn't have children
        self.assertFalse(avl.origin.left.left or avl.origin.left.right)
        # root right value and parent
        self.assertTrue(avl.origin.right.value == 3 and avl.origin.right.parent == avl.origin)
        # shouldn't have children
        self.assertFalse(avl.origin.right.right or avl.origin.right.left)

        """
        (2) test basic left
        initial structure:
        1
         \
          2
           \
            3
        final structure:
          2
         / \
        1   3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.size = 3

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertTrue(avl.origin.value == 2 and not avl.origin.parent)  # root value and parent
        # root left value and parent
        self.assertTrue(avl.origin.left.value == 1 and avl.origin.left.parent == avl.origin)
        # shouldn't have any children
        self.assertFalse(avl.origin.left.left or avl.origin.left.right)
        # root right value and parent
        self.assertTrue(avl.origin.right.value == 3 and avl.origin.right.parent == avl.origin)
        # shouldn't have any children
        self.assertFalse(avl.origin.right.right or avl.origin.right.left)

        """
        (3) test intermediate right, rotating at origin
        initial structure:
              7
             / \
            3   10
           / \
          2   4
         /
        1 
        final structure:
            3
           / \
          2   7
         /   / \
        1   4   10
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.left.left = Node(2, parent=avl.origin.left)
        avl.origin.left.left.left = Node(1, parent=avl.origin.left.left)
        avl.origin.left.right = Node(4, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)

        node = avl.right_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node7 = avl.origin.right
        node4 = avl.origin.right.left
        node10 = avl.origin.right.right

        self.assertTrue(node3.value == 3 and not node3.parent)
        self.assertTrue(node2.value == 2 and node2.parent == node3 and not node2.right)
        self.assertTrue(node1.value == 1 and node1.parent == node2 and not (node1.left or node1.right))
        self.assertTrue(node7.value == 7 and node7.parent == node3 and node7.left == node4 and node7.right == node10)
        self.assertTrue(node4.value == 4 and node4.parent == node7 and not (node4.left or node4.right))
        self.assertTrue(node10.value == 10 and node10.parent == node7 and not (node10.left or node10.right))

        """
        (4) test intermediate left, rotating at origin
        initial structure:
          7
         /  \
        3   10
           /   \
          9    11
                 \
                  12
        final structure:
        	10
           /  \
          7   11
         / \    \
        3   9    12
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(9, parent=avl.origin.right)
        avl.origin.right.right = Node(11, parent=avl.origin.right)
        avl.origin.right.right.right = Node(12, parent=avl.origin.right.right)

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node7 = avl.origin.left
        node3 = avl.origin.left.left
        node9 = avl.origin.left.right
        node11 = avl.origin.right
        node12 = avl.origin.right.right

        self.assertTrue(node10.value == 10 and not node10.parent)
        self.assertTrue(node7.value == 7 and node7.parent == node10)
        self.assertTrue(node3.value == 3 and node3.parent == node7 and not (
                node3.left or node3.right))
        self.assertTrue(node9.value == 9 and node9.parent == node7 and not (
                node9.left or node9.right))
        self.assertTrue(node11.value == 11 and node11.parent == node10 and not node11.left)
        self.assertTrue(node12.value == 12 and node12.parent == node11 and not (
                node12.left or node12.right))

        """
        (5) test advanced right, rotating not at origin
        initial structure:
        		10
        	   /  \
        	  5	   11
        	 / \     \
        	3	7    12
           / \
          2   4
         /
        1
        final structure:
              10
             /  \
            3    11
           / \     \
          2   5     12
         /   / \
        1   4   7
        """
        avl = AVLTree()
        avl.origin = Node(10)
        avl.origin.right = Node(11, parent=avl.origin)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.left = Node(5, parent=avl.origin)
        avl.origin.left.right = Node(7, parent=avl.origin.left)
        avl.origin.left.left = Node(3, parent=avl.origin.left)
        avl.origin.left.left.right = Node(4, parent=avl.origin.left.left)
        avl.origin.left.left.left = Node(2, parent=avl.origin.left.left)
        avl.origin.left.left.left.left = Node(
            1, parent=avl.origin.left.left.left)

        node = avl.right_rotate(avl.origin.left)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node11 = avl.origin.right
        node12 = avl.origin.right.right
        node3 = avl.origin.left
        node2 = avl.origin.left.left
        node1 = avl.origin.left.left.left
        node5 = avl.origin.left.right
        node4 = avl.origin.left.right.left
        node7 = avl.origin.left.right.right

        self.assertTrue(node10.value == 10 and not node10.parent)
        self.assertTrue(node3.value == 3 and node3.parent == node10)
        self.assertTrue(node2.value == 2 and node2.parent == node3 and not node2.right)
        self.assertTrue(node1.value == 1 and node1.parent == node2 and not (
                node1.left or node1.right))
        self.assertTrue(node5.value == 5 and node5.parent == node3)
        self.assertTrue(node4.value == 4 and node4.parent == node5 and not (
                node4.left or node4.right))
        self.assertTrue(node7.value == 7 and node7.parent == node5 and not (
                node7.left or node7.right))
        self.assertTrue(node11.value == 11 and node11.parent == node10 and not node11.left)
        self.assertTrue(node12.value == 12 and node12.parent == node11 and not (
                node12.left or node12.right))

        """
        (6) test advanced left, rotating not at origin
        initial structure:
        	3
           / \
          2   10
         /   /  \
        1   5   12
               /  \
              11   13
                     \
                      14
        final structure:
        	3
           / \
          2   12
         /   /  \
        1   10   13
           /  \    \
          5   11   14
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(5, parent=avl.origin.right)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.right.right.left = Node(11, parent=avl.origin.right.right)
        avl.origin.right.right.right = Node(13, parent=avl.origin.right.right)
        avl.origin.right.right.right.right = Node(
            14, parent=avl.origin.right.right.right)

        node = avl.left_rotate(avl.origin.right)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node12 = avl.origin.right
        node10 = avl.origin.right.left
        node5 = avl.origin.right.left.left
        node11 = avl.origin.right.left.right
        node13 = avl.origin.right.right
        node14 = avl.origin.right.right.right

        self.assertTrue(node3.value == 3 and not node3.parent)
        self.assertTrue(node2.value == 2 and node2.parent == node3 and not node2.right)
        self.assertTrue(node1.value == 1 and node1.parent == node2 and not (
                node1.left or node1.right))
        self.assertTrue(node12.value == 12 and node12.parent == node3)
        self.assertTrue(node10.value == 10 and node10.parent == node12)
        self.assertTrue(node5.value == 5 and node5.parent == node10 and not (
                node5.left or node5.right))
        self.assertTrue(node11.value == 11 and node11.parent == node10 and not (
                node11.left or node11.right))
        self.assertTrue(node13.value == 13 and node13.parent == node12 and not node13.left)
        self.assertTrue(node14.value == 14 and node14.parent == node13 and not (
                node14.left or node14.right))

    def test_balance_factor(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertEqual(0, avl.balance_factor(avl.origin))

        """
        (1) test on balanced tree
        structure:
          2
         / \
        1   3
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        self.assertEqual(0, avl.balance_factor(avl.origin))
        self.assertEqual(0, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.right))

        """
        (2) test on unbalanced left
        structure:
            3
           /
          2
         /
        1
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.size = 3

        self.assertEqual(2, avl.balance_factor(avl.origin))
        self.assertEqual(1, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.left.left))

        """
        (2) test on unbalanced right
        structure:
        1
         \
          2
           \
            3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.size = 3

        self.assertEqual(-2, avl.balance_factor(avl.origin))
        self.assertEqual(-1, avl.balance_factor(avl.origin.right))
        self.assertEqual(0, avl.balance_factor(avl.origin.right.right))

    def test_rebalance(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.rebalance(avl.origin))

        """
        (1) test balanced tree (do nothing)
        initial and final structure:
          2
         / \
        1   3
        since pointers are already tested in rotation testcase, only check values and heights
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test left-left rebalance
        initial structure:
            4
           /
          2
         / \
        1   3
        final structure:
          2
         / \
        1   4
           /
          3
        """
        avl = AVLTree()
        avl.origin = Node(4)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(3, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)

        """
        (3) test right-right rebalance
        initial structure:
        1
         \
          3
         /  \
        2    4
        final structure:
          3
         / \
        1   4
         \
          2
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(4, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left = Node(2, parent=avl.origin.right)
        avl.origin.right.left.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (4) test left-right rebalance
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        intermediate structure:
              5
             / \
            3   6
           / \
          2   4
         /
        1
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        avl.origin = Node(5)
        avl.origin.height = 3
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 2
        avl.origin.right = Node(6, parent=avl.origin)
        avl.origin.right.height = 0
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 1
        avl.origin.left.right.right = Node(4, parent=avl.origin.left.right)
        avl.origin.left.right.right.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (5) test right-left rebalance
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        intermediate structure:
          2
         / \
        1   4
           / \
          3   5
               \
                6
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        avl.origin = Node(2)
        avl.origin.height = 3
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(5, parent=avl.origin)
        avl.origin.right.height = 2
        avl.origin.right.left = Node(4, parent=avl.origin.right)
        avl.origin.right.left.height = 1
        avl.origin.right.right = Node(6, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left.left = Node(3, parent=avl.origin.right.left)
        avl.origin.right.left.left.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_insert(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        avl = AVLTree()
        """
        (1) test insertion causing right-right rotation
        final structure
          1
         / \
        0   3
           / \
          2   4
        """
        for i in range(5):
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)

        self.assertEqual(5, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(0, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(2, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(4, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (2) test insertion causing left-left rotation
        final structure
            3
           / \
          1   4
         / \
        0   2
        """
        avl = AVLTree()
        for i in range(4, -1, -1):
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)

        self.assertEqual(5, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (3) test insertion (with duplicates) causing left-right rotation
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3] * 2 + [4]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (4) test insertion (with duplicates) causing right-left rotation
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        for i in [2, 1, 5, 4, 6] * 2 + [3]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_min(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.min(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(0, min_node.value)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(-100, min_node.value)

    def test_max(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.max(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(9, max_node.value)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(100, max_node.value)

    def test_search(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.search(avl.origin, 0))

        """
        (1) search small basic tree
        tree structure
          1
         / \
        0   3
           / \
          2   4
        """
        avl = AVLTree()
        numbers = [1, 0, 3, 2, 4]
        for num in numbers:
            avl.insert(avl.origin, num)
        # search existing numbers
        for num in numbers:
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        # search non-existing numbers and ensure parent of where value would go is returned
        pairs = [(-1, 0), (0.5, 0), (5, 4), (2.5, 2),
                 (3.5, 4), (-1e5, 0), (1e5, 4)]
        for target, closest in pairs:
            node = avl.search(avl.origin, target)
            self.assertIsInstance(node, Node)
            self.assertEqual(closest, node.value)

    def test_inorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.inorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(10))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(-100, 101))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(4) Testing tree is iterable. Hint: Implement the __iter__ function."""
        for expected_val, actual in zip(expected, avl):
            self.assertEqual(expected_val, actual.value)

    def test_preorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.preorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 0, 2, 7, 5, 4, 6, 8, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 21):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, -17, -19, -20, -18, -15, -16, -14, -9, -11,
                    -12, -10, -7, -8, -6, 11, 3, -1, -3, -4, -2, 1, 0, 2,
                    7, 5, 4, 6, 9, 8, 10, 15, 13, 12, 14, 17, 16, 19, 18,
                    20]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_postorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.postorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, 2, 1, 4, 6, 5, 9, 8, 7, 3]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-20, -18, -19, -16, -14, -15, -17, -12, -10, -11, -8, -6, -7, -9,
                    -13, -4, -2, -3, 0, 2, 1, -1, 4, 6, 5, 8, 10, 9, 7, 3, 12, 14, 13,
                    16, 19, 18, 17, 15, 11, -5]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_levelorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.levelorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 7, 0, 2, 5, 8, 4, 6, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, 11, -17, -9, 3, 15, -19, -15, -11, -7, -1, 7, 13, 17, -20, -18,
                    -16, -14, -12, -10, -8, -6, -3, 1, 5, 9, 12, 14, 16, 18, -4, -2, 0, 2,
                    4, 6, 8, 10, 19]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_remove(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.remove(avl.origin, 0))

        """
        (1) test removal causing right-right rotation
        initial structure:
            2
           / \
          1   3
         /     \
        0       4
        final structure (removing 1, 0):
          3 
         / \
        2   4
        """
        avl = AVLTree()
        for i in [2, 1, 3, 4, 0]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 0)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test removal causing left-left rotation
        initial structure:
            3
           / \
          2   4
         /     \
        1       5
        final structure (removing 4, 5):
          2 
         / \
        1   3
        """
        avl = AVLTree()
        for i in [3, 2, 4, 1, 5]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 4)  # one child removal
        avl.remove(avl.origin, 5)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (3) test removal causing left-right rotation
        initial structure:
              5
             / \
            2   6
           / \   \
          1   3   7
         /     \
        0       4
        final structure (removing 1, 6):
            3 
           / \
          2   5
         /   / \
        0   4   7
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3, 7, 0, 4]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 6)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (4) test removal causing right-left rotation
        initial structure:
            2
           / \
          1   5
         /   / \
        0   4   6
           /     \
          3       7
        final structure (removing 6, 1):
            4 
           / \
          2   5
         / \   \
        0   3   7
        """
        avl = AVLTree()
        for i in [2, 1, 5, 0, 4, 6, 3, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 6)  # one child removal
        avl.remove(avl.origin, 1)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (5) test simple 2-child removal
        initial structure:
          2
         / \
        1   3
        final structure (removing 2):
         1 
          \
           3
        """
        avl = AVLTree()
        for i in [2, 1, 3]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (5) test compounded 2-child removal
        initial structure:
              4
           /     \
          2       6
         / \     / \
        1   3   5   7
        intermediate structure (removing 2, 6):
            4
           / \
          1   5
           \   \
            3   7
        final structure (removing 4)
            3
           / \
          1   5
               \
                7        
        """
        avl = AVLTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        avl.remove(avl.origin, 6)  # two child removal
        avl.remove(avl.origin, 4)  # two child removal
        self.assertEqual(4, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_is_avl_tree_basic(self):

        def create_tree(tree, height, start_value=None):
            """
            Create full binary tree with some value of same height as provided
            """
            start_value = start_value if start_value else 2 ** height
            tree.origin = Node((start_value, 2 ** (height - 1)))
            tree.origin.height = height
            num = 2 ** (height + 1) - 1
            x = 1
            q = [tree.origin]

            while x < num:
                node = q.pop(0)
                real_value, diff = node.value
                current_height = node.height
                node.value = real_value
                node.right = Node((node.value + diff, diff // 2))
                node.right.height = current_height - 1
                node.left = Node((node.value - diff, diff // 2))
                node.left.height = current_height - 1
                q.extend([node.left, node.right])
                x += 2
            # Assign the value to only just value
            for node in q:
                node.value = node.value[0]

        """
        (1) Example 1 balance tree
                   6
                 /   \
                4     8
               / \   / \  
              3   5 7    9
        """
        a = AVLTree()
        create_tree(a, 2, 6)
        a.origin.height = 3
        self.assertTrue(is_avl_tree(a))  # 1

        """
        (2) Example 2, one side tree
                 10
                   \
                    20
                     \
                      30
                       \
                        40  
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 3

        a.origin.right = Node(20)
        a.origin.right.right = Node(30)
        a.origin.right.right.right = Node(40)
        self.assertFalse(is_avl_tree(a))  # 1

        """
        (3) Example 3
                   10
                 /    \
                4      15
               / \    /  \  
              3   12 13  20
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 2

        a.origin.left = Node(5)
        a.origin.left.height = 1
        a.origin.left.right = Node(12)
        a.origin.left.left = Node(1)

        a.origin.right = Node(15)
        a.origin.right.height = 1
        a.origin.right.left = Node(13)
        a.origin.right.right = Node(20)
        self.assertFalse(is_avl_tree(a))  # 1

        """
        (4) Test Imbalance Subtree
        Tree after inserting all nodes
                    2
                   / \
                  1   8
                 /
                0 
        """
        a = AVLTree()
        self.assertTrue(is_avl_tree(a))  # 1

        a.origin = Node(2)
        a.origin.height = 0
        self.assertTrue(is_avl_tree(a))  # 2

        a.origin.height = 1
        a.origin.left = Node(1)
        self.assertTrue(is_avl_tree(a))  # 3

        a.origin.height = 2
        a.origin.left.height = 1
        a.origin.left.left = Node(0)

        self.assertFalse(is_avl_tree(a))  # 4 Tree is imbalance here

        a.origin.right = Node(8)
        self.assertTrue(is_avl_tree(a))  # 5

        """
        (5)
        False at Node(7) since 7 < 5 but it is in the left subtree of 5
        
                  10
                 / \
                5   12
               /     
              7      
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 2
        a.origin.left = Node(5)
        a.origin.left.height = 1
        a.origin.right = Node(12)
        a.origin.left.left = Node(7)
        self.assertFalse(is_avl_tree(a))  # 1

        """
        (6)
        False at Node(6) since 6 <= 10 but it is in the right subtree of 10
        
                  10
                 / \
                7   6
               /     
              5      
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 2
        a.origin.left = Node(7)
        a.origin.left.height = 1
        a.origin.right = Node(6)
        a.origin.left.left = Node(5)
        self.assertFalse(is_avl_tree(a))  # 1

        """
        (7)
        True, it is valid AVL tree that satisfies all properties
                  10
                 / \
                5   15
               /     
              1      
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 2
        a.origin.left = Node(5)
        a.origin.left.height = 1
        a.origin.right = Node(15)
        a.origin.left.left = Node(1)
        self.assertTrue(is_avl_tree(a))  # 1

        """
        (8)
        True, it is not valid AVL tree that satisfies all properties since 8 is in the right subtree of 10 but 8 < 10
                  10
                 /   \
                5    15
               /    /  \
              1    8    16
                 
        """
        a = AVLTree()
        a.origin = Node(10)
        a.origin.height = 2

        a.origin.left = Node(5)
        a.origin.left.height = 1
        a.origin.left.left = Node(1)

        a.origin.right = Node(15)
        a.origin.right.height = 1
        a.origin.right.left = Node(8)
        a.origin.right.right = Node(16)
        self.assertFalse(is_avl_tree(a))  # 1

        """(9) Test Empty Tree"""
        a = AVLTree()
        self.assertTrue(is_avl_tree(a))  # 1

    def test_is_avl_tree(self):
        def create_tree(tree, height):
            """
            Create full binary tree with some value of same height as provided
            """
            tree.origin = Node((2 ** (height), 2 ** (height - 1)))
            tree.origin.height = height
            num = 2 ** (height + 1) - 1
            x = 1
            q = [tree.origin]

            while x < num:
                node = q.pop(0)
                real_value, diff = node.value
                current_height = node.height
                node.value = real_value
                node.right = Node((node.value + diff, diff // 2))
                node.right.height = current_height - 1
                node.left = Node((node.value - diff, diff // 2))
                node.left.height = current_height - 1
                q.extend([node.left, node.right])
                x += 2
            # Assign the value to only just value
            for node in q:
                node.value = node.value[0]

        """(1) Test Empty Tree"""
        a = AVLTree()
        self.assertTrue(is_avl_tree(a))  # 1

        """(2) Test Following Construct Tree"""

        """
        Only one node:
              2
        """
        a.origin = Node(2)
        a.origin.height = 0
        self.assertTrue(is_avl_tree(a))  # 1

        """
        Two nodes as follow:
              2
             /
            1
        """
        a.origin.height = 1
        a.origin.left = Node(1)
        self.assertTrue(is_avl_tree(a))  # 2

        """
        Adding 0 node to above tree, making tree imbalance
               2
              /
             1
            /
           0
        """
        a.origin.height = 2
        a.origin.left.height = 1
        a.origin.left.left = Node(0)
        self.assertFalse(is_avl_tree(a))  # 3

        """
        Adding 5 on left, making tree balance again:
               2
              / \
             1   5
            /
           0
        """
        a.origin.right = Node(5)
        self.assertTrue(is_avl_tree(a))  # 4

        """
        (3)
        False at level 2 - both sides False
        Also, testing along construction
        Imbalance --> 2 and -2

                  10
                 / \
                5   15
               /     \
              2       20
             /         \
            1           25
        """

        a = AVLTree()
        self.assertTrue(is_avl_tree(a))  # 1 Empty Tree

        a.origin = Node(10)
        a.origin.height = 2
        self.assertTrue(is_avl_tree(a))  # 2 Adding 10 as root

        a.origin.right = Node(15)
        self.assertTrue(is_avl_tree(a))  # 3 Adding 15 as right of root
        a.origin.left = Node(5)
        self.assertTrue(is_avl_tree(a))  # 4 Adding 5 as left of root

        a.origin.right.right = Node(20)
        self.assertTrue(is_avl_tree(a))  # 5 Adding 20 as right of 15

        a.origin.left.left = Node(2)
        self.assertTrue(is_avl_tree(a))  # 6 Adding 2 as left of 5

        a.origin.right.right.right = Node(25)
        self.assertFalse(is_avl_tree(a))  # 7 adding 25 as left 20

        a.origin.left.left.left = Node(1)

        self.assertFalse(is_avl_tree(a))  # 8 adding 1 as left of 2

        """
        (4)
        False at level 2 - one side False

                  10
                 / \
                5   15
               /    /\
              2    12 20
             /         \
            1           25
        """

        a.origin.right.left = Node(12)
        self.assertFalse(is_avl_tree(a))  # 1 adding 12 as shown above

        a.origin.left.left.left = None
        self.assertTrue(is_avl_tree(a))  # 2 removing 1 from tree

        """
        (5) testing below tree
                  10
                 /  \
                5    15
               /  \    \
              2    12   20
             /           
            0            
        """
        a.origin.right.left = None
        a.origin.left.left.left = Node(0)
        a.origin.left.right = Node(12)
        a.origin.right.right.right = None
        self.assertFalse(is_avl_tree(a))  # 1

        """
        (6) Test Tree below at each step of constructing

                   10
                 /   \
                5    15
               / \   / \
              2   8 12 20
             /          \
            1            25
        """
        a.origin.left.right = Node(8)
        a.origin.right.left = Node(12)
        a.origin.right.right.right = Node(25)
        self.assertTrue(is_avl_tree(a))  # 1 Testing above tree

        a.origin.left.right.left = Node(6)
        self.assertTrue(is_avl_tree(a))  # 2 Adding node 6 as left of 8

        a.origin.left.right.right = Node(9)
        self.assertTrue(is_avl_tree(a))  # 3 Adding 9 as right of 8

        a.origin.left.left.right = Node(4)
        self.assertTrue(is_avl_tree(a))  # 4 Adding 4 as right of 2

        a.origin.right.left.right = Node(14)
        self.assertTrue(is_avl_tree(a))  # 5 Adding 14 as right of 12

        a.origin.right.left.left = Node(11)
        self.assertTrue(is_avl_tree(a))  # 6 Adding 11 as left of 12

        # False at last level - bottom right
        """
        Updating tree, so you can keep track
                     10
                 /       \
                5         15
               / \        /  \
              2    8     12   20
             /  \  / \   / \     \
            1    4 6  9 11 14     25
        """
        a.origin.right.right.right.right = Node(30)  # adding 30 as right most node

        self.assertFalse(is_avl_tree(a))  # 7

        a.origin.right.right.right.right = None  # Removing 30
        a.origin.right.right.right.left = Node(23)  # Adding 23 as left of 20

        self.assertFalse(is_avl_tree(a))  # 8

        # imbalance of more than absolute of 2
        a.origin.right.right.right.left.right = Node(21)

        self.assertFalse(is_avl_tree(a))  # 9

        """
        (7) Test full tree with height 1
                2
               /  \
              1    3
        """
        a = AVLTree()
        create_tree(a, 1)
        self.assertTrue(is_avl_tree(a))  # 1

        a.origin.right = None  # removing 3
        self.assertTrue(is_avl_tree(a))  # 2

        a.origin.left = None  # removing 1
        self.assertTrue(is_avl_tree(a))  # 3
        """
        (8) Test full tree with height 2
                    4
                  /   \
                 2     6
                / \   / \
               1  3  5   7  
        """
        a = AVLTree()
        create_tree(a, 2)
        self.assertTrue(is_avl_tree(a))  # 1

        a.origin.right.left = None  # removing 5
        self.assertTrue(is_avl_tree(a))  # 2
        # Changing right subtree to None, making it imbalance
        a.origin.right = None  # removing all subtree of 5
        self.assertFalse(is_avl_tree(a))  # 3

        a.origin.left = None  # removing subtree of 2
        self.assertTrue(is_avl_tree(a))  # 4

        """(9) Test full tree with height 2, with both imbalance and invalid value
                    4
                  /   \
                 2     6
                / \   / \
               1  3  5   7  
        """
        a = AVLTree()
        create_tree(a, 2)
        self.assertTrue(is_avl_tree(a))  # 1

        # Make it invalid
        a.origin.left.right = Node(6)
        self.assertFalse(is_avl_tree(a))  # 2

        # Revert tree back to valid
        a.origin.value = 7
        a.origin.right.value = 10
        a.origin.right.right.value = 20
        a.origin.right.left.value = 9
        self.assertTrue(is_avl_tree(a))  # 3

        a.origin.left = None
        self.assertFalse(is_avl_tree(a))  # 4

        """(10) Test full tree with height 3, with invalid value
        This one is quite large tree, it's full tree check zyBooks for definition of a full tree.
        Aka, calling inorder will get 1, 2, 3, ..., 13, 14, 15
        """
        a = AVLTree()
        create_tree(a, 3)
        self.assertTrue(is_avl_tree(a))  # 1

        a.origin.right.left.value = 3
        self.assertFalse(is_avl_tree(a))  # 2

        a.origin.right.left.value = 10
        self.assertTrue(is_avl_tree(a))  # 3

        a.origin.right.left.left.value = 7
        self.assertFalse(is_avl_tree(a))  # 4


if __name__ == '__main__':
    unittest.main()
