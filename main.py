#The main function

import objects_area as ob
import shapes_area as sp
import combine_shapes as cs
import combine_objects as co



print("\t\t..........................."
      "Calculate Area..........................")
print("\n\tDo you want to find shape or Object or Combine shape ")

# Get input from user want to find type of the shape

a = input("\nEnter shape or object or combine :")
a = a.lower()

while(a == 'shape' or a == 'object' or a=='combine'  and a != 0):
    if a == "shape":
       
        print("\n\t\t..........................."
              "Calculate Area of Shape..........................")
        shape_name = input("\nEnter the name of the shape(rectangle,circle,square,triangle): ")
       
        # function calling
        sp.calculate_area(shape_name)
        print("----------------------------------------------------------------------")
        a = input("\nEnter shape or Object or combine OR you want to exit the whole program please enter 0' :")
        a = a.lower()
       

    elif a == "object":
    
        print("\n\t\t..........................."
              "Calculate Area of Object..........................")
        shape_name = input("\nEnter the name of shape (cube,cone,cuboid,rectangular prism,cylinder,cone,sphere,hemisphere ) : ")
       
        # function calling
        ob.calculate_area_3d(shape_name)
        print("---------------------------------------------------------------------\n")
        
        a = input("\nEnter shape or Object or combine 'OR you want to exit the whole program please enter 0' :")
        a = a.lower()
       

    elif a =="combine":
        
        print("\n\tDo you want to combine 2D shape or 3D Object")
        i = input("Enter 2D or 3D :")
        i = i.lower()
        
        if i == "2d":
            print("\n\t\t..........................."
                  "Calculate Area of Combine Shape..........................")
            cs.combine_shapes()
            print("---------------------------------------------------------------------\n")
            
            a = input("\nEnter shape or object or combine 'OR you want to exit the whole program please enter 0' :")
            a = a.lower()
            
        elif i == "3d":
            print("\n\t\t..........................."
                  "Calculate Area of Combine Object..........................")
            co.combine_objects()
            print("---------------------------------------------------------------------\n")
            
            a = input("\nEnter shape or object or combine 'OR you want to exit the whole"
                      "program please enter 0' :")
            a = a.lower()
            os.system('cls')
            

    else:
        
        #If the condition is false display an error message and get the input again 
        print("Sorry your decision is not found!")
        a = input("\nEnter shape or object or combine 'OR you want to exit the whole program please enter 0' :")
        a = a.lower()
        
