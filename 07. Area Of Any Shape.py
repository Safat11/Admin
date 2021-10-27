#TRIANGLE = (0.5 * B * H)
Base = float(input("Enter Base = "))
Height = float(input("Enter Height = "))

Area = 0.5 * Base * Height

print(Area)

#CIRCLE = (3.1416 * R * R)
Radius = float(input("Enter Radius = "))

Area = 3.1416 * Radius * Radius

print("Area Of Circle = ",Area)

#RECTANGLE = (W * H)
Width = float(input("Enter Width = "))
Height = float(input("Enter Height = "))

Area = Width * Height

print("Area Of Rectangle = ",Area)

#SQUARE = (A * A)
A = float(input("Enter A Length Of Side = "))

Area = A * A

print("Area Of Square = ",Area)

#TRAPEZOID = [ 0.5 * (A + B) * H ]
A = float(input("Enter A Length Of Side = "))
B = float(input("Enter Base = "))
H = float(input("Enter Height = "))

Area = 0.5 * (A+B) * H

print("Area Of Trapezoid = ",Area)
