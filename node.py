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
        edges = []
        values = []
        node = self
        # collect from this node up to but not including the root
        while node.parent is not None:
            edges.append(node.edge)
            values.append(node.value)
            node = node.parent
        edges.reverse()
        values.reverse()
        return edges, values
