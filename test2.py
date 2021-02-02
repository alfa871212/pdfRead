import pdfplumber
import pandas as pd
pdffile = './test.pdf'
pdf = pdfplumber.open(pdffile)
p0 = pdf.pages[0]
text = p0.extract_text()
exp_num = 70
target_lis = []

for i in range(exp_num):
    target = str(i+1)+".  "
    target_lis.append(target)
target_lis[44]='000'
print(len(pdf.pages))

prob_num = 0
ctrl = True
missing=[]
for page in range(len(pdf.pages)):
    text = pdf.pages[page].extract_text()
    print(f"Dealing with page{page+1}...")
    if prob_num != 70:    
        while target_lis[prob_num] in text:
            print(f"Found Prob{prob_num+1} in page{page+1}!")
            prob_num+=1
            if prob_num==70:
                break
            if target_lis[prob_num]=='000':
                prob_num+=1
    print(f"Done with page{page+1}!")

