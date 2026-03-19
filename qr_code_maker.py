import qrcode

url = input("Enter the URL to generate QR code: ").strip()
qr_name = input("Give a name for the QR code image: ")

qr = qrcode.QRCode()
file_path = "C:\\Users\\gerri\\OneDrive\\Desktop\\"+ qr_name+".png"

qr = qrcode.QRCode()
qr.add_data(url)


img = qr.make_image()
img.save(file_path)

print(f"QR code generated and saved to {file_path}")

#add a interface and be possible to scan other qr code and convert them back to url and show the url in the interface