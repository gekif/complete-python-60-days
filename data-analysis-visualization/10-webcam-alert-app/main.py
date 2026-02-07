import glob
import os
from threading import Thread
import cv2
import time
from emailing import send_email

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(1)

first_frame = None
status_list = []
count = 1
image_with_object = None


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        try:
            os.remove(image)
        except PermissionError:
            pass
    print("Clean folder finished")


def send_email_and_cleanup(image_path):
    send_email(image_path)
    clean_folder()


while True:
    status = 0
    check, frame = video.read()
    if not check:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(
        dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        status = 1
        cv2.imwrite(f"images/{count}.png", frame)
        count += 1

        all_images = glob.glob("images/*.png")
        if all_images:
            image_with_object = all_images[len(all_images) // 2]

    status_list.append(status)
    status_list = status_list[-2:]

    # OBJECT LEAVES FRAME → SEND EMAIL ONCE
    if len(status_list) == 2 and status_list[0] == 1 and status_list[1] == 0:
        if image_with_object:
            Thread(
                target=send_email_and_cleanup,
                args=(image_with_object,),
                daemon=True
            ).start()

            image_with_object = None  # reset supaya tidak spam

    cv2.imshow("My Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
