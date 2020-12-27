import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PIL import Image, ImageDraw, ImageFont
import qrcode

def credencial(nombre, apellido, departamento):

    #--------------------abrir credencial base------------------
    credencial_base = Image.open(".\\Credenciales\\credencial_base.jpg")
    #------------------fin abrir credencial base----------------
    
    #----------------------generar codigo qr--------------------
    qr = qrcode.QRCode(
                        version=2,
                        box_size=27,
                        border=4
                        )
    qr.add_data("name:{name},surname:{surname},departament:{departament}".format(name=nombre, surname=apellido, departament=departamento))
    codigo_qr_empleado = qr.make_image(fill_color="black", back_color="white")
    #-------------------fin generar codigo qr-------------------

    #---------------pegar codigo qr en credencial---------------
    credencial_base.paste(codigo_qr_empleado, (807,640))
    #-------------fin pegar codigo qr en credencial-------------
    
    #--------------escribir datos en la credencial--------------
    credencial_base_draw = ImageDraw.Draw(credencial_base)
    font = ImageFont.truetype("arial.ttf", 120)
    datos = "Nombre: {} \n\nApellido: {} \n\nDepartamento: {}".format(nombre, apellido, departamento)
    
    lines = datos.splitlines()
    w = font.getsize(max(lines, key=lambda s: len(s)))[0]
    h = font.getsize(datos)[1] * len(lines)
    x, y = credencial_base.size
    x /= 2
    x -= w / 2
    y /= 2
    y = 1875

    credencial_base_draw.text((x, y), datos, font=font, fill="black", align="center")
    #-----------fin escribir datos en la credencial-------------

    credencial_base.show()
    credencial_base.save(".\\Credenciales\\credenciales_generadas\\{}_{}_{}.jpg".format(nombre, apellido, departamento))
