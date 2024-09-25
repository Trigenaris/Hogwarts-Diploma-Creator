from docxtpl import DocxTemplate, InlineImage
from docx2pdf import convert
from docx.shared import Mm
import pandas as pd
import datetime

def diploma_creator(student_name, graduation_date, hogwarts_house, minister_magic, hogwarts_headmaster):
            house_img = InlineImage(doc, image_descriptor=f"C:/Users/User/OneDrive/Belgeler/VScode_projects/hogwarts_diploma/assets/{hogwarts_house.lower()}.png", width=Mm(29), height=Mm(38))

            doc.render({"name": student_name.capitalize(),
                        "date": graduation_date,
                        "house": house_img,
                        "minister": minister_magic.capitalize(),
                        "headmaster": hogwarts_headmaster.capitalize()})
            
            doc_name = "hogwarts academy " + student_name + ".docx"
            doc.save(doc_name)
            convert(f"C:/Users/User/OneDrive/Belgeler/VScode_projects/hogwarts_diploma/{doc_name}")


doc = DocxTemplate("C:/Users/User/OneDrive/Belgeler/VScode_projects/hogwarts_diploma/assets/Hogwarts_Diploma.docx")

path = ""

while True:
    print("Welcome to Hogwarts Diploma creator")
    print("""
        1. Create a diploma for one person
        2. Create multiple diploma via a csv file
        3. Exit  
    """)
    process = input("Type the relevant number to commence your process: ")

    if process == "1":
        full_name = input("Please enter the full name of the student: ")
        house = input("Please enter the name of the house that the student belongs to: ")
        date = input("Please enter the graduation date (DD/MM/YYYY): ")
        minister = input("Please enter the name of the current minister of magic: ")
        headmaster = input("Please enter the name of the current headmaster of Hogwarts Academy: ")

        diploma_creator(full_name, date, house, minister, headmaster)

    elif process == "2":
        path = input("Please enter the current path of the csv file: ")
        student_list = pd.read_csv(path)

        for i in range(student_list.shape[0]):
             diploma_creator(student_list.full_name[i],
                             student_list.graduation_date[i],
                             student_list.house[i],
                             student_list.name_of_minister_of_magic[i],
                             student_list.hogwarts_headmaster[i])
    elif process == "3":
        break
    else:
        print("invalid option")
    
    