import qrcode
def generate_qr_code(data,filename):
    qr=qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=10,
                     border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill='black',back_color='white')
    img.save(filename + ".jpg")
data=input("Enter the qr information:")
filename=input("Enter the file name:")
generate_qr_code(data,filename)
print("QR code successfully created")