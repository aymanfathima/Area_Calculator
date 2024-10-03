pi = 3.14
total_area = 0


def cube():
    a = int(input("Enter lenght of the edge : "))

    # calculate the area 

    cube_area = 6 * (a**2)
    
    print(f"The area of rectangle is : {cube_area}.")
    return cube_area

def cone():
    r = int(input("Enter the radius of the circular base: "))
    l = int(input("Enter slant height of the cone       : "))
        
    #calculate the area 

    cone_area = pi * r *(r + l)
    print(f"\nThe area of rectangle is : {cone_area}.\n")
    return cone_area

def cuboid():
    a = int(input("Enter the length of the cuboid :"))
    b = int(input("Enter the height of the cuboid :"))
    c = int(input("Enter the width of the cuboid  :"))

    #calculate the area

    cuboid_area = 2*(a*b)+ 2*(b*c)+ 2*(a*c)
    print(f"\nThe area of rectangle is : {cuboid_area}.\n")
    return cuboid_area

def combine_objects():

    name = input("Enter the 1 st object (cube,cone,cuboid):")
    name2 = input("Enter the 2 nd object (cube,cone,cuboid) :")

#combine cone and cube
    
    if ((name == "cone" and name2 =="cube" )or (name=="cube" and name2 =="cone")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= a**2
        cube_areas = 5*(a**2)

        r = int(input("Enter the radius of the circular base: "))
        h = int(input("Enter slant height of the cone       : "))

        circle = pi*r*r
        cone_areas = pi * r * h

    if circle > cube_one:
        total_area = (circle - cube_one)+ cube_areas + cone_areas
        
    else:
        total_area = (cube_one - circle)+ cube_areas + cone_areas

    print(f"The total area of combine object is {total_area}")

#combine cuboid and cone
    
    if((name == "cuboid" and name2 =="cone" )or (name=="cone" and name2 =="cuboid")):
        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        one_side =a * b
        cuboid_area =(a*b)+ 2*(b*c)+ 2*(a*c)

        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = pi*r*2
        cone_areas = pi * r * l

        if circle > one_side :
            total_area = (circle - one_side)+ cone_areas + cuboid_area
        else:
            total_area = (one_side - circle)+cone_areas + cuboid_area

        print(f"The total area of combine object is {total_area}")
#combine cuboid and cube
    elif((name == "cuboid" and name2 =="cube" )or (name=="cube" and name2 =="cuboid")):
        a = int(input("\nEnter lenght of the edge : "))
        cube_one= a**2
        cube_areas = 5*(a**2)

        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        cuboid_area = (a*b)+ 2*(b*c)+ 2*(a*c)
        one_side = a*b
        if one_side > cube_one:
            total_area = (one_side - cube_one)+ cube_areas + cuboid_area
        else:
            total_area = (cube_one - one_side)+ cube_areas + cuboid_area

        print(f"The total area of combine object is {total_area}")

#combine cuboid and cone
    elif((name == "cuboid" and name2 =="cone" )or (name=="cone" and name2 =="cuboid")):
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone       : "))

        circle = pi*r*2
        cone_areas = pi * r * l

        a = int(input("Enter the length of the cuboid :"))
        b = int(input("Enter the height of the cuboid :"))
        c = int(input("Enter the width of the cuboid  :"))

        cuboid_area = (a*b)+ 2*(b*c)+ 2*(a*c)
        one_side = a*b
    
        if one_side > circle:
            total_area = (one_side - circle)+ cone_areas + cuboid_area
        else:
            total_area = (circle - one_side)+ cone_areas + cuboid_area

        print(f"The total area of combine object is {total_area}.")












