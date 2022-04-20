# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : linked_list_base_op.py
# Time       ：2022/4/20 15:48
# Author     ：hippoSang
# Email      ：842960911@qq.com
# Description：
"""


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, vals):
        assert (isinstance(vals, list) and vals), "vals should be a non empty list"

        cur = LinkedListNode(vals[0])
        self.head = cur
        for val in vals[1:]:
            next = LinkedListNode(val)
            cur.next = next
            cur = next

    def print(self):
        cur = self.head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print(None)

    def remove(self, index):
        last = None
        cur = self.head
        next = cur.next
        for _ in range(index):
            last = cur
            cur = next
            if not cur:
                print("len of linked list < {}".format(index + 1))
                return
            next = cur.next
        if last:
            last.next = next
        else:
            self.head = next

    def append(self, val):
        cur = self.head
        next = cur.next
        while next:
            cur = next
            next = cur.next
        cur.next = LinkedListNode(val)

    def pop(self):
        cur = self.head
        next = cur.next
        if not next:
            print("len of linked list is 1, could not pop the remaining one node")
            return
        while next:
            if next.next:
                cur = next
                next = cur.next
            else:
                return next

    def insert(self, index, val):
        last = None
        cur = self.head
        next = cur.next
        for _ in range(index):
            last = cur
            cur = next
            if not cur:
                print("len of linked list < {}".format(index + 1))
                return
            next = cur.next
        if last:
            last.next = LinkedListNode(val)
            last.next.next = cur
        else:
            self.head = LinkedListNode(val)
            self.head.next = cur

    def change(self, index, val):
        cur = self.head
        for _ in range(index):
            cur = cur.next
            assert cur, "len of linked list < {}".format(index+1)
        cur.val = val


if __name__ == "__main__":
    vals = list(range(10))
    ll = LinkedList(vals=vals)
    ll.print()
    # remove
    print("*"*20, "remove", "*"*20)
    ll.remove(0)
    ll.print()
    ll.remove(20)
    ll.print()
    ll.remove(7)
    ll.print()
    # append
    print("*"*20, "append", "*"*20)
    ll.append(20)
    ll.print()
    # pop
    print("*" * 20, "pop", "*" * 20)
    print(ll.pop().val)
    ll.print()
    # insert
    print("*" * 20, "insert", "*" * 20)
    ll.insert(0, 0)
    ll.insert(4, 3.5)
    ll.print()
    # change
    print("*" * 20, "change", "*" * 20)
    ll.change(4, 0)
    ll.print()
