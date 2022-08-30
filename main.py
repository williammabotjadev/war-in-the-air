import os
from process_img import process_img
from datetime import datetime

directory = "./data_collection/feb_data_c/"
filenames = []
count = 1
datef = datetime.now().strftime("%d-%m-%y%H:%M:%S")
temp_path = datef

if not os.path.exists(temp_path):
    os.mkdir(f"./pre_images/{temp_path}")

# Process Latest Images

print(os.listdir(directory))

print(directory)

dir_len = len(os.listdir(directory))

print(dir_len)

for filename in os.listdir(directory):
    if count > dir_len:
        break
    process_img(f"./data_collection/feb_data_c/{filename}", count, temp_path)
    count += 1



