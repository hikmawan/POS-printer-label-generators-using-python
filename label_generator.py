from escpos.printer import Usb
from PIL import Image, ImageDraw, ImageFont

column_one_y = int(0)
column_x = int(0)
rowheight = int(32)

labelWidth = int(576)
labelHeight = int(960)



shipment_code = "EM.I71XH3IRLX-20200710-20-7LM1WS"
shipment_code_splitted = shipment_code.split("-")
shipment_code_cut_part_one = shipment_code_splitted[1]+" - "+shipment_code_splitted[2]
shipment_code_cut_part_two = lambda x :  shipment_code_splitted[3] + " - " + shipment_code_splitted[4] if (len(shipment_code_splitted) > 4) else shipment_code_splitted[3]
shipment_code_cut_part_two = shipment_code_cut_part_two(shipment_code)

image = Image.new('RGB', (labelWidth,labelHeight), (255, 255, 255))
draw = ImageDraw.Draw(image)


#For linux check your installed font from fc-list
#or install it using "apt-get install fontconfig" for ubuntu and select one from it.


font = ImageFont.truetype('fonts/sans_serif.ttf', size=45)
import random
import os
import datetime
import qrcode
os.system("title ID CARD Generator by Sandeep")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t Air Waybill Generator\t\t\t\t\t  %I:%M:%S %p")
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print (reg_format_date)
print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
 
# starting position of the message

p = Usb(0x0483, 0x5720,timeout=0, in_ep=0x81, out_ep=0x02) #thermal zjiang

# adding an unique id number. You can manually take it from user
(x, y) = (190, column_one_y + rowheight)
idno=random.randint(10000000,90000000)
message = str('ID '+str(shipment_code))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
#draw.text((x, y), message, fill=color, font=font)
draw.rectangle((190, 30, 570, 300), outline=(0, 0, 0))

(x, y) = (270, column_one_y + rowheight*2)
message = "SUB-01"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=64)
draw.text((x, y), message, fill=color, font=font)

draw.line((210,140,550,140),fill=(0,0,0),width=1)

(x, y) = (250, column_one_y + rowheight*5.3)
message = "SUB-01.1"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=64)
draw.text((x, y), message, fill=color, font=font)

draw.line((190,240,570,240),fill=(0,0,0),width=1)
(x, y) = (280, column_one_y + rowheight*8)
message = "0 - SUB-01.1"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=32)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (column_x, column_one_y + rowheight * 7)
message = shipment_code_splitted[0]
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (column_x, column_one_y + rowheight * 8)
message = shipment_code_cut_part_one
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (column_x, column_one_y + rowheight * 9)
message = shipment_code_cut_part_two
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

draw.line((0,315,576,315),fill=(0,0,0),width=1)
(x, y) = (column_x, column_one_y + rowheight * 10)
message="non perishable food and snacks [NOT FRAGILE] COP"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)
draw.line((0,340,576,340),fill=(0,0,0),width=1)

(x, y) = (column_x, column_one_y + rowheight * 11)
message="Penerima : Receiver"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (column_x, column_one_y + rowheight * 12)
message="Tel      : Receiver"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (column_x, column_one_y + rowheight * 13)
message="ETA      : 07 Jul (10:00 - 14:00)"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (column_x, column_one_y + rowheight * 14)
message="Gedung Juang 45 Surabaya | Sewa Tempat Resepsi Pernikahan / Wedding Venue J;. Mayjen Sungkono No.106, Pakis, Kec. Sawahan, kota SBY, Jawa Timur"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (column_x, column_one_y + rowheight * 16)
message="Catatan: Gedung seberang mall ciputra world"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

draw.line((0,535,576,535),fill=(0,0,0),width=1)

(x, y) = (column_x, column_one_y + rowheight * 17)
message="Pengirim : Pengirim"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (column_x, column_one_y + rowheight * 18)
message="Tel      : 3123123213"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

draw.line((0,595,576,595),fill=(0,0,0),width=1)

(x, y) = (column_x, column_one_y + rowheight * 19)
message="Catatan: Gedung seberang mall ciputra world"
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('fonts/sans_serif.ttf', size=24)
draw.text((x, y), message, fill=color, font=font)

# save the edited image
 
image.save('ghani.png')


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=6,
    border=0,
)
img = qr.add_data(shipment_code)
img = qr.make(str(shipment_code))   # this info. is added in QR code, also add other things
img = qr.make_image()
img.save(str(shipment_code)+'.bmp')


til = Image.open('ghani.png')
im = Image.open(str(shipment_code)+'.bmp') #25x25
til.paste(im,(column_x,column_one_y+rowheight))
til.save('ghani.png')

#===Open Comment if you want to print this label directly===
#p.image('ghani.png')
#p.cut()
#==========================================

print(('\n\n\nYour Air Waybill Successfully created in a PNG file ghani.png'))
eval(input('\n\nPress any key to Close program...'))
