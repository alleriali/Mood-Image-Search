import csv
count = 0
google_image_dict ={}
with open('/home/ying/Downloads/Train_GCC-training.tsv') as f:
    for line in f:
        (key, value) = line.split()
        print(key,value)
        google_image_dict[key] = value


