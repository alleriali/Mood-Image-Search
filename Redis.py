import redis,pickle,json
r = redis.Redis(health_check_interval=10)
# r.delete("Bahamas")
url2description_list1 = ['folder/url2description_vector1.pickle','folder/url2description_vector2.pickle','folder/url2description_vector3.pickle']
url2description_list2 = ['folder/url2description_vector4.pickle','folder/url2description_vector5.pickle','folder/url2description_vector6.pickle']
url2description_list3 = ['folder/url2description_vector7.pickle','folder/url2description_vector8.pickle',
                        'folder/url2description_vector9.pickle']
def WriteToRedis(url2des2vector):

    cnt = 0
    for url, des2vector in url2des2vector.items():
        des2vector_serialized = pickle.dumps(des2vector)
        r.hset(url, 'des2vector', des2vector_serialized)
        cnt += 1
        if cnt % 10000 == 0:
            print(cnt)

for url2des2vector_path in url2description_list2:
    pickle_in = open(url2des2vector_path,"rb")
    url2des2vector = pickle.load(pickle_in)
    WriteToRedis(url2des2vector)

def ReadUrlFromRedis(r, url):
    column = 'des2vector'
    des2vector_serialized = r.hget(url, column)
    des2vector = pickle.loads(des2vector_serialized)
    return des2vector

test_url = 'http://static.flickr.com/3067/2836609074_6eb2637de4.jpg'
print(ReadUrlFromRedis(r, test_url))

exit(0)



# stringified_dict = json.dumps(url2des2vector)
#r.hmset('url2description2vector', str(url2des2vector))
# print(list(url2des2vector.keys())[0])
# stringified_dict = json.dumps(url2des2vector)
# r.hmset('url2description2vector', stringified_dict)
