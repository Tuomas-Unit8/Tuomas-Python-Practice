import csv
def main():
    with open("p102_triangles.txt") as f:
        contents = csv.reader(f)
        triangles = []
        for r in contents:
            r = list(map(float, r))
            # pretty ugly to do it manually, but the input format is fixed (and doesn't need to be sanitized)
            # and for only 3 coordinates, it's way easier
            c1 = Coordinates_cart(r[0], r[1])
            c2 = Coordinates_cart(r[2], r[3])
            c3 = Coordinates_cart(r[4], r[5])
            triangles.append(Triangle_102(c1, c2, c3))
        sum = 0
        for t in triangles:
            if(t.contains_og()):
                sum += 1
        print(sum)


class Coordinates_cart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle_102:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
    
    def area(self):
        return abs(self.c1.x * (self.c2.y - self.c3.y) + self.c2.x * (self.c3.y - self.c1.y) + self.c3.x * (self.c1.y - self.c2.y)) / 2

    def contains_og(self):
        og = Coordinates_cart(0, 0)
        t1 = Triangle_102(og, self.c2, self.c3)
        t2 = Triangle_102(self.c1, og, self.c3)
        t3 = Triangle_102(self.c1, self.c2, og)
        return self.area() == (t1.area() + t2.area() + t3.area())
        

if __name__ == "__main__":
    main()