import pdfplumber
import pandas as pd
pdffile = './test.pdf'
pdf = pdfplumber.open(pdffile)
expect_ind=[]
sw = True
ctrl = 1
page_num = 1
prob=[]
page_lis=[]
while sw:
    ind = str(ctrl)+'. '
    text = pdf.pages[page_num-1].extract_text()
    
    #problem in text
    if ind in text:
        print(ind,f"in page{page_num}")
        page_lis.append(text.find(ind))
        ctrl+=1
    else:
        page_num+=1
        page_lis.append(len(text))
        """
        if page_lis[0]!=0:
            page_lis.insert(0,0)
        """
        prob.append(page_lis)
        page_lis=[]
    
    if page_num > len(pdf.pages):
        break
prob.pop()
ctrl-=1
print(prob)

probContent = []
content =''
for i in range(ctrl):
    probContent.append('')
    
for i in range(len(prob)):
    text = pdf.pages[i].extract_text()
    subtext = ''
    if prob[i][0]!=0 and i!=0:
        subtext = text[:prob[i][0]]
        
    for j in range(len(prob[i])-1):
        content = text[prob[i][j]:prob[i][j+1]]
        probContent.append(content)
        
            

"""
for i in range(ctrl):
    probContent.append("")
for i in range(ctrl):
    num = i
    for j in range(len(prob)):
        text = pdf.pages[j].extract_text()
"""
    