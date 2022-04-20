# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : binaryTreeSearch.py
# Time       ：2022/3/31 16:57
# Author     ：hippoSang
# Email      ：842960911@qq.com
# Description：
"""
import random
import json


class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# randomly generate a binary tree from an built root node
def random_binary_tree_generator(root):
    tree_dict = {"val": root.val}
    is_left_growth = True if random.randint(0, 10) > 5 else False
    is_right_growth = True if random.randint(0, 10) > 5 else False
    if is_left_growth:
        root.left = BinaryTreeNode(val=random.randint(0, 10))
        tree_dict["left"] = random_binary_tree_generator(root=root.left)[1]
    if is_right_growth:
        root.right = BinaryTreeNode(val=random.randint(0, 10))
        tree_dict["right"] = random_binary_tree_generator(root=root.right)[1]
    return root, tree_dict


root = BinaryTreeNode(val=1)
root, tree_dict = random_binary_tree_generator(root=root)
print(root)  # the tree root node
print(json.dumps(tree_dict, indent=4, ensure_ascii=False))
# your code here


# 前序遍历
def front_search(root):
    if root:
        return [root.val] + front_search(root.left) + front_search(root.right)
    else:
        return []


# 中序遍历
def mid_search(root):
    if root:
        return mid_search(root.left) + [root.val] + mid_search(root.right)
    else:
        return []


# 后序遍历
def after_search(root):
    if root:
        return after_search(root.left) + after_search(root.right) + [root.val]
    else:
        return []


def binary_tree_search(root, mode="front"):
    if root:
        if mode == "front":
            return [root.val] + binary_tree_search(root.left, mode=mode) + binary_tree_search(root.right, mode=mode)
        elif mode == "mid":
            return binary_tree_search(root.left, mode=mode) + [root.val] + binary_tree_search(root.right, mode=mode)
        elif mode == "after":
            return binary_tree_search(root.left, mode=mode) + binary_tree_search(root.right, mode=mode) + [root.val]
        else:
            print("unsupported mode:{}".format(mode))
            return []
    else:
        return []


if __name__ == "__main__":
    print("front search result:", front_search(root))
    print("mid search result:", mid_search(root))
    print("after search result:", after_search(root))

    print("front search result:", binary_tree_search(root, mode="front"))
    print("mid search result:", binary_tree_search(root, mode="mid"))
    print("after search result:", binary_tree_search(root, mode="after"))
