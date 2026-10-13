class CafeMenu:
    def __init__(self,name,price,category,stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.sold_c = 0
        self.sales = 0

    def set_discount(self,rate):
        self.price -= self.price * rate

    def is_soldout(self):
        return self.stock == 0

    def sell(self,count):
        if count <= 0:
            print(f"판매수량은 1개 이상")
            return False
        
        if self.stock < count:
            print(f"재고부족")
            return False
        
        self.stock -= count
        self.sold_c += count
        self.sales += count * self.price

        print(f"{self.name}을 {count}만큼 {count * self.price}에 팔았습니다")
        return True

