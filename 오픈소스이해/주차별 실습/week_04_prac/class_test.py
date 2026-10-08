class Dog:
    def __init__(self,name,bread,age):
        self.name = name
        self.bread = bread
        self.age = age
        self.hunger_level = 100
        self.energy_lever = 100

    def eat(self,amount):
        self.hunger_level -= amount

        if self.hunger_level < 0:
            self.hunger_level = 0

        print(f"{self.name}가 사료를 {amount}만큼 먹었습니다.")

    def play(self, min):
        self.energy_lever -= min * 2
        self.hunger_level += min

        if self.energy_lever < 0:
            self.energy_lever = 0
            print("에너지가 부족합니다")

        print(f"{self.name}가 {min}분 동안 놀았습니다.")

    def sleep(self, hours):
        self.energy_lever += hours * 20

        if self.energy_lever > 100:
            self.energy_lever = 100

        print(f"{self.name}가 {hours}시간 동안 잠을 잤습니다.")

    def status(self):
        print(f"이름: {self.name}, 품종: {self.bread}, 나이: {self.age}, 배고픔 수준: {self.hunger_level}, 에너지 수준: {self.energy_lever}")

    
my_dog = Dog("흰둥이", "진돗개", 5)
my_dog.eat(50)
my_dog.play(20)
my_dog.sleep(2)
my_dog.status()

