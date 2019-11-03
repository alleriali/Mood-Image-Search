import pickle
import requests
from datetime import datetime
import time
from elasticsearch import Elasticsearch, helpers

my_index ="images_selection"
es = Elasticsearch()
# results = helpers.scan(es,index='images_selection',"explain": true,query={"query": {
#         "query_string" : {
#             "query" : "Laos flower",
#             "default_field": 'description'
#
#
#         }
#     }})
#
# for item in results:
#     print(item['_id'],item['_source'])



text2keywords={}
text2keywords['entity'] = ['Bahamas']
text2keywords['non_entity'] = []
text2keywords['activity'] = ['dive']
def GenerateQueryBody(input_list,tag):
    if tag=="activity":
        return [{"match": {tag: {"query":element,"boost":3}}} for element in input_list]
    else:
        return [{"match": {tag: element}} for element in input_list]
def GenerateQueryBody(element,tag):
    if tag == "activity":
        return {"match": {tag: {"query":element,"boost":2}}}
    else:
        return {"match": {tag: element}}
def QueryBody(text2keywords):
    body =[]
    for element in text2keywords['entity']:
        body.append(GenerateQueryBody(element,'entity'))
    for element in text2keywords['non_entity']:
        body.append(GenerateQueryBody(element,'non_entity'))
    for element in text2keywords['activity']:
        body.append(GenerateQueryBody(element,'activity'))
    return body

def elasticsearch(text2keywords):
    candidates=[]
    query_body = {
        "from": 0,
        "size": 20,
        "query": {
            "dis_max": {
                "queries": QueryBody(text2keywords),

                "tie_breaker": 0.7

            }}
    }
    return query_body
query_body1 = {
    "from": 0,
    "size": 20,
    "query": {
        "dis_max": {
            "queries": [
                {'match':{'entity':{'query':'Bahamas','boost':2}}},
                {'match':{'non_entity':{'query':'flower girl',"boost":1}}},
                {'match':{'activity':{"query":'diving','boost':3}}}
                # {'match':{'entity':'Bahamas'}},
                # {'match':{'non_entity':'flower girl'}},
                # {'match':{'activity':'diving'}}
                # {"query_string": {
                #     "query": " Bahamas",
                #     "fields": ['entity', 'non_entity']
                # }},
                # {"query_string": {
                #     "query": "",
                #     "fields": ['non_entity']
                # }
                # },
                # {"query_string": {
                #     "query": "diving",
                #     "fields": ['activity'],
                #     "boost": 2
                #
                # }
                # }],
                ],
            "tie_breaker": 0.7

        }}
}

#print(elasticsearch(text2keywords))
st =time.time()
result1 = es.search(index=my_index,  body=query_body1)
et = time.time()
print(et-st)
hits = result1["hits"]["hits"]
# counts =0
for hit in hits:
    print(hit['_source'])




#
# def es_iterate_all_documents(es, index, pagesize=250, scroll_timeout="1m", **kwargs):
#     """
#     Helper to iterate ALL values from a single index
#     Yields all the documents.
#     """
#     is_first = True
#     while True:
#         # Scroll next
#         if is_first: # Initialize scroll
#             result = es.search(index=index, scroll="1m", **kwargs, body=query_body1)
#             is_first = False
#         else:
#             result = es.scroll(body={
#                 "scroll_id": scroll_id,
#                 "scroll": scroll_timeout
#             })
#         scroll_id = result["_scroll_id"]
#         hits = result["hits"]["hits"]
#         # Stop after no more docs
#         if not hits:
#             break
#         # Yield each entry
#         yield from ([hit['_source'],hit['_score']]for hit in hits)
# st = time.time()
# counts =0
# for entry ,score in es_iterate_all_documents(es, my_index):
#     # if counts <20:
#     print(entry,score) # Prints the document as stored in the DB
#     # else:
#     #     break
#     counts+=1
# print(counts)
# et =time.time()
# print(et-st)
#print(es.search(index="images_selection",body=query_body))


