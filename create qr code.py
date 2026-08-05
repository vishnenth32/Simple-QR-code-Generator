import qrcode

data="hello , this is a way to create a qr code in simple "

qr=qrcode.make(data)

qr.save("qrcode.png")

print("qr code is printed successfully")