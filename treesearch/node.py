import numpy as np
from typing import Tuple


class Node:

    def __init__(self,
                 parent: 'Node',
                 edge = None,
                 value: float = 0,
                 is_leaf: bool = False) -> None:

        self.parent: Node = parent
        self.edge = edge
        self.is_leaf = is_leaf
        self.value = value
        self.depth = self.parent.depth + 1 if self.parent else 0
        self.visit_count = 0
        self.children = []

    def addchildren(self, children: list['Node']):
        if not isinstance(children, list):
            raise TypeError(f'Expected list, got {type(children)}')
        self.children.extend(children)

    def unroll(self) -> Tuple[float, list]:
        branch_value = self.value
        branch_edges = [self.edge]
        parent = self.parent
        while parent is not None:  # loop until root node
            branch_value += parent.value
            branch_edges.append(parent.edge)
            parent = parent.parent
        branch_edges.pop()  # remove root node edge
        branch_edges.reverse()
        return branch_value, branch_edges
