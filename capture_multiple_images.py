import cv2

cam1 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.1:80/video/mjpg.cgi')
cam2 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.2:80/video/mjpg.cgi')
cam3 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.3:80/video/mjpg.cgi')
cam4 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.4:80/video/mjpg.cgi')
cam5 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.5:80/video/mjpg.cgi')
cam6 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.6:80/video/mjpg.cgi')
cam7 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.7:80/video/mjpg.cgi')
cam8 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.8:80/video/mjpg.cgi')
cam9 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.9:80/video/mjpg.cgi')
cam10 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.10:80/video/mjpg.cgi')
cam11 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.11:80/video/mjpg.cgi')
cam12 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.12:80/video/mjpg.cgi')
cam13 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.13:80/video/mjpg.cgi')
cam14 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.14:80/video/mjpg.cgi')
cam15 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.15:80/video/mjpg.cgi')

cam16 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.16:80/video/mjpg.cgi')
cam17 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.17:80/video/mjpg.cgi')
cam18 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.18:80/video/mjpg.cgi')
cam19 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.19:80/video/mjpg.cgi')
cam20 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.20:80/video/mjpg.cgi')
cam21 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.21:80/video/mjpg.cgi')
cam22 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.22:80/video/mjpg.cgi')
cam23 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.23:80/video/mjpg.cgi')
cam24 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.24:80/video/mjpg.cgi')
cam25 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.25:80/video/mjpg.cgi')
cam26 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.26:80/video/mjpg.cgi')
cam27 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.27:80/video/mjpg.cgi')
cam28 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.28:80/video/mjpg.cgi')
cam29 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.29:80/video/mjpg.cgi')
cam30 = cv2.VideoCapture('http://admin:nnsaja@192.168.0.30:80/video/mjpg.cgi')




cv2.namedWindow("test1")
cv2.namedWindow("test2")
cv2.namedWindow("test3")
cv2.namedWindow("test4")
cv2.namedWindow("test5")
cv2.namedWindow("test6")
cv2.namedWindow("test7")
cv2.namedWindow("test8")
cv2.namedWindow("test9")
cv2.namedWindow("test10")
cv2.namedWindow("test11")
cv2.namedWindow("test12")
cv2.namedWindow("test13")
cv2.namedWindow("test14")
cv2.namedWindow("test15")

cv2.namedWindow("test16")
cv2.namedWindow("test17")
cv2.namedWindow("test18")
cv2.namedWindow("test19")
cv2.namedWindow("test20")
cv2.namedWindow("test21")
cv2.namedWindow("test22")
cv2.namedWindow("test23")
cv2.namedWindow("test24")
cv2.namedWindow("test25")
cv2.namedWindow("test26")
cv2.namedWindow("test27")
cv2.namedWindow("test28")
cv2.namedWindow("test29")
cv2.namedWindow("test30")




img_counter = 0

