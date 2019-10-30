import cv2
import numpy as np

wireColor=(128,128,128)
notWireColor=(0,0,0)
electronColor=(0,255,255)
tailColor=(0,128,255)

wire=1
notWire=0
electron=3
tail=2

def show(img, title="image", wait=30):
	d=np.max(img.shape)
	unitSize=640//d
	resized = cv2.resize(np.uint8(img), (unitSize*w,unitSize*h), interpolation = cv2.INTER_AREA)
	cv2.imshow(title, resized)
	cv2.waitKey(wait) # 0 means wait for key input. postive value waits for that many milliseconds

def showCA(ca, title="image", wait=30):
	h,w = ca.shape[:2]
	img = np.zeros((h,w,3))
	img[ca==wire]=wireColor
	img[ca==notWire]=notWireColor
	img[ca==electron]=electronColor
	img[ca==tail]=tailColor
	# ~ img[ca==2]=(255,0,0)
	show(img, wait=wait)

def iterate(world):
	newWorld=world*1
	kernel=np.float32([[1,1,1],[1,0,1],[1,1,1]])
	cv2.filter2D(world==electron),kernel
	print(img)
world=np.array([[0,0,0,0,0],
				[2,3,1,1,1],
				[0,0,0,0,1]])
fps=10
for i in range(100):
	world=iterate(world)
	showCA(world,1000//fps)
	
	
	
	
# ~ public class Rectangle{
	# ~ //Instance Variable(s):Things to remember
	# ~ private int w=100;
	# ~ private int h=100;
	# ~ //Constructor(s):Fill In instance varibles
	# ~ public Rectangle(int w, int h)
	# ~ //Method(s)/Function(s):Things you can do
	# ~ public int area()
	# ~ {
		# ~ return w*h
	# ~ }
# ~ }

class Rectangle:
	def __init__(self,w,h):
		self.w=w
		self.h=h
	def area(self):
		return self.w*self.h
	def scale(self):
		self.w*=factor
		self.h*=factor
reggie = Rectangle(5,6)
print(reggie.area())
