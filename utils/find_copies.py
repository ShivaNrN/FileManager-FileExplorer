import hashlib
import json

# files_json = dict()
# with open("C:\level0\\file_dictionary_log[level0].json", "r") as f:
#     files_dictionary = f.read()
copies = []


def take_json_input(the_json):
    jsonfile = json.loads(the_json)
    new_list = list(jsonfile.values())
    filelist = []
    for v in new_list:
        filelist.append(list((v.values())))
    return filelist


def find_copies(all_files):
    sizes_counter = list(
        (k, sum(1 for i in all_files if k in i)) for k in set(m[2] for m in all_files)
    )
    not_unique_sizes = []

    for x in range(len(sizes_counter)):
        if (sizes_counter[x][1]) > 1:
            not_unique_sizes.append(sizes_counter[x][0])
    for i in range(len(all_files)):
        if all_files[i][2] in not_unique_sizes:
            copies.append(
                [
                    all_files[i][0],
                    all_files[i][1],
                    all_files[i][2],
                    all_files[i][3],
                    get_hash(all_files[i][0]),
                ]
            )

    sizes_counter = list(
        (k, sum(1 for i in copies if k in i)) for k in set(m[4] for m in copies)
    )
    not_unique_sizes = []

    for i in range(len(sizes_counter)):
        if sizes_counter[i][1] > 1:
            not_unique_sizes.append(sizes_counter[i][0])

    copies[:] = [item for item in copies if item[4] in not_unique_sizes]

    sorted_copies = sorted(copies, key=lambda x: x[4], reverse=False)
    return sorted_copies


def get_hash(file_path):
    hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    return hash
