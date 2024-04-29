'''
QR : which stands for “quick response” code is basically a barcode on steroids. While the barcode holds information horizontally, the QR code does so both horizontally and vertically. QR codes are quick response code that can be used to make a call, send messages or emails, open a website, or share locations. QR code can store upto 4296 characters, or 7089 digits
'''

import qrcode

# To generate a name for our qr code image, we will extract the url name before the extention
def remove_extension(img_url):
    # Find the index of the last dot in the URL
    last_dot_index = img_url.rfind('.')
    
    # If a dot is found, return the substring before it, else return the original URL
    if last_dot_index != -1:
        return img_url[:last_dot_index]
    else:
        return img_url

def generate_qr_code(url):

    img_name = remove_extension(url)

    myqr = qrcode.make(url)
    myqr.save(f"qr_code_images/{img_name}.png")

while True:
    x = input("Type the url you want to generate QR Code for. Example: google.com (q to quit) ").lower()

    if x == 'q':
        break

    generate_qr_code(x) 