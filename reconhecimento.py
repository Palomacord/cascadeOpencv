import cv2
webcamera = cv2.VideoCapture(0)
carregarCascade = cv2.CascadeClassifier('classifier/cascade-15v.xml')
while True:
    camera, img = webcamera.read()
    cv2.imshow("web", img)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    box = carregarCascade.detectMultiScale(imgGray, scaleFactor=1.3, minNeighbors=2)
    print(box)
    for (x,y,l,a) in box:
        cv2.rectangle(img, (x,y), (x+l, y+a), (0,255,0), 2)
        cv2.putText(img, 'Caixa', (x, y - 10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Caixas", img)
    if cv2.waitKey(1)==ord('q'):
        break


