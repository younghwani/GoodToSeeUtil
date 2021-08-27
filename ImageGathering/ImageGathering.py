import cv2
import os

videoPath = './VideoFile/'
imagePath = './images/'
file_list = os.listdir(videoPath)

for file in file_list:
    try:
        if not (os.path.isdir(videoPath + file)):
            os.makedirs(os.path.join(imagePath + file))

            cap = cv2.VideoCapture(videoPath + file)

            count = 0

            while True:
                ret, image = cap.read()

                if not ret:
                    break

                cv2.imwrite(imagePath + file + "/frame%d.jpg" % count, image)

                print('%d.jpg done' % count)
                count += 1

            cap.release()

    except OSError as e:
        if e.errno != e.EEXIST:
            print("Failed to create directory!!!!!")
            raise