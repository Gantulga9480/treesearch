from typing import Tuple, List


class Node:

    def __init__(self,
                 parent: 'Node',
                 edge=None,
                 value: float = 0,
                 is_leaf: bool = False) -> None:

        self.parent: Node = parent
        self.edge = edge
        self.is_leaf = is_leaf
        self.value = value
        self.depth = self.parent.depth + 1 if self.parent else 0
        self.visit_count = 0
        self.children = []

    @property
    def has_child(self) -> bool:
        return self.children.__len__() > 0

    def addchildren(self, children: List['Node']):
        if not isinstance(children, list):
            raise TypeError(f'Expected list, got {type(children)}')
        self.children.extend(children)

    def unroll(self) -> Tuple[float, list]:
        branch_values = [self.value]
        branch_edges = [self.edge]
        parent = self.parent
        while parent is not None:  # loop until root node
            branch_values.append(parent.value)
            branch_edges.append(parent.edge)
            parent = parent.parent
        branch_edges.pop()  # remove root node edge (beacuse it's None)
        branch_values.pop()  # # remove root node value (beacuse it's same to all nodes)
        branch_edges.reverse()
        branch_values.reverse()
        return branch_edges, branch_values
