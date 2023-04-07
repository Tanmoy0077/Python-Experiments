import cmath as cm
print("Enter the complex number : ", end="")
comp = complex(input())
print("The distance from the origin is : ", end="")
print(f"{(comp.real*comp.real + comp.imag*comp.imag)**0.5:.3f}")
print("The angle is : ", end="")
print(f"{cm.phase(comp):.3f}")
