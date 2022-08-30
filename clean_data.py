import os

mydir = "./data_collection/feb_data/"

for f in os.listdir(mydir):
    if not f.endswith(".json"):
        continue
    os.remove(os.path.join(mydir, f))