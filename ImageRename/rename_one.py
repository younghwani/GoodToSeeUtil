import os
from time import sleep

def rename(path, new_path, willChangeName):
    i = 1
    for fileName in os.listdir(path):
        if (fileName != '.DS_Store'):
            print(f'{path + fileName} -> {new_path + str(willChangeName) + str(i)}.jpg')
            os.rename(path + fileName, new_path+str(willChangeName)+'_'+str(i)+'.jpg')
            # os.rename(path + fileName, path+str(willChangeName)+str(i)+'.jpg')
            # sleep(0.1)
            i += 1

rename('/Users/kyh/GitHub/Yolov3Tiny/custom/ImageRename/need_labeling/',
       '/Users/kyh/GitHub/Yolov3Tiny/custom/ImageRename/ok/',
       'multi')
