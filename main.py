from tree_builder.dir_tree_builder import build_tree
from utils.find_copies import take_json_input, find_copies
from utils.ask_directory import ask_directory
from utils.save_output import save_to_csv, save_to_dict
from tree_builder.treenode import all_files_list

if __name__ == "__main__":

    # all_folders_list = []
    root_path = ask_directory("Select the starting root folder of the tree")
    tree = build_tree(root_path)
    # tree.print_tree()

    the_json = save_to_dict(all_files_list)
    filelist = take_json_input(the_json)
    copies = find_copies(filelist)

    save_to_csv(
        copies, ask_directory("Select a folder to export to copies.csv"), root_path
    )
