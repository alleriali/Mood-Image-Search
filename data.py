import pickle
# pickle_in = open('/home/ying/Documents/VM2/keywordsforelastic.pickle','rb')
# im2ents,im2nonents,im2keywords = pickle.load(pickle_in)
# im2entnonent ={}
# for im, toekns in im2ents.items():
#     keywords ={}
#     keywords['entity'] = toekns
#     keywords['non_entity'] = im2nonents[im]
#
#     im2entnonent[im] = keywords




# url2description={}
#
# for i in range(1,10):
#     print(i)
#     pickle_name = 'folder1/url2description'+str(i)+'.pickle'
#     pickle_in = open(pickle_name, 'rb')
#     sub_url2description= pickle.load(pickle_in)
#     for im, description in sub_url2description.items():
#         url2description[im] = description
# pickle_out = open("folder1/url2description.pickle","wb")
# pickle.dump(url2description,pickle_out)
# pickle_out.close()



import spacy
nlp = spacy.load('en_core_web_lg')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
activity_list = ['camping', 'hiking', 'picnic', 'photography', 'climbing', 'swimming', 'bungee jumping',
                 'parachute jumping', 'paragliding', 'riding', 'cycling', 'hockey', 'running', 'walking',
                 'fishing', 'surfing', 'canoeing', 'skiing', 'skating', 'windsurfing', 'diving', 'shopping']

# pickle_in = open('/home/ying/Documents/VM2/im2keywords.pickle','rb')
#
# im2keywords = pickle.load(pickle_in)
# pickle_in = open('/home/ying/Documents/VM2/im2keywords_vector.pickle','rb')
#
# im2keywords_vector = pickle.load(pickle_in)
#
# for im, dict in im2keywords.items():
#
#     set2list =  list(dict['activity'])
#     for act in set2list:
#         if act in activity_list:
#             print(im)
#             new_act = lemmatizer.lemmatize(act, 'v')
#             set2list[set2list.index(act)] = new_act
#             del im2keywords_vector[im]['activity'][act]
#             im2keywords_vector[im]['activity'][new_act]= nlp.vocab.get_vector(new_act)
#     dict['activity'] = set(set2list)
#
#
#

# for im , dict in im2keywords_vector.items():
#     if len(dict['activity'] )>0:
#         print(dict['activity'])
#
# pickle_out = open('/home/ying/Documents/VM2/im2keywords.pickle','wb')
# pickle.dump(im2keywords,pickle_out)
# pickle_out = open('/home/ying/Documents/VM2/im2keywords_vector.pickle','wb')
# pickle.dump(im2keywords_vector,pickle_out)


pickle_in = open("folder1/url2description.pickle","rb")

url2description = pickle.load(pickle_in)

def UpdateVectors(update_dict):


    for i in range(1,10):
        pickle_name = 'folder1/url2description_vector'+str(i)+'.pickle'
        pickle_in = open(pickle_name, 'rb')
        sub_url2description_vector= pickle.load(pickle_in)
        for im ,vector_dict in sub_url2description_vector.items():
            if im in update_dict:
                for i, act in enumerate(update_dict[im]['old']):
                    del sub_url2description_vector[im]['activity'][act]
                    new_act = update_dict[im]['new'][i]
                    sub_url2description_vector[im]['activity'][new_act]= nlp.vocab.get_vector(new_act)
        pickle_out = open(pickle_name,'wb')
        pickle.dump(sub_url2description_vector,pickle_out)



update_dict = {}

for im, dict in url2description.items():

    set2list =  list(dict['activity'])
    old =[]
    new =[]
    for act in set2list:
        if act in activity_list:
            # print(act)
            old.append(act)
            new_act = lemmatizer.lemmatize(act, 'v')
            new.append(new_act)
            set2list[set2list.index(act)] = new_act

            # update_dict[im] = {'old':act,"new":new_act}
    if len(old)>0:
        update_dict[im] = {'old': old, "new": new}
        print(set2list)
    dict['activity'] = set(set2list)

pickle_out = open("folder1/url2description.pickle","wb")
pickle.dump(url2description,pickle_out)

UpdateVectors(update_dict)

