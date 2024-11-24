from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from docx2pdf import convert

doc = DocxTemplate("assets/Hogwarts_Diploma.docx")

def diploma_creator(student_name, graduation_date, hogwarts_house, minister_magic, hogwarts_headmaster, is_PDF=False, is_PDF_multi=False):
    house_img = InlineImage(doc, image_descriptor=f"assets/{hogwarts_house.lower()}.png", width=Mm(29), height=Mm(38))

    # Enters the corresponding values into the docx document
    doc.render({
        "name": student_name,
        "date": graduation_date,
        "house": house_img,
        "minister": minister_magic,
        "headmaster": hogwarts_headmaster
    })

    # Names the document after the current student name and saves it
    doc_name = f"hogwarts_academy_{student_name}.docx"
    doc.save(f"diploma/{doc_name}")

    # Converts the document into a PDF document if the 'if condition' checks out
    if is_PDF or is_PDF_multi:
        convert(f"diploma/{doc_name}")
