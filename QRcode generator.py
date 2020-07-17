import qrcode
link='https://xyz.com'
#Filename to save the resulting png
filename='qr.png'
#generate qr code
img=qrcode.make(link)
#save img to a file
img.save(filename)