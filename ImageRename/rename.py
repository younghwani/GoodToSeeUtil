import os
from time import sleep

# 저장한 File의 name을 넣는다.
f_list = ['cheetos', 'chic_choc', 'custard', 'kancho', 'crunky_pepero', 'changgu', 'whale_rice',
           'turtle_chips', 'eye_potato', 'diget', 'nacho_cheese', 'peanut_gangjeong', 'swingchip_hot',
           'oh_potato', 'oddu', 'saddo_bob', 'kosomi', 'diget_choco']

def rename(path, willChangeName):
    i = 1
    for fileName in os.listdir(path):
        if (fileName != '.DS_Store'):
            print(f'{path + fileName} -> {path + str(willChangeName) + str(i)}.jpg')
            os.rename(path + fileName, path+str(willChangeName)+'_'+str(i)+'.jpg')
            # os.rename(path + fileName, path+str(willChangeName)+str(i)+'.jpg')
            sleep(0.1)
            i += 1

for idx in range(len(f_list)):
    rename('/Users/kyh/GitHub/ImageScrap/test/'+f_list[idx]+'/', f_list[idx])
    sleep(1)
