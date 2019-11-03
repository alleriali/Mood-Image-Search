import pickle
filepath = '/home/ying/Downloads/SBUCaptionedPhotoDataset/dataset/SBU_captioned_photo_dataset_urls.txt'
captionpath = '/home/ying/Downloads/SBUCaptionedPhotoDataset/dataset/SBU_captioned_photo_dataset_captions.txt'
url2caption ={}
count=0
with open(filepath) as fp:
    fcap = open(captionpath)
    cap_line = fcap.read().split('\n')
    for cnt, line in enumerate(fp):
        url = line.strip('\n')

        caption= cap_line[cnt]
        url2caption[url] = caption
        count+=1
        print(count,caption)
fp.close()
fcap.close()
print(count)
pickle_out = open("url2captionORIGINAL.pickle","wb")
pickle.dump(url2caption,pickle_out)
pickle_out.close()