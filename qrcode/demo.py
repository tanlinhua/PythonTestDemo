import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.baidu.com')

qr.make(fit=True)
img = qr.make_image()
filename = 'qrcode_dome.png'
img.save(filename)
img.show()
