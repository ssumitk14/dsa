class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # print(self)
        child.parent = self
        # print(child.parent)
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level

    def print_tree(self):
        """
        Prints the tree
        :return:
        """

        spaces = " " * self.get_level() * 5
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix + self.data)
        if self.children:  # Putting this check as the least node will have no children
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("Think pad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Google"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    return root


if __name__ == "__main__":
    tree = build_tree()
    # tree_
