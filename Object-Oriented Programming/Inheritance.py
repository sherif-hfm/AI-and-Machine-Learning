class Animal:
    def move(self):
        print("moving")
    def sound(self):
        pass
class Dog(Animal):
    pass

class Snake(Animal):
    def move(self):
        print("crawling")

dog = Dog()
dog.move()

snake = Snake()
snake.move()