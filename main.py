from docx import Document

company = "Google"
hr_manager = "Ms. Stephanie Chan"
position = "Software Engineer"
office = "New York"
address_line_1 = "1700 Menlo Park Drive"
city = "San Francisco"
state = "NY"
someone = "Ted Baker"

diction = {'<company>': company, 
    '<position>':position, 
    '<office>':office, 
    '<address_line_1>':address_line_1, 
    '<city>':city,
    '<st>':state,
    '<someone>':someone}

document = Document("cover_letter_default.docx")

for paragraph in document.paragraphs:
    #print paragraph.text
    for key,value in diction.iteritems():
        if key in paragraph.text:
            print "*found* "+ key
            string = paragraph.text
            paragraph.text = string.replace(str(key), value, 100)
            print '*replaced* with '+value

document.save(company+".docx")