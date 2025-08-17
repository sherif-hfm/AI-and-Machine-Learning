class Animal:
    def move(self):
        print("moving")
    def sound(self):
        print("hiss")

class Dog(Animal):
    def move(self):
        print("running")
    def sound(self):
        print("bark")

class Snake(Animal):
    def move(self):
        print("crawling")

dog = Dog()
dog.move()
dog.sound()

snake = Snake()
snake.move()
snake.sound()