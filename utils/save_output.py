import json
import re
import os
import pandas as pd

all_files_dict = dict()


def save_to_dict(lists, target_path=None):
    for c in range(len(lists)):
        all_files_dict[c] = {
            "Filepath": lists[c][0],
            "Name": lists[c][1],
            "Size": lists[c][2],
            "Type": lists[c][3],
        }
    pretty = json.dumps(all_files_dict, indent=2)

    # print(pretty)

    # selected_root = re.search(r"[^/]+$", target_path).group(0)
    # desired_name = f"file_dictionary_log[{selected_root}].json"

    # with open(os.path.join(target_path, desired_name), "w") as f:
    #     f.write(pretty)
    return pretty


def save_to_csv(lists, target_path, file_name):
    selected_root = re.search(r"[^/]+$", file_name).group(0)
    desired_name = f"files[{selected_root}].csv"

    for i in range(len(lists)):
        if "\u2013" in lists[i][0]:
            a = lists[i][0]
            lists[i][0] = a.replace("\u2013", "-")
            b = lists[i][1]
            lists[i][1] = b.replace("\u2013", "-")

    df = pd.DataFrame(
        lists,
        columns=[
            "Complete Path",
            "File Name",
            "File Size (bytes)",
            "Extension",
            "Hash",
        ],
    )
    df.to_csv(os.path.join(target_path, desired_name), encoding="latin-1")

    return df