while True:
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    ret3, frame3 = cam3.read()
    ret4, frame4 = cam4.read()
    ret5, frame5 = cam5.read()
    ret6, frame6 = cam6.read()
    ret7, frame7 = cam7.read()
    ret8, frame8 = cam8.read()
    ret9, frame9 = cam9.read()
    ret10, frame10 = cam10.read()
    ret11, frame11 = cam11.read()
    ret12, frame12 = cam12.read()
    ret13, frame13 = cam13.read()
    ret14, frame14 = cam14.read()
    ret15, frame15 = cam15.read()

    ret16, frame16 = cam16.read()
    ret17, frame17 = cam17.read()
    ret18, frame18 = cam18.read()
    ret19, frame19 = cam19.read()
    ret20, frame20 = cam20.read()
    ret21, frame21 = cam21.read()
    ret22, frame22 = cam22.read()
    ret23, frame23 = cam23.read()
    ret24, frame24 = cam24.read()
    ret25, frame25 = cam25.read()
    ret26, frame26 = cam26.read()
    ret27, frame27 = cam27.read()
    ret28, frame28 = cam28.read()
    ret29, frame29 = cam29.read()
    ret30, frame30 = cam30.read()

    if not ret1:
        print("failed to grab frame0")
        break

    cv2.imshow("test1", frame1)
    cv2.imshow("test2", frame2)
    cv2.imshow("test3", frame3)
    cv2.imshow("test4", frame4)
    cv2.imshow("test5", frame5)
    cv2.imshow("test6", frame6)
    cv2.imshow("test7", frame7)
    cv2.imshow("test8", frame8)
    cv2.imshow("test9", frame9)
    cv2.imshow("test10", frame10)
    cv2.imshow("test11", frame11)
    cv2.imshow("test12", frame12)
    cv2.imshow("test13", frame13)
    cv2.imshow("test14", frame14)
    cv2.imshow("test15", frame15)

    cv2.imshow("test16", frame16)
    cv2.imshow("test17", frame17)
    cv2.imshow("test18", frame18)
    cv2.imshow("test19", frame19)
    cv2.imshow("test20", frame20)
    cv2.imshow("test21", frame21)
    cv2.imshow("test22", frame22)
    cv2.imshow("test23", frame23)
    cv2.imshow("test24", frame24)
    cv2.imshow("test25", frame25)
    cv2.imshow("test26", frame26)
    cv2.imshow("test27", frame27)
    cv2.imshow("test28", frame28)
    cv2.imshow("test29", frame29)
    cv2.imshow("test30", frame30)


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name1 = "opencv_frame1_{}.jpeg".format(img_counter)
        img_name2 = "opencv_frame2_{}.jpeg".format(img_counter)
        img_name3 = "opencv_frame3_{}.jpeg".format(img_counter)
        img_name4 = "opencv_frame4_{}.jpeg".format(img_counter)
        img_name5 = "opencv_frame5_{}.jpeg".format(img_counter)
        img_name6 = "opencv_frame6_{}.jpeg".format(img_counter)
        img_name7 = "opencv_frame7_{}.jpeg".format(img_counter)
        img_name8 = "opencv_frame8_{}.jpeg".format(img_counter)
        img_name9 = "opencv_frame9_{}.jpeg".format(img_counter)
        img_name10 = "opencv_frame10_{}.jpeg".format(img_counter)
        img_name11 = "opencv_frame11_{}.jpeg".format(img_counter)
        img_name12 = "opencv_frame12_{}.jpeg".format(img_counter)
        img_name13 = "opencv_frame13_{}.jpeg".format(img_counter)
        img_name14 = "opencv_frame14_{}.jpeg".format(img_counter)
        img_name15 = "opencv_frame15_{}.jpeg".format(img_counter)

        img_name16 = "opencv_frame16_{}.jpeg".format(img_counter)
        img_name17 = "opencv_frame17_{}.jpeg".format(img_counter)
        img_name18 = "opencv_frame18_{}.jpeg".format(img_counter)
        img_name19 = "opencv_frame19_{}.jpeg".format(img_counter)
        img_name20 = "opencv_frame20_{}.jpeg".format(img_counter)
        img_name21 = "opencv_frame21_{}.jpeg".format(img_counter)
        img_name22 = "opencv_frame22_{}.jpeg".format(img_counter)
        img_name23 = "opencv_frame23_{}.jpeg".format(img_counter)
        img_name24 = "opencv_frame24_{}.jpeg".format(img_counter)
        img_name25 = "opencv_frame25_{}.jpeg".format(img_counter)
        img_name26 = "opencv_frame26_{}.jpeg".format(img_counter)
        img_name27 = "opencv_frame27_{}.jpeg".format(img_counter)
        img_name28 = "opencv_frame28_{}.jpeg".format(img_counter)
        img_name29 = "opencv_frame29_{}.jpeg".format(img_counter)
        img_name30 = "opencv_frame30_{}.jpeg".format(img_counter)
        
        cv2.imwrite(img_name1, frame1)
        cv2.imwrite(img_name2, frame2)
        cv2.imwrite(img_name3, frame3)
        cv2.imwrite(img_name4, frame4)
        cv2.imwrite(img_name5, frame5)
        cv2.imwrite(img_name6, frame6)
        cv2.imwrite(img_name7, frame7)
        cv2.imwrite(img_name8, frame8)
        cv2.imwrite(img_name9, frame9)
        cv2.imwrite(img_name10, frame10)
        cv2.imwrite(img_name11, frame11)
        cv2.imwrite(img_name12, frame12)
        cv2.imwrite(img_name13, frame13)
        cv2.imwrite(img_name14, frame14)
        cv2.imwrite(img_name15, frame15)

        cv2.imwrite(img_name16, frame16)
        cv2.imwrite(img_name17, frame17)
        cv2.imwrite(img_name18, frame18)
        cv2.imwrite(img_name19, frame19)
        cv2.imwrite(img_name20, frame20)
        cv2.imwrite(img_name21, frame21)
        cv2.imwrite(img_name22, frame22)
        cv2.imwrite(img_name23, frame23)
        cv2.imwrite(img_name24, frame24)
        cv2.imwrite(img_name25, frame25)
        cv2.imwrite(img_name26, frame26)
        cv2.imwrite(img_name27, frame27)
        cv2.imwrite(img_name28, frame28)
        cv2.imwrite(img_name29, frame29)
        cv2.imwrite(img_name30, frame30)

        print("{} written!".format(img_name1))
        
        img_counter += 5

cam1.release()
cam2.release()
cam3.release()
cam4.release()
cam5.release()
cam6.release()
cam7.release()
cam8.release()
cam9.release()
cam10.release()
cam11.release()
cam12.release()
cam13.release()
cam14.release()
cam15.release()

cam16.release()
cam17.release()
cam18.release()
cam19.release()
cam20.release()
cam21.release()
cam22.release()
cam23.release()
cam24.release()
cam25.release()
cam26.release()
cam27.release()
cam28.release()
cam29.release()
cam30.release()

cv2.destroyAllWindows()
