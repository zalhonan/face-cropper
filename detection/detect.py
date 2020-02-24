import cv2


def detect(input_image):

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # # Read the input image
    # img = cv2.imread(input_image)
    # Convert into grayscale
    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # возврат результатов в формате [[x, y, w, h], [x, y, w, h]]
    return faces
