def delete_():    
    name = input("請輸入病患的姓名：") 
    nid = input("請輸入病患的身分證字號：")
    
    with open('a.txt','r',encoding="UTF-8") as f:
                lines=f.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].split()
                for i in range(len(lines)):    
                    if lines[i][0] == name and lines[i][1] == nid:
                        del(lines[i])
                        break
                print(lines) 
    with open('a.txt','w') as f:
        for line in lines:
            for j in range(len(line)):
                if j < 4:
                    f.write(line[j]+" ")
                else:
                     f.write(line[j])
            f.write('\n')                                

if __name__ =='__main__':
     delete_()   
