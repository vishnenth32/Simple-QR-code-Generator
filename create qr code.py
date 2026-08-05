import qrcode

data="  Enter the details which you need to print in qr (link, text etc) "

qr=qrcode.make(data)

qr.save("qrcode.png")

print("qr code is printed successfully")
