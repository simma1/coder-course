import requests
from fpdf import FPDF
pdf = FPDF()

for num in range (1,10):
	url = 'https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/0C011E0B-770D-41FB-A626-2B03470F752E/foxit-assets/pages/page' + str(num)

	res = requests.get(url, stream = True).content

	with open (str(num) + '.png', 'wb+') as file:
		file.write(res)

	pdf.add_page()
	pdf.image(image,x,y,w,h)

pdf.output("specialist.pdf", "F")
del image

