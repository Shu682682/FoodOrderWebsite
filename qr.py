import qrcode

# need to install python -m pip install qrcode
# python -m pip install pillow

image = qrcode.make("https://127.0.0.1:8000")  # app normally run on this domain
image.save("qr.png")
