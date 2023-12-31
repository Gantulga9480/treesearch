import numpy as np
from .base import BaseTree
from .node import Node


class BredthFirstSearch(BaseTree):

    def __init__(self, max_depth: int = 1) -> None:
        super().__init__(max_depth)

    def search(self, root_node: Node):
        self.append(root_node)
        while True:
            node: Node = self.popleft()
            if node is not None:
                if node.depth < self.max_depth:
                    expanded = self.expand(node)
                    if not expanded:
                        self.leaf_nodes.append(node)
                    continue
                self.append(node)  # put back node to queue
            break
        return self.select()

    def select(self):
        scores = []
        edges = []

        for node in self.queue:
            branch_edges, branch_values = node.unroll()
            edges.append(branch_edges)
            scores.append(branch_values)
        if edges:
            idx = np.argmax(np.sum(scores, axis=1))
            return list(zip(edges[idx], scores[idx]))

        for node in self.leaf_nodes:
            branch_edges, branch_values = node.unroll()
            edges.append(branch_edges)
            scores.append(branch_values)
        if edges:
            idx = np.argmax(np.sum(scores, axis=1))
            return list(zip(edges[idx], scores[idx]))
        return None
