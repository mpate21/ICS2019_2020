import cv2
import numpy as np

L = 20
p = 0.4
p1 = p
p2 = p

np.random.seed(100)
#display an array
#param img the array
#param title
#param wait= The wait time in milliseconds. 0 to wait for keypress
def show(img, title="Image", wait=0):
	resized=cv2.resize(np.uint8(img), (600,600), interpolation = cv2.INTER_AREA)
	cv2.imshow(title, resized)
	cv2.waitKey(wait)# 0 means wait for key input. positive value waits for n milliseconds


def initCA(L,p1,p2):
	ca = np.zeros( (L,L) )
	for i in range(L):#visits each column once
		for j in range(L):#Visits each row once
			r=np.random.random()
			if (r>=p1+p2):
				ca[i,j]=0
			elif(p1<=r<p1+p2):
				ca[i,j]=2
			else:
				ca[i,j]=1
	return ca
def calcSat(ca,i,j):
	kind = ca[i,j]
	likeCount= 0
	neighCount= 0
	
	for x in [-1,0,1]:
		for y in [-1,0,1]:
			if(i==x and j==y):
				pass
			else:
				if(kind==ca[x,y]):
					likeCount +=1
				if (ca[x,y]!=0):
					neighCount += 1
	print("Kind is {}. There are {} likes and {} neighbors." .format(kind,likeCount,neighCount))
	
	if(neighCount>0):
		return likeCount/neighCount
	else:
		return 0
ca=initCA(L,p1,p2)
print(ca)

print(calcSat(ca, 2, 1))

