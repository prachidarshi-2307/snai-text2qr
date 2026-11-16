import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)

img.save("my_qr.png")

print("Your QR Code has been generated successfully!")