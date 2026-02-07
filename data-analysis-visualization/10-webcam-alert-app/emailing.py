import smtplib
from config import SENDER, RECEIVER, PASSWORD
from email.message import EmailMessage
from PIL import Image
import io


def send_email(image_path):
    gmail = None

    try:
        email_message = EmailMessage()
        email_message["Subject"] = "New Customer Showed Up!!!"
        email_message["From"] = SENDER
        email_message["To"] = RECEIVER
        email_message.set_content("Hey, We Just Saw a New Customer")

        # Baca image sebagai bytes
        with open(image_path, "rb") as file:
            image_bytes = file.read()

        # Deteksi format image pakai Pillow
        image = Image.open(io.BytesIO(image_bytes))
        image_format = image.format.lower()  # jpeg, png, webp, dll

        email_message.add_attachment(
            image_bytes,
            maintype="image",
            subtype=image_format,
            filename=f"image.{image_format}"
        )

        # Kirim email
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.send_message(email_message)

        print("✅ Email is sent")

    except FileNotFoundError:
        print("❌ Image file not found")

    except Image.UnidentifiedImageError:
        print("❌ File is not a valid image")

    except smtplib.SMTPAuthenticationError:
        print("❌ SMTP authentication failed")

    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    finally:
        if gmail:
            gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/1.png")
    # pass
