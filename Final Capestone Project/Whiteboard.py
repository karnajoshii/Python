import turtle

class Whiteboard:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        
        # Create turtle canvas
        turtle.setup(width=self.width, height=self.height)
        turtle.title("Online Whiteboard")
        turtle.bgcolor("white")
        turtle.tracer(0)
        
        # Create turtle pen
        self.pen = turtle.Turtle()
        self.pen.pensize(3)
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.pendown()
        
        # Set up event handling
        turtle.listen()
        turtle.onscreenclick(self.draw)
        turtle.onkey(self.clear, "c")
        
    def draw(self, x, y):
        # Move pen to click location
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        
        # Draw line while mouse is down
        self.pen.ondrag(self.draw_line)
        
    def draw_line(self, x, y):
        self.pen.goto(x, y)
        
    def clear(self):
        # Clear the screen
        self.pen.clear()
        
    def run(self):
        # Start the turtle main loop
        turtle.mainloop()
        

# Create a Whiteboard object and run it
wb = Whiteboard()
wb.run()
