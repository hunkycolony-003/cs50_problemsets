#Taking real and imaginary part of x as input
re_x = input("What's real of x? ")
im_x = input("What's imaginary of x? ")

#Printing x
x = re_x + " + i " + im_x

print("x is: ", x, end="\n\n")

#Taking real and impaginary part of y as input
re_y = input("What's real of y? ")
im_y = input("Whatt's imagijnary of y? ")

#Printing y
y = re_y + " + i " + im_y

print("y is: ", y, end="\n\n\n")



#Calculating real and imagiay part of z
re_z = int(re_x) + int(re_y)
im_z = int(im_x) + int(im_y)

#printing z
z = str(re_z) + " + i " + str(im_z)

print("The sum is", z)
