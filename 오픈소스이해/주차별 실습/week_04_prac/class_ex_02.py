class CafeMenu:
    def __init__(self,name,price,category,stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.sold_count = 0
        self.sales = 0

    def set_discount(self,rate):
        print("아메리카노 가격 할인 ", self.price," -> ",end="")
        self.price -= self.price * rate
        print(self.price)
        

    def is_soldout(self):
        return self.stock == 0

    def sell(self,count):
        if(count <= 0):
            print("판매수량은 1개 이상이어야 합니다.")
            return False
        
        if(count>self.stock):
            print("재고가 부족합니다")
            return False

        self.stock -= count
        self.sold_count += count
        self.sales += count*self.price
        if(self.category == "coffee"):
            print(self.name,count,"잔 주문했습니다")
        elif(self.category == "dessert"):
            print(self.name,count,"조각 주문했습니다")
        print("가격은",count*self.price,"입니다")
        return True

    def restock(self,count):
        if(count<=0):
            print("입고 수량은 1개 이상이어야 합니다")
        self.stock += count
        if(self.category == "coffee"):
            print(self.name,count,"잔 입고되었습니다")
        elif(self.category == "dessert"):
            print(self.name,count,"조각 입고되었습니다")

    def show_info(self):
        print("----- 메뉴 정보 -----")
        print(f"메뉴이름 : {self.name}")
        print(f"카테고리 : {self.category}")
        print(f"현재가격 : {self.price}")
        print(f"현재재고 : {self.stock}")
        print(f"누적 판매량 : {self.sold_count}")
        print(f"누적 매출 : {self.sales}")
        print(f"품절 여부 : {self.is_soldout()}")


ame = CafeMenu("아메리카노",2500,"coffee",10)
latte = CafeMenu("카페라떼",4000,"coffee",5)
cake = CafeMenu("치즈케이크",5500,"dessert",2)

ame.set_discount(0.1)
ame.sell(2)

latte.sell(2)
cake.sell(2)
print("치즈케이크 품절 여부 ", cake.is_soldout())

cake.sell(1)
cake.restock(3)
cake.sell(1)

ame.show_info
latte.show_info
cake.show_info

menu_list = [ame,latte,cake]
total_sales = sum(menu.sales for menu in menu_list)
print(f"전체 매출: {total_sales}원")