def update_():
    name = input("請輸入病患的姓名：") 
    nid = input("請輸入病患的身分證字號：")
    with open('a.txt','r',encoding='UTF-8') as f:
        lines=f.readlines()
        print(lines)
    
    for i in range(len(lines)):
            lines[i] = lines[i].split()
            if name == lines[i][0] and nid == lines[i][1]:
                line[i][0] = input("請輸入病患的姓名：") 
                line[i][1] = input("請輸入病患的身分證字號：") 
                line[i][2] = input("請輸入病患的年紀：")
                line[i][3] = input("請輸入病患的身高(cm)：")
                line[i][4] = input("請輸入病患的體重(kg)：")
    with open('a.txt','w') as f:
        for line in lines:
            for j in range(len(line)):
                if j < 4:
                    f.write(line[j]+" ")
                else:
                     f.write(line[j])
            f.write('\n')                                

if __name__ =='__main__':
     update_()   

    #先delete原本的再insert
