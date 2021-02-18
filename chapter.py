"""
index:
acid=0
oxred=1
precipataition=2
gas=3
balance=4
rate=5
heat=6
electric=7
inorganic=8
organic=9
periodic=10
orbital=11
atom=12
solution=13
basic=14
concentration=15
"""
def cmpProb(prob_lis, keywords):
    acid_keyword = ['酸鹼','H+','OH-','pH','pOH','Ka','Kw','酸性','中性','鹼性','離子積','滴定','共軛酸鹼','弱鹼','弱酸','強酸','強鹼','氫離子','氫氧根離子']
    oxred_keyword = ['氧化','還原']
    precipitaition_keyword = ['沉澱','沈澱','ksp']
    gas_keyword =['氣體','理想氣體','波以耳','查理','給呂薩克','nRT','氣壓計','大氣壓','分壓']
    balance_keyword =['平衡','平衡常數','勒沙特列']
    rate_keyword=['反應速率','速率定律式']
    heat_keyword=['反應熱','生成熱','分解熱','燃燒熱']
    electric_keyword=['電化學','電位','電壓','電流','庫侖']
    inorganic_keyword=['無機','錯合物','錯離子','配位']
    organic_keyword=['有機','烷','烯','炔','醯胺','胺','異構物','醇','醛','酮','酯','醚']
    periodic_keyword=['週期表','電負度','電子親和力','游離能','原子半徑','金屬性']
    orbital_keyword=['軌域','混成','共價鍵','價鍵理論','金屬鍵','離子鍵','氫鍵','凡得瓦力','鍵角','鍵長','鍵能','極性','分子形狀','共振','單鍵','雙鍵','參鍵']
    atom_keyword=['原子','質子','電子','中子','原子序','質量數']
    solution_keyword=['溶液','拉午耳','蒸氣壓','理想溶液']
    basic_keyword=['係數平衡','方程式係數']
    concentration_keyword=['溶解度','濃度','飽和','不飽和','過飽和']

    keyword_prob = []
    keyword_prob.append(acid_keyword)
    keyword_prob.append(oxred_keyword)
    keyword_prob.append(precipitaition_keyword)
    keyword_prob.append(gas_keyword)
    keyword_prob.append(balance_keyword)
    keyword_prob.append(rate_keyword)
    keyword_prob.append(heat_keyword)
    keyword_prob.append(electric_keyword)
    keyword_prob.append(inorganic_keyword)
    keyword_prob.append(organic_keyword)
    keyword_prob.append(periodic_keyword)
    keyword_prob.append(orbital_keyword)
    keyword_prob.append(atom_keyword)
    keyword_prob.append(solution_keyword)
    keyword_prob.append(basic_keyword)
    keyword_prob.append(concentration_keyword)

    acid_prob=[]
    oxred_prob=[]
    precipitaition_prob=[]
    gas_prob=[]
    balance_prob=[]
    rate_prob=[]
    heat_prob=[]
    electric_prob=[]
    inorganic_prob=[]
    organic_prob=[]
    periodic_prob=[]
    orbital_prob=[]
    atom_prob=[]
    solution_prob=[]
    basic_prob=[]
    concentration_prob=[]

    chapter_prob = []
    for i in range(len(keyword_prob)):
        chapter_prob.append([])

    for p in prob_lis:
        print(f"Dealing with prob{prob_lis.index(p)+1}")
        for key_lis in keyword_prob:
            print(f"Comparing with topic {key_lis[0]}")
            for key in key_lis:
                if key in p:
                    chapter_prob[keyword_prob.index(key_lis)].append(prob_lis.index(p)+1)
                    

    for i in range(len(chapter_prob)):
        print(keyword_prob[i][0],sorted(set(chapter_prob[i])))