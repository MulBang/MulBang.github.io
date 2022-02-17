items = {"커피"   : [3000,5,10],
         "펜"     : [1000,10,20],
         "종이컵" : [20,1050,550],
         "우유"   : [500,10,5],
         "콜라"   : [1050,22,10]}


def openfile():
    infile = open("items.txt", "r")
    for item in infile:
        list = item.split()
        print(list[0], end=' \t')
        print("가격=", list[1], end=' \t')
        print("판매량=", list[2], end=' \t')
        print("재고=", list[3])
    infile.close()

openfile()


def printItem(key):
    price, saled, stockn = items[key]
    print(key, end=' \t')
    print("가격=", price, end=' \t')
    print("판매량=", saled, end=' \t')
    print("재고=", stockn)
    

def statusPrint():
    for key in items.keys():
        printItem(key)


def printKey():
    for product in range(5):
        print(list(items.keys())[product])


def saleFunc():
    printKey()
    key = input("판매한 물품은?")
    if key in items.keys():
        price, saled, stockn = items[key]
        amount = int(input("판매한 수량은?"))
        if amount > int(stockn):
            print("판매한 수량이 재고보다 많습니다. 입력할 수 없습니다.")
        elif amount <= int(stockn):
            saled = saled + amount
            stockn = stockn - amount
            items[key][1]=saled
            items[key][2]=stockn
            statusPrint()
    else:
        print("판매하지 않는 물품입니다.")

    
def addition():
    addname = input("추가된 판매 물품이름을 입력하시오: ")
    addprice = input("단가를 입력하시오: ")
    addsaled = input("판매수량을 입력하시오: ")
    addstockn = input("재고를 입력하시오: ")
    statusPrint()
    print(addname, end='\t')
    print("가격=", addprice, end='\t')
    print("판매량=", addsaled, end='\t')
    print("재고=", addstockn)
    addsave = input("파일에 저장하겠습니까?(네, 아니요): ")
    if addsave == '네':
        infile = open("../파일/items.txt", "a")
        infile.write(addname)
        infile.write(' ')
        infile.write(addprice)
        infile.write(' ')
        infile.write(addsaled)
        infile.write(' ')
        infile.write(addstockn)
        infile.write('\n')
        print("변경된 내용을 저장했습니다.")
        infile.close()
    elif addsave == '아니요':
        print('파일에 저장하지 않았습니다')
    else:
        print('적합하지 않은 명령입니다.')
    
    
def plus():
    printKey()
    plusname = input("재고 수량을 바꿀 물품 이름을 입력하시오: ")
    if plusname in items.keys():
        price, saled, stockn = items[plusname]
        plusstockn = int(input("재고 수량을 얼만큼 늘릴건가요?: "))
        stockn = stockn + plusstockn
        items[plusname][2] = stockn
        statusPrint()
    else:
        print("판매하지 않는 물품입니다.")


def change():
    printKey()
    changename = input("단가를 바굴 물품 이름을 입력하시오: ")
    if changename in items.keys():
        price, saled, stockn = items[changename]
        changeprice = int(input("단가를 얼마로 바꿀껀가요?: "))
        items[changename][0] = changeprice
        statusPrint()
    else:
        print("판매하지 않는 물품입니다.")
    
        

while True:
    respond = input("명령을 입력하시오(중지, 출력, 판매, 추가, 입고, 변경): ")

    if respond == "출력":
        statusPrint()
        
    elif respond == "중지":
        print("재고관리 프로그램을 중지합니다.")
        break
    
    elif respond == "판매":
        saleFunc()

    elif respond == "추가":
        addition()

    elif respond == "입고":
        plus()

    elif respond == "변경":
        change()

    else:
        print("적합하지 않은 명령입니다.")


