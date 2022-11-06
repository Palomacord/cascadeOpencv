import cv2
import imutils
import os

pasta = 'p'
if not os.path.exists(pasta):
	os.makedirs(pasta)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 300, 120
x2, y2 = 600, 400

count = 193
while True:

	ret, frame = cap.read()
	if ret == False:  break
	imAux = frame.copy()
	cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

	objeto = imAux[y1:y2,x1:x2]
	objeto = imutils.resize(objeto, width=38)
	n=0

	k = cv2.waitKey(1)
	if k == ord('s'):
		n +=1
		cv2.imwrite(pasta+str(n)+'.jpg'.format(count),objeto)
		print('Imagem: ',str(n)+ '.jpg'.format(count))
		count = count + 1
	if k ==ord('q'):
		break

	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()