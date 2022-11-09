# dir_tree_builder with comments
import hashlib
import json
import re
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import pandas as pd

# First, let's create a Class
class Treenode:
    """
    __init__ function is the constructor of the class. It is called whenever a new object is created.
    The first argument is self, which is similar to keyword "this" in Java.
    It assigns the parameters and method for every Object of the class,
    so we can call them simply by using the_tree.method() or the_tree.parameters
    This function accept only one argument (name) which will  be the name of the folder to create the tree upon.
    """

    def __init__(self, name):
        self.name = name  # FILE name or FOLDER name --> short path
        self.size = None  # dimension of the FILE in bytes
        self.type = None  # extension of the FILE
        self.path = None  # complete path FILE  or FOLDER
        self.children = []  # If NO CHILDREN ==> IS A FILE else IS A FOLDER
        self.parent = None  # IF NO PARENT ==> ROOT
        # self.hash = None

    """
  add_child() function is used to properly add a child to the parent. 
  For every child it appends it to the list [children] and update the parent 
  i.e: 
  tree = TreeNode("root tree")
  brach_tree = TreeNode("branch")
  tree.add_child(branch_tree)  --> tree is self - branch_tree is child
  So, child.parent = self ==> branc_tree.parent = tree 
  and, self.children.append(child) ==> tree.children.append(branch_tree) 
  """

    def add_child(self, child):  # --> ADD FOLDER
        child.parent = self  # --> ASSIGN PARENT FOLDER
        self.children.append(child)  # --> ASSIGN CHILD FOLDER
        # all_folders_list.append([self.name, self.path]) # --> ADD FOLDER DATA to a list

    # def add_hash(self, file):
    #     self.hash =  file
    #     all_hashes.append([self.hash, self.path])

    # Pretty straithforward, every thime is called create a file.
    # It is called recursively when building the Tree. Easier to distinguish file from folders.
    # Stores the file properties as a nested list --> [[p,n,s,t],[p,n,s,t]...]
    def add_file(self, path, name, size, type):
        self.path = path
        self.name = name
        self.type = type[-1]  # -1 gets the latest element of this tuple
        self.size = size
        all_files_list.append([self.path, self.name, self.size, self.type])
        return all_files_list

    """
  get_level() function to find at which level (or depth) is the object. 
  Basically answering the question how far from the root is a given child?
    - initiate a variable (level) with value 0
    - assign to variable (p) the value stored in parent. 
    - it update the level by one at every iteration, and update p assigning the new self.parent to it, 
      until this value isnot "None"  (we can simply use while p, instead of while p != None).
      Whenever it finds another tree object in the self.parent it continues searching for its parent.
    - finally return the level
  """

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    """
  print_tree() is a recursive function to actually print out the whole tree. 
  spaces ==> add indentation based upon the level of the sub tree.
  prefix ==> add an elbow |__ if the tree has parents, else is the root tree we don't need spaces nor elbows.
  for every child of the tree it recursively call the function itself until no children are found.
  Moreover, it checks if the current istance has a size (aka is a file) and 
  when True print the current object Size (in bytes if size<1024, else in kb) 
  """

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


"""
ask_directory() function to ask the user lol
That prompt the select dialog screen. title = give a name to the select dialog window. 
"""


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


"""
build_tree(path) function that actually create the TreeNode object(s) 
An argument (the complete path must be passed as a string --> from ask_directory())
  -  initialize a helper variable as a dictionary containing the given path(s) as key(s) and the 
     tree object for the given path as value(s) (basically the tree root) 
  -  call the os.walk() method of the library os. topdown = True is superflous since True is the default value.
     os.walk(path) basically return a tuple consisting of 
      - a string (the root) 
      - a list (directories inside the root)
      - a list (files inside the root)
      Whenever it finds a directory, step into to return another tuple and so on..
  -  for every item in the two lists dirs and files create a new node with that item
      + concatenate lists as well: 
      If dirs = ["folderA"] and files = ["fileA"] --> dirs + files is ["folderA", "fileA"])
  -  the new node is created as follow: 
      - calls the helper dictionary
      - find the child associated with the current item. 
        In order to do so we use os.path.join() which joins the root path with the current item. 
        If root = "C:/Level0/Level1" and path = "file1", the join would return "C:/Level0/Level1/file1"
      - assign the type "Folder" to the node if current item is a folder
      - checks if current item is a file. If True add the node via add_file,
        assigning it to its parent
      - add the node to the root Tree as its child, using the root path as key,
        assuring that each file and folder is a sub-tree of the correct folder
  -  return the first key of the dictionary, which in fact is the complete Tree
"""


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
  Saving the list as a dictionary/JSON format if needed (i.e. web app)
  The function asks for a list and the directory where to save the file into.
  for any sub-list in the list (aka rows), assign the file properties as keys - values
  json module is imported to add some indentation to the output. 
  .dumps() --> Serialize the passed object to json formatted string.
  (.txt --> .json should work)
"""


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
    """
  formatting the path. 
   re --> import re (regex), 
   search(r"a regex",the string to apply the regex) --> Scan through a string, 
                                looking for any location where this RE matches.
       ^ --> matches at the start 
       / --> char to start with
      [] --> used for specifying a character class, which is a set of characters that I wish to match
       + --> matches one or more times
       $ --> matches at the end
   group(0) --> not clear really
  """
    selected_root = re.search(r"[^/]+$", target_path).group(0)
    desired_name = f"file_dictionary_log[{selected_root}].txt"
    # Saving the output to a file - "w" stands fo write.
    # (with open() assures the file is closed even if
    # throwing exceptions. Avoiding files to keep opened in os)
    with open(os.path.join(target_path, desired_name), "w") as f:
        f.write(pretty)
    return


"""
  Saving to .csv format. Basically to have a table of files. Can be used fo DB as well
  desired_name is constructed as prevously in save_to_dict
  Then I try the panda library to work with large files. Seems pretty usefull.
  encoding can give some problems with accents and weird chars. Excel does not enjoy 
  utf-8 or utf-16 as well.. "Todo" --> check output carefully, make some testing 
"""


def save_to_csv(lists, target_path):
    selected_root = re.search(r"[^/]+$", target_path).group(0)
    desired_name = f"files[{selected_root}].csv"
    df = pd.DataFrame(
        lists, columns=["Complete Path", "File Name", "File Size", "Type (bytes)"]
    )
    df.to_csv(os.path.join(target_path, desired_name), encoding="latin1")
    return print(df)


"""
  Main Function of the script. 
  __name__ and "__main__" explained here if needed. (not today) -> https://realpython.com/if-name-main-python/
  in the main funct of the script we simply 
    - ask the user a directory using the proper method
    - inizialize the data structures needed for storing files' data
    - build the tree via build_tree(chosen directory), 
    - print out the tree --> Output in terminal (can be saved as .txt)
"""
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
