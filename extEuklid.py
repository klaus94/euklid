#!/ usr/binenv python
# -*- coding : utf -8 -*

# erweiterter euklidischer Algorithmus

def ggT(a,b):
	global A
	global B
	global Q
	global R

	if (len(R) > 0):
		if (R[-1] == 0):
			return B[-1]
		else:
			A.append(b)
			B.append(a % b)
			Q.append(A[-1] / B[-1])
			R.append(A[-1] % B[-1])
			return ggT(b, a % b)

def main():
	#Variablendeklaration
	global A
	global B
	global Q
	global R
	A = []
	B = []
	Q = []
	R = []
	#x = []
	#y = []

	#Eingabe
	a = int(raw_input("a = "))
	b = int(raw_input("b = "))
	
	
	A.append(a)
	B.append(b)
	
	if (b != 0):
		Q.append(a / b)
		R.append(a % b)
	
	
	print ggT(a, b)

	print A
	print B
	print Q
	print R


if __name__ == '__main__':
	main()
