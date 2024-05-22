def insert_():
    name = input("請輸入病患的姓名：") 
    nid = input("請輸入病患的身分證字號：") 
    age = input("請輸入病患的年紀：")
    height = input("請輸入病患的身高(cm)：")
    weight = input("請輸入病患的體重(kg)：")
    
    with open('a.txt','w',encoding="UTF-8") as f:
        f.write(name+ " " +nid+ " " +age+ " " +height+ " " +weight+ "\n")

if __name__ == '__main__':
    insert_()
    