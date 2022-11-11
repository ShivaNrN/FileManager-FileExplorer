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


def find_copies(arr):
    result = list((k, sum(1 for i in arr if k in i)) for k in set(m[2] for m in arr))
    helper = []

    for x in range(len(result)):
        if (result[x][1]) > 1:
            helper.append(result[x][0])
    for i in range(len(arr)):
        if arr[i][2] in helper:
            copies.append(
                [arr[i][0], arr[i][1], arr[i][2], arr[i][3], get_hash(arr[i][0])]
            )
    copiees = sorted(copies, key=lambda x: x[2], reverse=False)
    return copiees


def get_hash(file_path):
    hash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    return hash
