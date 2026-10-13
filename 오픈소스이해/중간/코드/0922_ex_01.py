class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
        self.h_level = 100
        self.e_level = 100

    def eat(self,amount):
        self.h_level -= amount

        if self.h_level < 0:
            self.h_level = 0

        print(f"{self.name}가 사료를 {amount}만큼 먹었습니다")

    def play(self,min):
        if self.e_level < min * 2:
            print(f"에너지가 부족합니다.")
            return
        
        self.e_level -= min * 2
        self.h_level += min

    def sleep(self,hours):
        self.e_level += hours * 20
        if self.e_level > 100:
            self.e_level = 100

    def show_status(self):
        print(f"이름: {self.name}, 견종: {self.breed}, 나이: {self.age}, 배고픔: {self.h_level}, 에너지: {self.e_level}")

my_dog = Dog("wh","jin",5)
my_dog.eat(50)
my_dog.play(20)
my_dog.sleep(2)
my_dog.show_status()