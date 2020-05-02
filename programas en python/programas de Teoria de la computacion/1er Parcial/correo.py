palabra=raw_input("Ingrese la cadena")+";"
estado="q0"

for entrada in palabra:
	if estado == "q0":
		if entrada=="a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or ".":
			estado="q1"
		if entrada== "@"  :
			estado="qR"
		if entrada==";":
			estado="qR"
			
	elif estado =="q1":
		if entrada== "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or ".":
			estado="q1"
		if entrada=="@":
			estado="q2"
		if entrada==";" :
			estado="qR"
			
			
	elif estado=="q2":
		if entrada == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" :
			estado="q2"
		if entrada=="@":
			estado="qR"
		if entrada==".":
			estado="q3"
		if entrada==";" :
			estado="qR"
	
			
	elif estado=="q3":
		if entrada == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z":
			estado="q3"
		
		if entrada== ".":
			estado="qR"
		if entrada==";":
			estado="qA"
			
			


	elif estado =="qR" or estado=="qA":
		break
	
	
print estado
