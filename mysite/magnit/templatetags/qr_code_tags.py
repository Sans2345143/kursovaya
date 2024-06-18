import io
import base64
from django import template
import qrcode

register = template.Library()

@register.filter(name='qr_code_filter')
def qr_code_filter(unique_id):
    img_data = io.BytesIO()
    generate_qr_code_from_unique_id(unique_id)
    img_data.seek(0)
    qr_code_base64 = base64.b64encode(img_data.read()).decode('utf-8')
    return f'data:image/png;base64,{qr_code_base64}'

def generate_qr_code_from_unique_id(unique_id):
    # Generate QR code image data using the unique_id (implement logic here)
    # Example using qrcode library:
    qr = qrcode.QRCode(
        version=1,  # Adjust version as needed
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Choose error correction level
        box_size=10,  # Adjust box size for image resolution
        border=4,  # Adjust border width
    )
    qr.add_data(unique_id)  # Add unique_id data
    qr.make(fit=True)  # Generate QR code matrix
    img = qr.make_image(fill_color='black', back_color='white')  # Create the image

    # Write the image data to the BytesIO object
    img_data.seek(0)  # Ensure buffer is at the beginning
    img.save(img_data, format='PNG')  # Save image to buffer