def calculate_area(name): 
    # converting all characters into lower cases
    name = name.lower()
    # check for the conditions
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        w = int(input("Enter rectangle's width: "))
     
    # calculate area of rectangle
        rect_area = l * w
        print(f"The area of rectangle is {rect_area}.")
   
    elif name == "square":
        s = int(input("Enter square's side length: "))
       
    # calculate area of square
        sqt_area = s * s
        print(f"The area of square is {sqt_area}.")
 
    elif name == "triangle":
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
       
    # calculate area of triangle
        tri_area = 0.5 * b * h
        print(f"The area of triangle is {tri_area}.")
 
    elif name == "circle":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14
         
    # calculate area of circle
        circ_area = pi * r * r
        print(f"The area of circle is {circ_area}.")
         
    elif name == 'parallelogram':
        b = int(input("Enter parallelogram's base length: "))
        h = int(input("Enter parallelogram's height length: "))
    else:
        print("Sorry! This shape is not available")

       
        

        
       
