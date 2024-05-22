import os
from insert_ import insert_
from query_ import query_
from delete_ import delete_
from update_ import update_
def main():
    while True:
        choice =int(input("(1)新增(2)查詢(3)刪除(4)更改(5)結束程式："))
        if choice =='1':
            insert_()
        elif choice=='2':
            query_()
        elif choice=='3':
            delete_()
        elif choice=='4':
            update_()
        elif choice=='5':
            print("結束程式！")
            break
        else:
            print("無效指令！")

if __name__=='__main__':
    main()


os.system('pause')