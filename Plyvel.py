import plyvel,pickle
url2description_list1 = ['folder/url2description_vector1.pickle','folder/url2description_vector2.pickle','folder/url2description_vector3.pickle']
url2description_list2 = ['folder/url2description_vector4.pickle','folder/url2description_vector5.pickle','folder/url2description_vector6.pickle']
url2description_list3 = ['folder/url2description_vector7.pickle','folder/url2description_vector8.pickle',
                        'folder/url2description_vector9.pickle']
#db = plyvel.DB('/tmp/testdb/', create_if_missing=True)
def WriteToRedis(url2des2vector):
    count = 0
    wb = db.write_batch()
    for url, des2vector in url2des2vector.items():
        count += 1
        des2vector_serialized = pickle.dumps(des2vector)
        if count > 60000:
            wb.put(b'url', des2vector_serialized)
        if count % 100 == 0:
            wb.write()
            print(count)
    # with db.write_batch() as wb:
    #     for url, des2vector in url2des2vector.items():
    #         des2vector_serialized = pickle.dumps(des2vector)
    #         wb.put(b'url', des2vector_serialized)


#
# for url2des2vector_path in url2description_list1:
#     pickle_in = open(url2des2vector_path, "rb")
#     url2des2vector = pickle.load(pickle_in)
#     WriteToRedis(url2des2vector)

test_url = 'http://static.flickr.com/3067/2836609074_6eb2637de4.jpg'
db = plyvel.DB('/tmp/testdb_2/', create_if_missing=True)

db.put(b'http://static.flickr.com/3067/2836609074_6eb2637de4.jpg', b'value')
print(db.get(b'http://static.flickr.com/3067/2836609074_6eb2637de4.jpg'))