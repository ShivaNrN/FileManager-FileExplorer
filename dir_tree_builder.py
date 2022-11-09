# dir_tree_build.py
import hashlib
import json
import re
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import pandas as pd


class Treenode:
    def __init__(self, name):
        self.name = name  # FILE name or FOLDER name --> short path
        self.size = None  # dimension of the FILE in bytes
        self.type = None  # extension of the FILE
        self.path = None  # complete path FILE  or FOLDER
        self.children = []  # If NO CHILDREN ==> IS A FILE else IS A FOLDER
        self.parent = None  # IF NO PARENT ==> ROOT
        # self.hash = None

    def add_child(self, child):  # --> ADD FOLDER
        child.parent = self  # --> ASSIGN PARENT FOLDER
        self.children.append(child)  # --> ASSIGN CHILD FOLDER

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
        if self.size:
            size = (
                f"{self.size} bytes" if self.size < 1024 else f"{self.size // 1024} Kb"
            )
        print(nesting + "   " + size if self.size else nesting)
        for child in self.children:
            child.print_tree()


def get_hash(file_path):
    hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    return hash


def ask_directory():
    Tk().withdraw()  # .withdraw --> method to untoggle an superflous dialog window.
    if work_flow == 0:
        title = "Select the starting root folder of the tree"
    elif work_flow == 1:
        title = "Select a folder to export to .csv"
    elif work_flow == 2:
        title = "Select a folder to export to .json"
    path = askdirectory(title=title)
    return path


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


def save_to_dict(lists, target_path):
    for c in range(len(lists)):
        all_files_dict[c] = {
            "Filepath": lists[c][0],
            "Name": lists[c][1],
            "Size": lists[c][2],
            "Type": lists[c][3],
        }
    pretty = json.dumps(all_files_dict, indent=2)
    print(pretty)

    selected_root = re.search(r"[^/]+$", target_path).group(0)
    desired_name = f"file_dictionary_log[{selected_root}].txt"

    with open(os.path.join(target_path, desired_name), "w") as f:
        f.write(pretty)
    return


def save_to_csv(lists, target_path):
    selected_root = re.search(r"[^/]+$", target_path).group(0)
    desired_name = f"files[{selected_root}].csv"
    df = pd.DataFrame(
        lists, columns=["Complete Path", "File Name", "File Size", "Type (bytes)"]
    )
    df.to_csv(os.path.join(target_path, desired_name), encoding="latin1")
    return print(df)


if __name__ == "__main__":

    all_files_list = []
    all_files_dict = dict()
    # all_folders_list = []

    work_flow = 0
    tree = build_tree(ask_directory())
    tree.print_tree()

    work_flow = 1
    save_to_csv(all_files_list, ask_directory())

    work_flow = 2
    save_to_dict(all_files_list, ask_directory())

    """
      TO DO LIST:
       - Searching files/dirs 
       - Create/Remove/Move Dirs & Files
       - Open files 
       - Scan fo duplicates in files 
          (first compare size, then if size1 == size2 --> use hashes)
    """
    # -------- Scraps to complete ----------

    # #Duplicates
    # copies = [h for h in dimensions if dimensions.count(h) > 1]
    # unique_copies = list(set(copies))
    # print(unique_copies)
    # i = 0
    # lst = []
    # lst = [all_files_list[i][0] for i in range(len(all_files_list))]
    # print(lst)
    # print(all_files_list)
