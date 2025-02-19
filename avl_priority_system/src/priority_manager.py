from avl_tree import AVLTree

class PriorityManager:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None

    def add_task(self, task_id, priority):
        self.root = self.tree.insert(self.root, task_id, priority)

    def display_tasks(self, node, level=0):
        if node:
            self.display_tasks(node.right, level + 1)
            print("   " * level + f"({node.priority}) {node.key}")
            self.display_tasks(node.left, level + 1)
