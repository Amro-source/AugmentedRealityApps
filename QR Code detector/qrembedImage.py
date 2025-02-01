import qrcode
from PIL import Image

def generate_qr_code_inside_image(data, image_size, qr_size, filename):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create a new image with a plain color
    img = Image.new('RGB', image_size, color='white')

    # Convert QR code to image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Resize QR code image
    qr_img = qr_img.resize(qr_size)

    # Calculate the position to paste the QR code
    pos = ((image_size[0] - qr_size[0]) // 2, (image_size[1] - qr_size[1]) // 2)

    # Paste the QR code onto the image
    img.paste(qr_img, pos)

    # Save the image
    img.save(filename)

# Example usage
data = "https://www.example.com"
image_size = (500, 500)
qr_size = (200, 200)
filename = "qrcode_inside_image.png"
generate_qr_code_inside_image(data, image_size, qr_size, filename)
