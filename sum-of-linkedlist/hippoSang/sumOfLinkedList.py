# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : sumOfLinkedList.py
# Time       ：2022/3/31 15:31
# Author     ：hippoSang
# Email      ：842960911@qq.com
# Description：
"""


class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __add__(self, other):
        left = self.head
        right = other.head
        new_head = LinkedListNode((left.val + right.val) % 10)
        carry = int((left.val + right.val) / 10)  # 进位数
        left = left.next
        right = right.next
        cur_node = new_head
        while left or right:
            left_val = left.val if left else 0
            right_val = right.val if right else 0
            new_node = LinkedListNode((left_val + right_val + carry) % 10)  # 取个位数
            carry = int((left_val + right_val + carry) / 10)  # 取十位数
            cur_node.next = new_node
            cur_node = new_node
            left = left.next
            right = right.next
        if carry != 0:
            cur_node.next = LinkedListNode(carry)
        # new_head = linked_list_generator(result_vals)
        new_linked_list = LinkedList(head=new_head)
        return new_linked_list


def print_linked_list(linked_list):
    cur_node = linked_list
    while cur_node:
        print(cur_node.val, end="->")
        cur_node = cur_node.next
    print("|")


def linked_list_generator(vals):
    head = LinkedListNode(val=vals[0], next=None)
    cur_node = head
    for val in vals[1:]:
        next_node = LinkedListNode(val=val, next=None)
        cur_node.next = next_node
        cur_node = next_node
    return head


def sum_of_linked_list(left_linked_list, right_linked_list):
    left = left_linked_list.head
    right = right_linked_list.head
    result_vals = []
    carry = 0  # 进位数
    while left or right:
        left_val = left.val if left else 0
        right_val = right.val if right else 0
        result_vals.append((left_val + right_val + carry) % 10)  # 取个位数
        carry = int((left_val + right_val + carry) / 10)  # 取十位数
        left = left.next
        right = right.next
    if carry != 0:
        result_vals.append(carry)
    new_linked_list = linked_list_generator(result_vals)
    return new_linked_list


if __name__ == "__main__":
    left_linked_list = LinkedList(head=linked_list_generator(vals=[2, 4, 3]))
    right_linked_list = LinkedList(head=linked_list_generator(vals=[5, 6, 4]))
    new_linked_list = left_linked_list + right_linked_list
    # new_linked_list = sum_of_linked_list(left_linked_list=left_linked_list, right_linked_list=right_linked_list)
    print_linked_list(left_linked_list.head)
    print_linked_list(right_linked_list.head)
    print_linked_list(new_linked_list.head)
