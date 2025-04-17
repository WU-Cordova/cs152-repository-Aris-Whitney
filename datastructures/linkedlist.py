from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head:Optional[LinkedList.Node]=None
        self.tail:Optional[LinkedList.Node]=None
        self.size:int=0
        self.data_type=data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list=LinkedList(data_type)
        for item in sequence:
            if not isinstance(item, data_type):
                raise TypeError(f"Item {item} is not of type {data_type}")
            linked_list.append(item)
        return linked_list

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be or type {self.data_type}")
        new_node=LinkedList.Node(item)
        if not self.head:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node
        self.size +=1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be of type {self.data_type}")
        new_node=LinkedList.Node(item)
        if not self.head:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node
        self.size +=1
    def insert_before(self, target: T, item: T) -> None:
        if not isinstance (target, self.data_type):
            raise TypeError(f"Target must be of type {self.data_type}")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be of type {self.data_type}")
        node=self.head
        while node:
            if node.data == target:
                new_node=LinkedList.Node(item)
                new_node.next=node
                new_node.previous=node.previous
                if node.previous:
                    node.previous.next=new_node
                node.previous=new_node
                if node == self.head:
                    self.head=new_node
                self.size += 1
                return
            node=node.next
        raise ValueError(f"Target {target} not found")



    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type):
            raise TypeError(f"Target must be of type {self.data_type}")
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be of type {self.data_type}")
        node=self.head
        while node:
            if node.data ==target:
                new_node=LinkedList.Node(item)
                new_node.previous=node
                new_node.next=node.next
                if node.next:
                    node.next.previous=new_node
                node.next=new_node
                if node == self.tail:
                    self.tail=new_node
                self.size +=1
                return
            node=node.next
        raise ValueError(f"Target {target} not found")

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be of type {self.data_type}")
        node=self.head
        while node:
            if node.data==item:
                if node.previous:
                    node.previous.next=node.next
                if node.next:
                    node.next.previous=node.previous
                if node == self.tail:
                    self.tail=node.previous
                self.size -=1
                return
            node = node.next
        raise ValueError(f"Item {item} not found")

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item must be of type {self.data_type}")
        node=self.head
        while node:
            next_node=node.next
            if node.data==item:
                if node.previous:
                    node.previous.next=node.next
                else:
                    self.head=node.next
                if node.next:
                    node.next.previous=node.previous
                else:
                    self.tail=node.previous
                self.size -=1
            node=node.next

    def pop(self) -> T:
        if not self.tail:
            raise IndexError("Pop from empty list")
        data= self.tail.data
        self.remove(data)
        return data

    def pop_front(self) -> T:
        if not self.head:
            raise IndexError("Pop from empty list")
        data=self.head.data
        if self.head.next:
            self.head=self.head.next
            self.head.previous=None
        else:
            self.head=self.tail=None
        self.size -=1
        return data

    @property
    def front(self) -> T:
        if not self.head:
            raise IndexError("List is empty")
        return self.head.data

    @property
    def back(self) -> T:
        if not self. tail:
            raise IndexError("List is empty")
        return self.tail.data
    @property
    def empty(self) -> bool:
        return self.size ==0

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.head=self.tail=None
        self.size=0

    def __contains__(self, item: T) -> bool:
        node=self.head
        while node:
            if node.data==item:
                return True
            node=node.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node=self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data=self.travel_node.data
        self.travel_node=self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        node=self.tail
        reversed_list=LinkedList(self.data_type)
        while node:
            reversed_list.append(node.data)
            node=node.previous
        return reversed_list
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.size !=other.size:
            return False
        node1=self.head
        node2=other.head
        while node1:
            if node1.data != node2.data:
                return False
            node1=node1.next
            node2=node2.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.size}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
