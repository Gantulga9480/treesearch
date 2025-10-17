class Node:

    def __init__(self,
                 parent: 'Node | None',
                 edge = None,
                 value: float = 0,
                 is_leaf: bool = False) -> None:

        self.parent = parent
        self.edge = edge
        self.is_leaf = is_leaf
        self.value = value
        self.depth = self.parent.depth + 1 if self.parent else 0
        self.visit_count = 0
        self.children: list['Node'] = []

    @property
    def has_child(self) -> bool:
        return self.children.__len__() > 0

    def addchild(self, child: 'Node'):
        if not isinstance(child, Node):
            raise TypeError(f'Expected Node, got {type(child)}')
        self.children.append(child)

    def addchildren(self, children: list['Node']):
        if not isinstance(children, list):
            raise TypeError(f'Expected list, got {type(children)}')
        self.children.extend(children)

    def unroll(self):
        parent = self.parent
        branch_edges = [self.edge]
        branch_values = [self.value]
        while parent is not None:  # loop until root node
            branch_values.append(parent.value)
            branch_edges.append(parent.edge)
            parent = parent.parent
        branch_edges.pop()  # remove root node edge (beacuse it's None)
        branch_values.pop()  # # remove root node value (beacuse it's same to all nodes)
        branch_edges.reverse()
        branch_values.reverse()
        return branch_edges, branch_values
