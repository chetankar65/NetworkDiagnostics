# importing modules
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os
import uuid
  
def makeFile(subTitle, textLines):
    # initializing variables with values
    documentTitle = 'Report'
    #name = str(datetime.datetime.now())
    name = str(uuid.uuid4())
    filename = f'{name}.pdf'

    dirname = os.path.dirname(__file__)
    image = os.path.join(dirname, '../' ,'images/logo.jpg')
    #image = "/Users/Chetan Kar/OneDrive/Desktop/kivy_app/images/logo.jpg"
    print(dirname)
    save_name = os.path.join(os.path.join(dirname, '../' ,f'reports/{filename}'))
    print(save_name)
    # creating a pdf object
    pdf = canvas.Canvas(save_name)
    # setting the title of the document
    pdf.setTitle(documentTitle)
    
    # creating the title by setting it's font 
    # and putting it on the canvas
    pdf.drawInlineImage(image, 180, 720)
    
    # creating the subtitle by setting it's font, 
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)
    
    # drawing a line
    pdf.line(30, 710, 550, 710)
    
    # creating a multiline text using 
    # textline and for loop
    text = pdf.beginText(150, 680)
    text.setFont("Courier", 13)

    for line in textLines:
        if (line[1] == True):
            text.setFillColor(colors.green)
            text.textLine(line[0])
        else:
            text.setFillColor(colors.red)
            text.textLine(line[0])

    pdf.drawText(text)
    
    # saving the pdf
    pdf.save()
