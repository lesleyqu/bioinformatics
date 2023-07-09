'''获取负例样本，即从全本样本中去除正例样本'''
file1 = open('procutclean-y.fasta', 'r', encoding='utf-8') # 所有蛋白质切片后的样本（包含正例样本）
file2 = open('phosposfast.fasta', 'r', encoding='utf-8')  # 正例样本
file3 = open('neg-y.fasta', 'w', encoding='utf-8')
name=[]
a=0
try:
    line2=file2.readlines()

    for line1 in file1.readlines():
        if line1[0] == '>':
            name.append(line1)
            continue
        if line1 not in line2:
            file3.write('{}'.format(name[a]))
            file3.write(line1)
        print(a)
    
        
        a+=1
            
finally:
        file1.close()
        file2.close()
        file3.close()
