def calculate_area_3d(name): 
    pi = 3.14
    #converting all characters into lower case
    name = name.lower()
    #check for the conditions
    
    if name == "cube" :
        a = int(input("Enter lenght of the edge: "))

        #calculate the area of the cube

        cube_area = 6 * (a**2)
        print(f"The area of cube is  {cube_area}.")

    elif  name == "rectangular prism" :
        l = int(input("Enter lenght of the rectangular prism: "))
        w = int(input("Enter width of the rectangular prism: "))
        h = int(input("Enter height of the rectangular prism: "))
        
        #calculate the area of the rectangular prism

        rectangular_prism_area = 2 * (w*l + h*l + h*w)
        print(f"The area of rectangular prism is {rectangular_prism_area}.")

    elif name == "cylinder":
        r = int(input("Enter the radius of the circular base: "))
        h = int(input("Enter height of the cylinder: "))
        

        #calculate the area of the cylinder

        cylinder_area = 2 * pi * r*(r+h)
        print(f"The area of cylinder is {ccylinder_area}.")
        
    elif name == "cone":
        r = int(input("Enter the radius of the circular base: "))
        l = int(input("Enter slant height of the cone: "))
        
        #calculate the area of the cone

        cone_area = pi * r *(r + l)
        print(f"The area of cone is {cone_area}.")

    elif name == "sphere":
        r = int(input("Enter the radius of the sphere: "))

        #calculate the area of the sphere

        sphere_area = 4 * pi * (r**2)
        print(f"The area of sphere is  {sphere_area}.")

    elif name == "hemisphere" :
        r = int(input("Enter the radius of the hemisphere: "))
        sphere_area = 3 * pi * (r**2)
        print(f"The area of hemisphere is : {hemisphere_area}.")
    else:
        print("Sorry! This shape is not available")

        
