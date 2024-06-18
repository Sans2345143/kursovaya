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