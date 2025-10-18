from .node import Node
from .base import BaseTree
import random
import math


class MonteCarloSearch(BaseTree):

    def __init__(self, num_iters: int = 1, c: float = 1) -> None:
        super().__init__(num_iters)
        self.c = c

    def simulate(self, node: Node) -> float:
        raise NotImplementedError

    def search(self, root_node: Node):
        for _ in range(self.max_depth):
            node = root_node

            while node.has_child:
                node = max(node.children, key=lambda n: self.UCB1(n))

            new_nodes = self.expand(node)
            if new_nodes:
                for n in new_nodes:
                    n.depth = node.depth + 1
                    node.addchild(n)
                node = random.choice(new_nodes)

            value = self.simulate(node)

            self.backprob(node, value)

        if root_node.has_child:
            edges, scores = max(root_node.children, key=lambda c: c.visit_count).unroll()
            return edges, scores
        return None

    def backprob(self, node: Node | None, value: float):
        while node is not None:
            node.value += value
            node.visit_count += 1
            node = node.parent

    def UCB1(self, node: Node):
        if node.visit_count == 0 or node.parent is None:
            return float('inf')
        return (node.value / node.visit_count + self.c * math.sqrt(math.log(node.parent.visit_count) / (node.visit_count)))
