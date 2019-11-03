import random
import pickle,re,os
# path = ['folder/url2description1.pickle','folder/url2description2.pickle','folder/url2description3.pickle','folder/url2description4.pickle','folder/url2description5.pickle',
#         'folder/url2description6.pickle']
# vector_path = ['folder/url2description_vector1.pickle','folder/url2description_vector2.pickle'
# ]
# url2description ={}
# url2description_vector={}
# def assemble(directory,dict):
#     for file in directory:
#
#         pickle_in = open(file, 'rb')
#         url2description_branch = pickle.load(pickle_in)
#         print(len(url2description_branch))
#         for url, description in url2description_branch.items():
#             dict[url] = description
# assemble(path,url2description)
# assemble(vector_path,url2description_vector)
# print(len(url2description))
# print(len(url2description_vector))
# pickle_out = open("folder/url2description.pickle","wb")
# pickle.dump(url2description, pickle_out)
# pickle_out.close()
# pickle_out = open("folder/url2description_vector.pickle","wb")
# pickle.dump(url2description_vector, pickle_out)
# pickle_out.close()


# chars = ['.','-','&','*','/','#']
# instring = '2000.jpg'
# instring = re.sub("\S*\d\S*", "", instring)
# if instring=="":
#     print("yes")
# # instring = " ".join(instring.split())
# print(instring)
#
# count_num = 1
# pickle_name = 'folder/' + 'url2description' + str(count_num) + '.pickle'
# print(pickle_name)
# print(os.path.getsize(vector_path[5]))
# pickle_in = open(vector_path[5], 'rb')
# url2description_branch = pickle.load(pickle_in)
# print(len(url2description_branch))


# file_path = ["folder/rurl2description1.pickle","folder/rurl2description2.pickle","folder/rurl2description3.pickle"]
# file_path_vector = ['folder/url2description_vector1.pickle','folder/url2description_vector2.pickle','folder/url2description_vector3.pickle','folder/url2description_vector4.pickle',
#                'folder/url2description_vector5.pickle',"folder/rurl2description_vector1.pickle","folder/rurl2description_vector2.pickle","folder/rurl2description_vector3.pickle","folder/6rurl2description_vector1.pickle"]
# file_path_vector_change = ["folder/rurl2description_vector1.pickle","folder/rurl2description_vector2.pickle","folder/rurl2description_vector3.pickle","folder/6rurl2description_vector1.pickle"]

# pickle_in = open('folder/url2description.pickle','rb')
# url2description = pickle.load(pickle_in)
#
# url2description_vector = {}
# for path in file_path:
#     pickle_in = open(path, 'rb')
#     rurl2description = pickle.load(pickle_in)
#     for url, description in rurl2description.items():
#         url2description[url] = description
#
# print(len(url2description))
# pickle_out = open('folder/url2description.pickle','wb')
# pickle.dump(url2description,pickle_out)
#
# pickle_in = open("url2caption.pickle","rb")
# url2caption = pickle.load(pickle_in)
# print(len(url2caption))
# url2description_vector_branch1 ={}


# size = 0
# for path in file_path_vector:
#     pickle_in = open(path, 'rb')
#     url2description_vector_branch = pickle.load(pickle_in)
#     print(len(url2description_vector_branch))
#     size +=len(url2description_vector_branch)
#
# print(size)


# index = 6
# for path in file_path_vector_change:
#     pickle_in = open(path, 'rb')
#     url2description_vector_branch = pickle.load(pickle_in)
#     print(len(url2description_vector_branch))
#     pickle_name = "folder/url2description_vector" + str(index) +".pickle"
#     pickle_out = open(pickle_name,"wb")
#     pickle.dump(url2description_vector_branch,pickle_out)
#     index+=1


# print(len(url2description))
# print(len(url2description_vector_branch1))
# pickle_out = open('folder/url2description_vector_branch1.pickle','wb')
# pickle.dump(url2description_vector,pickle_out)


#print(os.path.getsize("folder/url2description_vector.pickle"))
# url2description_vector_path = ['folder/url2description_vector1.pickle','folder/url2description_vector2.pickle','folder/url2description_vector3.pickle',
# 'folder/url2description_vector4.pickle','folder/url2description_vector5.pickle','folder/url2description_vector6.pickle',
# 'folder/url2description_vector7.pickle','folder/url2description_vector8.pickle',
#                         'folder/url2description_vector9.pickle']
# url2description_vector = {}
# for path in url2description_vector_path:
#
#
#     pickle_large_in = open(path,'rb')
#     url2description_branch = pickle.load(pickle_large_in)
#     for url, vectors in url2description_branch.items():
#         url2description_vector[url] =vectors
#
# print(1)
# pickle_out = open("folder/url2description_vector.pickle","wb", buffering=4096)
# pickle.dump(url2description_vector,pickle_out)
# pickle_out.close()

# pickle_in  = open("url2caption.pickle",'rb')
# url2caption = pickle.load(pickle_in)
# print(len(url2caption))


