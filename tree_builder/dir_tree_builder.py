# dir_tree_build.py
import hashlib
import os
from tree_builder.treenode import Treenode


def build_tree(dir_path):
    helper = {dir_path: Treenode(dir_path)}
    for root, dirs, files in os.walk(dir_path, topdown=True):
        for item in dirs + files:
            complete_path = os.path.join(root, item)
            node = helper[complete_path] = Treenode(item)
            node.path = complete_path
            node.type = "Folder" if item in dirs else None
            if item in files:
                type = os.path.splitext(item)
                # node.add_hash((hashlib.md5(open((complete_path), "rb").read()).hexdigest()))
                node.add_file(complete_path, item, os.path.getsize(complete_path), type)
            helper[root].add_child(node)
    return helper[dir_path]

    """
      TO DO LIST:
       - Searching files/dirs 
       - Create/Remove/Move Dirs & Files
       - Open files 
       - Scan fo duplicates in files 
          (first compare size, then if size1 == size2 --> use hashes)
    """
