from circle import *

def main():
    cyl = Cylinder(1, "Red", 1)
    print(f"Radius is {cyl.getradius()}")
    print(f"Height is {cyl.getheight()}")
    print(f"Color is {cyl.getcolor()}")
    print(f"Area is {'{:.2f}'.format(cyl.getarea())}")
    print(f"Volume is {'{:.2f}'.format(cyl.getvolume())}")
    cyl.setradius(5)
    cyl.setheight(5)
    cyl.setcolor("Black")
    print(f"The New Radius is {cyl.getradius()}")
    print(f"The New Color is {cyl.getcolor()}")
    print(f"The New Area is {'{:.2f}'.format(cyl.getarea())}")
    print(f"The New Volume is {'{:.2f}'.format(cyl.getvolume())}")

main()