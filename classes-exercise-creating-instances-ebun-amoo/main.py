
class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    
    def move_right(self):
        self.x += 1
        
    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1
        
    def move_down(self):
        self.y -= 1

# please add your code here
first_instance = Point(0, 0)
second_instance = Point(0, 2)
third_instance = Point(2, 0)
first_instance.move_right()