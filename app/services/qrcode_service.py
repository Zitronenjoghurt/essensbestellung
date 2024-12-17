import qrcode
from PIL import Image


def generate_qr_code(kunden_id: int) -> str:
    # Predefined path to the assets/qrcodes folder
    output_dir = "assets"
    file_name = f"{kunden_id}.png"
    file_path = f"{output_dir}/{file_name}"

    # Generate the QR code
    kunden_qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    kunden_qr.add_data(kunden_id)
    kunden_qr.make(fit=True)
    kunden_qr_img = kunden_qr.make_image(fill_color='black', back_color='white')

    # Save the image to the specified path
    kunden_qr_img.save(file_path)

    return file_path