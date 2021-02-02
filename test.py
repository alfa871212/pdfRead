import pdfplumber
import pandas as pd
pdffile = './test.pdf'
pdf = pdfplumber.open(pdffile)
p0 = pdf.pages[0]
text = p0.extract_text()
target='.  '
num_lis=[0]
prob_num_lis=[]
prob_lis=[]
#exp_num = input("Expected num of prob: ")
exp_num=70

for i in range(0,int(exp_num)):
    prob_num_lis.append(0)
    prob_lis.append(0)


prob=[]
page_lim_lis=[]
num = 0
prob_num=0
#print(len(pdf.pages))
for pages_num in range(len(pdf.pages)):
    text = pdf.pages[pages_num].extract_text()
    print(f"Dealing with page{pages_num+1}...")
    page_lim_lis.append(len(text))
    page_lim = len(text)
    pos = 0
    pos_lis=[]
    subtext = text
    while(pos<len(text)):
        if target in subtext:
            pos = text.index(target, pos+1)
            #print(pos)
            
            if num>=9:
                key = text[pos-2:pos]
                if key.isdigit():
                    #prob_num_lis.append(key)
                    key = int(key)
                    prob_num_lis[key-1]=key
                    num+=1
                    pos_lis.append(pos)

            else:
                key = text[pos-1:pos]
                if key.isdigit():
                    key = int(key)
                    #prob_num_lis.append(key)
                    prob_num_lis[key-1]=key
                    num+=1
                    pos_lis.append(pos)
            subtext = text[pos+2:]
        else:
            pos = len(text)
    print(f"For page{pages_num+1}, pos={pos_lis}")
    for i in range(len(pos_lis)):
        if i != (len(pos_lis)-1):
            problem = text[pos_lis[i]:pos_lis[i+1]]
        else:
            problem = text[pos_lis[i]:page_lim]
        prob_lis[prob_num]=problem
        prob_num+=1



missing = [i for i,x in enumerate(prob_num_lis) if x==0]

for i in missing:
    print(f"Missing Prob num. {i+1}, please check it manually!!!")
    prob_lis = prob_lis[:i]+['0']+prob_lis[i:]
    prob_lis.pop()
missing_prob = [i for i,x in enumerate(prob_lis) if x==0]
for i in missing_prob:
    print(f"Missing Prob. {i+1}, please check it manually!!!")


chapter = ['酸鹼','氧化還原','沉澱','氣體','平衡','反應速率',
'反應熱','電化學','無機','有機','週期表','電子軌域','原子構造','溶液','基本化學','未分類']


acid_keyword = ['酸鹼','H+','OH-','pH','pOH','Ka','Kw','酸性','中性','鹼性','離子積','滴定','共軛酸鹼',
'弱鹼','弱酸','強酸','強鹼']

potential=[]
for i in prob_lis:
    for j in acid_keyword:
        if j in i:
            potential.append(prob_lis.index(i)+1)
tmp = set(potential)
print(sorted(list(tmp)))