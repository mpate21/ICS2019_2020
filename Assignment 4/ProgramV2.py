import turtle,math,sys
"""print("What temperature is it in Fahrenheit?")
def convertTemp(f):
    """
"""Converts Fahrenheit to Celcius"""
"""
    c = str(round(((f-32) * (5/9)),3))
    print(str(f) + " degrees Fahrenheit is " + str(c) + " degrees Celsius")
convertTemp(float(input()))
print("How many acres does your family own?")
def convertArea(a):
    """
"""Converts from acres to barns"""
"""
    b = str(a*(4.047**31))
    print(str(a) + " acres is approximately " + str(b) + " barns")
convertArea(int(input()))"""
print("How many sides do you want for a polygon? (larger amount of sides means you wait longer)")
def sidesToAngle(s):
	"""
	Converts sides to angles to make a polygon
	"""
	circle = 360
	A=circle/s
	
	bob=turtle.Turtle()
	while(circle > 0):
		bob.forward(100)
		bob.left(A)
		circle = circle - A
	screen=bob.getscreen()
	screen.mainloop()
sidesToAngle(int(input()))

