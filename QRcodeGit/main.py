import cv2
from qrcode import QRCode
from pyzbar.pyzbar import decode

color = (0, 0, 255) #цвет выделения полигона

try:
    stream = cv2.VideoCapture(0) #захват изображения с нужной нам камеры

    while True:
        ret, img = stream.read() #чтение изображения

        for decode_image in decode(img): #распаковка массива
            decode_image = decode_image
            #Создание класса qr_code
            qr_code = QRCode(
                decode_image.data,
                decode_image.rect,
                decode_image.polygon,
                decode_image.quality,
                decode_image.orientation)

            print(qr_code.get_data()) #print данных

            #оформление
            cv2.polylines(img, [qr_code.get_polygon()], True, color, 4) #полигон

            #отрисовка текста
            cv2.putText(img, qr_code.get_data(),
                        (qr_code.rect[0], qr_code.rect[2]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, color)

        #отображение изображения
        cv2.imshow('frame', img)

        #waitKey(1) обновляет изображения с камеры каждую миллисекунду, время можно изменить
        #0xFF == ord('q') - просто кнопка, по нажатию на которую происходит выход

        if cv2.waitKey(1) & 0xFF == ord('q'):
            stream.release() #это особенности библиотеки, не обязательно вдаваться, но нужно писать в конце
            cv2.destroyAllWindows() #Уничтожает все открытые окна
            break

#обработка возможных ошибок
except KeyboardInterrupt:
    stream.release()
    cv2.destroyAllWindows()
    print('Работа приложения прервана')

except MemoryError:
    stream.release()
    cv2.destroyAllWindows()
    print('Память переполнена')

#выполниться в любом случае
finally:
    stream.release()
    cv2.destroyAllWindows()
    print('Приложение отработало')






