import qrcode
import secrets
import string
import os


def get_qr(user_id):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(password)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'./data/{user_id}qrcode.jpg', 'JPEG')
    photo = open (
        f'./data/{user_id}qrcode.jpg',
        'rb'
    )

    return photo


def delete_user_qr(user_id):
    path = os.path.join(f"./data/{user_id}qrcode.jpg")
    os.remove(path)
