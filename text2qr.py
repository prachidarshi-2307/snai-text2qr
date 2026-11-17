import pyfiglet
import qrcode

# Display the application banner
banner = pyfiglet.figlet_format("Text2QR", font="slant")
print(banner)

# Get input from the user
data = input("Enter text or URL to generate QR code: ")

# Generate QR code
img = qrcode.make(data)

# Save QR code as an image
img.save("text2qr.png")

print("QR Code generated successfully!")
print("Saved as text2qr.png")