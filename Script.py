import os
import img2pdf

# path variable for folder containing jpg images to be compiled into a PDF.
# Note that the path will need to be modified for personal use, unless your  
# name happens to also be Sean and you use the same file structure as me.
path = "C:\\Users\\Sean\\Documents\\Projects\\img-2-singlePDF"

# creates a list of all files with the ".jpg" suffix
images = [i for i in os.listdir(path) if i.endswith(".jpg")]

# use img2pdf to stuff the images into a pdf data
pdf_data = img2pdf.convert(images)

# write the pdf_data to a PDF file called WaterfallImages"
with open("WaterfallImages.pdf", "wb") as file:
    file.write(pdf_data)

