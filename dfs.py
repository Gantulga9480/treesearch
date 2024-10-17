from .base import BaseTree
from .node import Node
import numpy as np


class DepthFirstSearch(BaseTree):

    def __init__(self, max_depth: int = 1) -> None:
        super().__init__(max_depth)

    def search(self, root_node: Node):
        self.append(root_node)
        while True:
            node: Node = self.popright()
            if node is not None:
                if node.depth == self.max_depth:
                    self.leaf_nodes.append(node)
                    continue
                else:
                    expanded = self.expand(node)
                    if not expanded:
                        self.leaf_nodes.append(node)
                    continue
            break
        return self.select()

    def select(self):
        scores = []
        edges = []
        scores_sum = []

        for node in self.leaf_nodes:
            branch_edges, branch_values = node.unroll()
            edges.append(branch_edges)
            scores.append(branch_values)
            scores_sum.append(sum(branch_values))
        if edges:
            idx = np.argmax(scores_sum)
            return list(zip(edges[idx], scores[idx]))
        return None
