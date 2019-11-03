# Import requests, shutil python module.
import requests
import shutil
import io,pickle
import urllib.request
from multiprocessing import Pool
from concurrent import futures
from urllib.error import URLError, HTTPError
from PIL import Image
from threading import Lock, Thread
from socket import timeout
import time
import datetime

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return width*height

pickle_in = open("url2captionORIGINAL.pickle",'rb')
url2captionORIGINAL = pickle.load(pickle_in)
url2caption ={}
filepath = '/home/ying/Downloads/SBUCaptionedPhotoDataset/dataset/SBU_captioned_photo_dataset_urls.txt'
urllists1 =[]
urllists2 =[]
urllists3 =[]
urllists4 =[]
urllists5 =[]
validurls =[]
url_list =[urllists1,urllists2,urllists3,urllists4,urllists5]
pickle_list = ['url2caption1.pickle','url2caption2.pickle','url2caption3.pickle','url2caption4.pickle','url2caption5.pickle']
count = 0
lock = Lock()
with open(filepath) as fp:
    url_count =0
    for cnt, line in enumerate(fp):
        url = line.strip('\n')
        if url_count <20:
            urllists1.append(url)

        if url_count >= 20 and url_count < 40:
            urllists2.append(url)

        if url_count >= 40 and url_count < 60:
            urllists3.append(url)

        if url_count >= 60 and url_count < 80:
            urllists4.append(url)

        if url_count >= 800000:
            urllists5.append(url)
        url_count+=1
print(len(urllists1),len(urllists2),len(urllists3),len(urllists4),len(urllists5))
fp.close()
def get_valid_images(url):
    lock.acquire()
    global count
    count += 1
    lock.release()
    try:
        f = urllib.request.urlopen(url,timeout=10)
    except HTTPError as e:
        pass
        #print('The server couldn\'t fulfill the request.')
        #print('Error code: ', e.code)
    except URLError as e:
        pass
        #print('We failed to reach a server.')
        #print('Reason: ', e.reason)
    except timeout:
        pass
    except:
        pass
    else:
        b = io.BytesIO(f.read())
        im = Image.open(b)
        width, height = im.size
        #print(width, height)
        if width * height > 300 * 500:
            lock.acquire()
            validurls.append(url)
            lock.release()

def parallel(urllists,pick_name):
    count = 0
    with futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(get_valid_images, urllists)

        lock.acquire()
        while count != len(urllists):
            tmp = count
            lock.release()
            print(tmp, '/', len(urllists))
            time.sleep(5)
            lock.acquire()
        lock.release()
    for url in validurls:
        url2caption[url] = url2captionORIGINAL[url]
    print(len(url2caption))
    pickle_out = open(pick_name, 'wb')
    pickle.dump(url2caption, pickle_out)
    pickle_out.close()
    validurls.clear()
    url2caption.clear()


for i in range(5):
    parallel(url_list[i],pickle_list[i] )
    print("finish",(i+1)*200000)



# image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"
# # Open the url image, set stream to True, this will return the stream content.
# resp = requests.get(image_url, stream=True)
# # Open a local file with wb ( write binary ) permission.
# local_file = open('local_image.jpg', 'wb')
# # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
# resp.raw.decode_content = True
# # Copy the response stream raw data to local image file.
# shutil.copyfileobj(resp.raw, local_file)
# # Remove the image url response object.
# del resp