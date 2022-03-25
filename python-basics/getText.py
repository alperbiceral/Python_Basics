import docx
d = docx.Document('demo.docx')
p = d.paragraphs
text = []

for para in p:
	text.append(para.text)

print('\n'.join(text))
