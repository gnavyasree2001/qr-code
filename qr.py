import qrcode
data="www.msrit.edu"
qr=qrcode.QRCode(
    version = 5,
    box_size=5,
    border=3,

)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='purple')
img.save('hello.png')
img.show()
