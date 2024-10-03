pi=3.14
total_area = 0
def combine_shapes():
    def rectangle(name):
        # converting all characters into lower cases
        name = name.lower()

        l = int(input("Enter rectangle's length: "))
        w = int(input("Enter rectangle's width: "))

        # calculate area of rectangle
        rect_area = l * w
        print(f"The area of rectangle is {rect_area}.")
        global total_area 
        total_area = total_area + rect_area


    def square(name):

        # converting all characters into lower cases
        name = name.lower()
        
        s = int(input("Enter square's side length: "))
           
        # calculate area of square
        sqt_area = s * s
        global total_area 
        total_area = total_area + sqt_area
        print(f"The area of square is {sqt_area}.")

    def triangle(name):
        
        # converting all characters into lower cases
        name = name.lower()

        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
           
        # calculate area of triangle
        tri_area = 0.5 * b * h
        print(f"The area of triangle is {tri_area}.")
        global total_area 
        total_area = total_area + tri_area

    def circle(name):

        # converting all characters into lower cases
        name = name.lower()

        r = int(input("Enter circle's radius length: "))
             
        # calculate area of circle
        circ_area = pi * r * r
        print(f"The area of circle is {circ_area}.")
        global total_area 
        total_area = total_area + circ_area


    #The main function of combine shape
        
    shape_name = input("Enter the name of shape which area you want to find (rectangle,circle,square,triangle): ")   
    if shape_name =="rectangle":
        rectangle(shape_name)
        x = input("Do you want to add another shape please enter yes or no")
        x = x.lower()

                       
    elif shape_name =="square":
        square(shape_name)
        x = input("Do you want to add another shape please enter yes or no :")
        x = x.lower()

        
    elif shape_name =="triangle":
        triangle(shape_name)
        x = input("Do you want to add another shape please enter yes or no: ")
        x = x.lower()

    elif shape_name =="circle":
        circle(shape_name)
        x = input("Do you want to add another shape please enter yes or no: ")
        x = x.lower()

    else:
        print("Please enter the correct shape name")
        x = input("Do you want to add another shape please enter yes or no : ")
        x = x.lower()


    while(x != 'no' and x == 'yes'):
        shape_name = input("Enter the name of shape which area you want to find: ")
        if shape_name =="rectangle":
            rectangle(shape_name)
            x = input("Do you want to add another shape please enter yes or no: ")
            x = x.lower()

        elif shape_name =="square":
            square(shape_name)
            x = input("Do you want to add another shape please enter yes or no :")
            x = x.lower()
            

        elif shape_name =="triangle":
            triangle(shape_name)
            x = input("Do you want to add another shape please enter yes or no :")
            x = x.lower()
            
        elif shape_name =="circle":
            circle(shape_name)
            x = input("Do you want to add another shape please enter yes or no : ")
            x = x.lower()
            
        else:
            print("Please enter the correct shape name")
            x = input("Do you want to add another shape please enter yes or no")
            x = x.lower()
        
    print(f"The total area of the combine shape is {total_area}.")
