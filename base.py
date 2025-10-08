from collections import deque
from .node import Node


class BaseTree:

    def __init__(self, max_depth: int = 1) -> None:
        self.max_depth = max_depth
        self.queue: deque[Node] = deque()
        self.leaf_nodes: deque[Node] = deque()

    def reset(self) -> None:
        self.queue.clear()
        self.leaf_nodes.clear()

    def popright(self) -> Node | None:
        try:
            return self.queue.pop()
        except IndexError:
            return None

    def popleft(self) -> Node | None:
        try:
            return self.queue.popleft()
        except IndexError:
            return None

    def append(self, node: Node) -> None:
        self.queue.append(node)

    def search(self, root_node: Node):
        "Includes algorithm specific search logic"
        raise NotImplementedError

    def select(self):
        "Includes algorithm specific selection logic"
        raise NotImplementedError

    def expand(self, node: Node) -> bool:
        "Includes algorithm specific expansion logic. End application should override this method"
        raise NotImplementedError
