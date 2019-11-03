import pickle
pickle_in = open("url2caption1.pickle",'rb')
url2caption1 = pickle.load(pickle_in)
pickle_in = open("url2caption2.pickle",'rb')
url2caption2 = pickle.load(pickle_in)
pickle_in = open("url2caption3.pickle",'rb')
url2caption3 = pickle.load(pickle_in)
pickle_in = open("url2caption4.pickle",'rb')
url2caption4 = pickle.load(pickle_in)
pickle_in = open("url2caption5.pickle",'rb')
url2caption5 = pickle.load(pickle_in)
valid_url2caption =[url2caption1,url2caption2,url2caption3,url2caption4,url2caption5]
url2caption = {}
for dict in valid_url2caption:
    for url, caption in dict.items():
        url2caption[url] = caption

print(len(url2caption))

pickle_out = open("url2caption.pickle", 'wb')
pickle.dump(url2caption, pickle_out)
pickle_out.close()