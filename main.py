import qrcode as qr       # Import qrcode Module.
from PIL import Image     # Import pil ( pillow - a fork of pil ) Module. PIL - Python Imaging Library.

# QR Code (1) - A QR Code To My Github Profile.
# img = qr.make ( "https://github.com/Mandakini-Kumrawat" )
# img.save ( "Github QR.png" )

# QR Code (2) - A Basic QR Code.
1. Version Parameter Is Tempered To See How It Works. ( From 1 to 20 )
data = "Mandakini - Kumrawat"
qrc = qr.QRCode ( version = 1 , box_size = 10 , border = 5 )
qrc.add_data ( data )
qrc.make ( fit = True )
img = qrc1.make_image ( fill_color = "red" , back_color = "black" )
img.save ( "QR_image.png" )

# Some PILLOW library Functions. -
img = Image.open ( r"Github QR.png" )
img.show () # It Will Show The Image.
print ( img.mode ) # It Will Show The Mode Of Image.
print ( img.size ) # It Will Print The Size Of Image In A Tuple Containing ( Width , Height ).
print ( img.format ) # It Will Print The Format Of Image.
# angle = 50
# img = img.rotate ( angle ) # It Rotates The Image.
# size = ( 40 , 40 )
# img_resized = img.resize ( size , resample = Image.BILINEAR ) # It Resizes The Image.
# img_resized.save ( "Github QR Resized.png" )
# print ( img_resized.size )
# img.show ()