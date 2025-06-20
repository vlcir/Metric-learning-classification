import os
import pandas as pd

images_dir = "veri776_ds"
lists_dir = "list"

file_data = {}

train_path = os.path.join(lists_dir, "veri_train_list.txt")
with open(train_path, "r") as f:
    for line in f:
        filename, train_label = line.strip().split()
        file_data[filename] = {
            "label": int(filename.split("_")[0]),
            "cam_id": int(filename.split("_")[1][1::]),
            "split": "train",
            "is_query": None,
            "is_gallery": None,
            "path": os.path.join(images_dir, filename)
        }

query_path = os.path.join(lists_dir, "veri_query_list.txt")
with open(query_path, "r") as f:
    for line in f:
        filename = line.strip()
        if filename not in file_data:
            file_data[filename] = {
                "label": int(filename.split("_")[0]),
                "cam_id": int(filename.split("_")[1][1::]),
                "split": "validation",
                "is_query": True,
                "is_gallery": False,
                "path": os.path.join(images_dir, filename)
            }
        else:
            file_data[filename]["is_query"] = True

gallery_path = os.path.join(lists_dir, "veri_test_list.txt")
with open(gallery_path, "r") as f:
    for line in f:
        filename = line.strip()
        if filename not in file_data:
            file_data[filename] = {
                "label": int(filename.split("_")[0]),
                "cam_id": int(filename.split("_")[1][1::]),
                "split": "validation",
                "is_query": False,
                "is_gallery": True,
                "path": os.path.join(images_dir, filename)
            }
        else:
            file_data[filename]["is_gallery"] = True

df = pd.DataFrame.from_dict(file_data, orient="index")
df.to_csv("veri776_metadata.csv", index=False)

