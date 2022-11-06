import cv2
import os
from imutils import paths
import shutil


def listNegative():
    imagePath = list(paths.list_images('imagens/n'))
    n = 1
    if not os.path.exists('n'):
        os.makedirs('n')

    for i in imagePath:
        # renomear a imagem
        i.replace(i, "n/"+str(n)+".png")

        # copiar a imagem com novo nome
        shutil.copy(i, i.replace(i, "n/"+str(n)+".png"))

        # realiza a leitura da imagem transformando ela em cinza
        img = cv2.imread("n/"+str(n)+".png", cv2.IMREAD_GRAYSCALE)

        # redimenciona o tamanho de todas para o mesmo padrão
        resized_image = cv2.resize(img, (38, 35))

        # cola as imagems com as alteracoes
        cv2.imwrite("n/"+str(n)+".png", resized_image)

        print(i.replace(i, "n/"+str(n)+".png"))

        n += 1


def listPositive():
    imagePath = list(paths.list_images('imagens/train'))
    n = 1
    if not os.path.exists('train'):
        os.makedirs('train')

    for i in imagePath:
        # renomear a imagem
        i.replace(i, "train/"+str(n)+".png")

        # copiar a imagem com novo nome
        shutil.copy(i, i.replace(i, "train/"+str(n)+".png"))

        # realiza a leitura da imagem transformando ela em cinza
        img = cv2.imread("train/"+str(n)+".png")

        # redimenciona o tamanho de todas para o mesmo padrão
        resized_image = cv2.resize(img, (28, 28))

        # cola as imagems com as alteracoes
        cv2.imwrite("train/"+str(n)+".png", resized_image)

        print(i.replace(i, "train/"+str(n)+".png"))

        n += 1

# listNegative()
listPositive()