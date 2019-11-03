import pickle
import requests
import time
from elasticsearch import Elasticsearch, helpers
res = requests.get('http://localhost:9200')
print(res.content)
es = Elasticsearch()
#es.indices.delete(index="images_selection")


pickle_in = open('../../data/folder1//im2keywords.pickle','rb')
im2keywords = pickle.load(pickle_in)
pickle_large_in = open('folder1/url2description.pickle','rb')
url2description = pickle.load(pickle_large_in)


def insert_data(im2attributes):
    actions = [
        {
        "_index" : "images_selection",
        "_type" : "travelling",
        "_source":{ # the body of the image
                "directory" :im,
                "entity":list(keywords['entity']),
                "non_entity":list(keywords['non_entity']),
                "activity": list(keywords['activity'])
            }

        }
    for im,keywords in im2attributes.items()
    ]

    helpers.bulk(es,actions)



st = time.time()
insert_data(im2keywords)
et = time.time()
used_time = et-st
print(used_time)


st = time.time()
insert_data(url2description)
et = time.time()
used_time = et-st
print(used_time)





results = helpers.scan(es,index='images_selection',query={"query":{"match_all":{}}})
for item in results:
    print(item['_id'],item['_source'])