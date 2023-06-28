#!/usr/bin/python3
''' Modeule single linke list task '''


class Node:
    ''' Node Class '''
    def __init__(self, data, next_node=None):
        ''' Node constructor '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' data getter'''
        return self.__data

    @data.setter
    def data(self, value):
        ''' data setter '''
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        ''' next_node getter'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' next_node setter '''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    ''' single linked list class'''
    def __init__(self):
        ''' constructor '''
        self.__head = None

    def __str__(self):
        ''' replace __str__'''
        tmp = self.__head
        ret = ''
        while (tmp is not None):
            ret += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                ret += '\n'
        return ret

    def sorted_insert(self, value):
        '''insert new node ascending'''
        new_node = Node(value)
        pre = None
        curr = self.__head
        while (curr and curr.data < value):
            pre = curr
            curr = curr.next_node
        new_node.next_node = curr
        if (pre):
            pre.next_node = new_node
        else:
            self.__head = new_node
