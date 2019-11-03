import pickle
# url2description_vector_path = ['folder1/url2description_vector1.pickle', 'folder1/url2description_vector2.pickle',
#                                'folder1/url2description_vector3.pickle',
#                                'folder1/url2description_vector4.pickle', 'folder1/url2description_vector5.pickle',
#                                'folder1/url2description_vector6.pickle',
#                                'folder1/url2description_vector7.pickle', 'folder1/url2description_vector8.pickle',
#                                'folder1/url2description_vector9.pickle']
# count = 0
# url2descrip_vector = {}
# count_num=0
# sub_count = 0
# for path in url2description_vector_path:
#     pickle_in = open(path,"rb")
#     url2description_vector = pickle.load(pickle_in)
#
#     for url, vector_dict in url2description_vector.items():
#
#         url2descrip_vector[url] = vector_dict
#         sub_count+=1
#         if sub_count>12785:
#             count+=1
#             print(count)
#             store_name = "/home/ying/django_starter_project/ying/data/folder1/url2descrip_vector" + str(count)+'.pickle'
#             pickle_out = open(store_name, 'wb')
#             pickle.dump(url2descrip_vector, pickle_out)
#             print(len(url2descrip_vector))
#             count_num+=len(url2descrip_vector)
#             sub_count=0
#             url2descrip_vector={}
# print(count_num)
# if count_num < 839859:
#     store_name = "/home/ying/django_starter_project/ying/data/folder1/url2descrip_vector" + str(count+1) + '.pickle'
#     pickle_out = open(store_name, 'wb')
#     pickle.dump(url2descrip_vector, pickle_out)


# pickle_in = open("/home/ying/django_starter_project/ying/data/folder1/url2caption.pickle","rb")
# url2caption = pickle.load(pickle_in)
# count = 0
# count_num =0
# sub_url2caption = {}
# sub_count=0
# for url, caption in url2caption.items():
#     sub_url2caption[url] = caption
#     sub_count+=1
#     if sub_count == 420000:
#         count+=1
#         store_name = "/home/ying/django_starter_project/ying/data/folder1/url2caption"+ str(count) + '.pickle'
#         pickle_out = open(store_name, 'wb')
#         pickle.dump(sub_url2caption, pickle_out)
#         sub_count=0
#         count_num += len(sub_url2caption)
#         sub_url2caption ={}
#
# store_name = "/home/ying/django_starter_project/ying/data/folder1/url2caption"+ str(count+1) + '.pickle'
# pickle_out = open(store_name, 'wb')
# pickle.dump(sub_url2caption, pickle_out)
# count_num += len(sub_url2caption)
# print(count_num)


pickle_in = open("folder1/url2description.pickle","rb")
url2caption = pickle.load(pickle_in)
count = 0
count_num =0
sub_url2caption = {}
sub_count=0
for url, caption in url2caption.items():
    sub_url2caption[url] = caption
    sub_count+=1
    if sub_count == 420000:
        count+=1
        store_name = "folder1/url2caption"+ str(count) + '.pickle'
        pickle_out = open(store_name, 'wb')
        pickle.dump(sub_url2caption, pickle_out)
        sub_count=0
        count_num += len(sub_url2caption)
        sub_url2caption ={}

store_name = "folder1/url2caption"+ str(count+1) + '.pickle'
pickle_out = open(store_name, 'wb')
pickle.dump(sub_url2caption, pickle_out)
count_num += len(sub_url2caption)
print(count_num)