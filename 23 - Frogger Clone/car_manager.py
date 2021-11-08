from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Car(Turtle):
    """Creates a car object to travel across the screen"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.penup()
        self.color(random.choice(COLORS))
        self.random_start()
        self.speed = STARTING_MOVE_DISTANCE

    def random_start(self):
        rand_y = random.randrange(-240, 240, 20)
        self.goto(340, rand_y)


class CarManager:
    """Creates an object to handle car generation, movement, and collision detection with turtle object"""
    def __init__(self):
        self.car_array = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # if random.random() > 0.833:
        self.car_array.append(Car())

    def move_cars(self):
        for car in self.car_array:
            car.back(self.speed)
            if car.xcor() < -360:
                self.car_array.remove(car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def detect_collision(self, turtle_pos):
        for car in self.car_array:
            if car.distance(turtle_pos) < 20:
                return True
            else:
                return False
