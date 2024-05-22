def query_():
    name = input("請輸入病患的姓名：") 
    nid = input("請輸入病患的身分證字號：")

    with open('a.txt','r',encoding='UTF-8') as f:
        lines=f.readlines()
        print(lines)
    for i in range(len(lines)):
            lines[i] = lines[i].split()
            if name == lines[i][0] and nid == lines[i][1]:
                print(lines[i]) 

if __name__ == '__main__':
    query_()
