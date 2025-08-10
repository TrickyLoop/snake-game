from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("purple")
        self.speed("fastest")
        self.refresh

    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(x=random_x, y=random_y)
