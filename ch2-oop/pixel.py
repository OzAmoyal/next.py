class pixel:
    def __init__(self,x=0,y=0,r=0,g=0,b=0):
        self._x=x
        self._y=y
        self._r=r
        self._g=g
        self._b=b
    
    def set_coords(self,x,y):
        self._x=x
        self._y=y

    def set_grayscale(self):
        gray = int((self._r + self._g + self._b) / 3)
        self._r = gray
        self._g = gray
        self._b = gray
    
    def print_pixel_info(self):
        if self._r==0 and self._g==0:
            color = "blue"
        elif self._r==0 and self._b == 0:
            color = "green"
        elif self._g == 0 and self._b==0:
            color = "red"
        else:
            color = ""
        print(f"X: {self._x}, Y: {self._y}, Color: ({self._r}, {self._g}, {self._b}) {color}")

def main():
    p = pixel(5,6,250,0,0)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()
    
main()