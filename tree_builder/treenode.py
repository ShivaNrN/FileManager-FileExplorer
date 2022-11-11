all_files_list = []


class Treenode:
    def __init__(self, name):
        self.name = name
        self.size = None
        self.type = None
        self.path = None
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_file(self, path, name, size, type):
        self.path = path
        self.name = name
        self.type = type[-1]
        self.size = size
        all_files_list.append([self.path, self.name, self.size, self.type])
        return all_files_list

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        nesting = prefix + self.name
        if self.size or self.size == 0:
            size = (
                f"{self.size} bytes" if self.size < 1024 else f"{self.size // 1024} Kb"
            )

        print(nesting + "   " + size if not self.children else nesting)
        for child in self.children:
            child.print_tree()
