import math 
def circle(radius):
    return math.pi*radius*radius

def rectangle(length,width):
    return length*width

def triangle(base,height):
    return 0.5*base*height

if __name__ == "__main__":
    print(circle(5))
    print(rectangle(5,3))
    print(triangle(6,2))