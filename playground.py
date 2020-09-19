import tabula

# creating an object 
file = '2019.pdf'

# creating a pdf reader object
table = tabula.read_pdf(file,pages=2)


print(table[0])