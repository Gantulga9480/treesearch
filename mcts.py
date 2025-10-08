# import numpy as np
# import random
# from .base import BaseTree


# class MonteCarloTreeSearch(BaseTree):

#     def __init__(self,
#                  root,
#                  executor: object,
#                  target=None,
#                  max_depth: int = 0) -> None:
#         super().__init__(root, executor, target, max_depth)
#         self.simulator = None

#     def search(self):
#         self.depth = 0
#         self.expand(0)
#         while self.depth < self.max_depth:
#             if self.traverse():
#                 continue
#             break
#         next_layer = self.get_layer(self.root.layer + 1)
#         score = [self.buffer[i].value for i in next_layer]
#         best_node = self.buffer[next_layer[np.argmax(score)]]
#         return best_node.unroll()[0][0]

#     def traverse(self, index=0):
#         node = self.buffer[index]
#         if node.visit_count == 0:
#             sim_result = self.simulate(node)
#             self.backprob(node, sim_result)
#             return True
#         elif node.visit_count != 0:
#             if node.has_child():
#                 selected_node = self.select(index)
#                 return self.traverse(selected_node)
#             elif node.visit_count == 1:  # just simulated
#                 return self.expand(index)
#         return False

#     def select(self, index):
#         node = self.buffer[index]
#         children = node.children
#         parent_visit = node.visit_count
#         scores = []
#         for i in children:
#             child = self.buffer[i]
#             child_visit = child.visit_count
#             value = child.value
#             ucb_score = self.UCB1(parent_visit, child_visit, value)
#             scores.append(ucb_score)
#         if scores.count(scores[0]) == len(scores):
#             return random.choice(children)
#         return children[np.argmax(scores)]

#     def expand(self, parent_index):
#         parent = self.buffer[parent_index]
#         parent.children.clear()
#         if parent.possible_actions:
#             for action in parent.possible_actions:
#                 if self.executor.move(copy.deepcopy(parent), action):
#                     self.append(self.create(parent, action))
#                     parent.children.append(len(self.buffer) - 1)
#             self.depth = self.buffer[-1].layer
#             return True
#         return False

#     def simulate(self, node):
#         return self.simulator.run(node)

#     def backprob(self, node, value):
#         while node is not None:
#             node.value += value
#             node.visit_count += 1
#             node = node.parent

#     def UCB1(self, N, n, value, C=10):
#         return 1_000_000 if n == 0 else (value + C * np.sqrt(np.log(N) / (n)))