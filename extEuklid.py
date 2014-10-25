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
	
	#Initialisierung
	A.append(a)
	B.append(b)
	
	if (b != 0):
		Q.append(a / b)
		R.append(a % b)
	
	#Ausgabe
		print "ggT(%i, %i) = %i."%(a, b, ggT(a, b))

	########################################
	# erweiterter euklidischer Algorithmus #
	
	#Variablendeklaration
	global X
	global Y
	X = range(0, len(A))					#X und Y selbe Laenge wie A
	Y = range(0, len(A))		
	
	for i in range(len(X)-1, -1, -1):		#durchlaeuft X von hinten nach vorne. z.b.: 3,2,1,0
		if (i == len(X)-1):					#unterste Stufe: (x,y) = (0,1)
			X[i] = 0
			Y[i] = 1
		else:								#erw. euklidischer Algorithmus
			X[i] = Y[i+1]
			Y[i] = X[i+1] - (Q[i] * Y[i+1])

	print "a * x + b * y = ggT(a, b)"
	print "x = %i\ny = %i"%(X[0], Y[0])


if __name__ == '__main__':
	main()
