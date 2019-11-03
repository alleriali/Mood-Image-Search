import os
import spacy
import pickle,truecase
import re,time
from concurrent import futures
from nltk.stem import WordNetLemmatizer
from threading import Lock
activity_list = ['camping','hiking','picnic','photography','climbing','swimming','bungee jumping','parachute jumping','paragliding','riding','cycling','hockey','running','walking',
            'fishing','surfing','canoeing','skiing','skating','windsurfing','diving','shopping']
activ_list = ['camp', 'hike', 'picnic', 'photography', 'climb', 'swim', 'jump', 'paragliding', 'ride', 'cycle', 'hockey', 'run',
              'walk', 'fish', 'surf', 'canoe', 'ski', 'skate', 'windsurf', 'dive','shop']
nlp = spacy.load('en_core_web_lg')
lock = Lock()
lock1 = Lock()
lemmatizer = WordNetLemmatizer()
count =0
urls=[]
pickle_in = open('url2caption.pickle','rb')
url2caption = pickle.load(pickle_in)
# pickle_in = open('folder/rest_url_list.pickle','rb')
# urls = pickle.load(pickle_in)
url2description ={}
url2description_vector ={}

for url, caption in url2caption.items():
    urls.append(url)


def FindKeywords(input):
    #find entity ,non-entity, activity and their word embedding vectors
    entities = set([])
    entity_vector ={}
    non_entities = set([])
    non_entity_vector ={}
    activity = set([])
    activity_vector ={}
    doc = nlp(input)
    for entity in doc.ents:
        if entity.label_ == 'GPE' or entity.label_ == 'ORG' or entity.label_ == 'NORP' or entity.label_ == 'LOC':
            entities.add(entity.text)
            entity_vector[entity.text] = entity.vector

    for token in doc:
        word = re.sub("\S*\d\S*", "", token.text)
        if word=="" or len(word)==1:
            continue
        if len(token.text)==1:
            continue
        flag = False
        for entity in entities:
            if flag==True:
                break
            if token.text.lower() in entity.lower():
                flag = True
        if not flag:
            if token.is_stop != True and token.is_punct != True and token.like_num != True:
                lock1.acquire()
                tag = token.pos_
                if tag == "VERB":

                    lemmed = lemmatizer.lemmatize(token.text.lower(), 'v')
                    if lemmed in activ_list:
                        activity.add(lemmed)
                        activity_vector[lemmed] = nlp.vocab.get_vector(lemmed)
                else:
                    lemmed = token.lemma_.lower()
                    if lemmed in activity_list:
                        activity.add(lemmed)
                        activity_vector[lemmed] = nlp.vocab.get_vector(lemmed)
                    else:
                        non_entities.add(lemmed)
                        non_entity_vector[lemmed] = nlp.vocab.get_vector(lemmed)

                lock1.release()

    url2keywords = {}
    url2keywords['entity'] = entities
    url2keywords['non_entity'] = non_entities
    url2keywords['activity'] = activity
    url2keywords_vector={}
    url2keywords_vector['entity'] = entity_vector
    url2keywords_vector['non_entity'] = non_entity_vector
    url2keywords_vector['activity'] = activity_vector
    return url2keywords,url2keywords_vector

def preprocessing(instring):
    chars = ['.', '-', '&', '*', '/', '|','#']
    for char in chars:
        if char in instring:
            instring = instring.replace(char, " ")
    instring = " ".join(instring.split())
    #instring = re.sub("\S*\d\S*", "", instring).strip()
    return instring




def get_url2description_and_vectors(url):
    lock.acquire()
    global count
    count += 1
    caption = url2caption[url]
    lock.release()
    case_caption = truecase.get_true_case(caption)
    case_caption = preprocessing(case_caption)
    url2keywords, url2keywords_vector = FindKeywords(case_caption)
    lock.acquire()
    url2description[url] = url2keywords
    url2description_vector[url] = url2keywords_vector
    lock.release()

def store_data(count_num):
    count_num += 1
    pickle_name = 'folder1/' + 'url2description' + str(count_num) + '.pickle'
    pickle_out = open(pickle_name, 'wb')
    pickle.dump(url2description, pickle_out)
    pickle_out.close()
    pickle_vector_name = 'folder1/' + 'url2description_vector' + str(count_num) + '.pickle'
    pickle_out = open(pickle_vector_name, 'wb')
    pickle.dump(url2description_vector, pickle_out)
    pickle_out.close()

with futures.ThreadPoolExecutor(max_workers=12) as executor:
    future_result = executor.map(get_url2description_and_vectors, urls)
    lock.acquire()
    count_num=0
    while count != len(urls):
        if count/100000>count_num+1:
            print(count_num)
            print(count)
            store_data(count_num)
            url2description.clear()

            url2description_vector.clear()
            count_num+=1
        tmp = count
        lock.release()
        print(tmp, '/', len(urls))
        time.sleep(5)
        lock.acquire()
    lock.release()
    real_result = list(future_result)
    store_data(count_num)






