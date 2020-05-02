palabra=raw_input("Ingrese la cadena")+"*"
estado="q0"

for entrada in palabra:
	if estado == "q0":
		if entrada=="0":
			estado="q0"
		if entrada=="1":
			estado="q1"
		if entrada=="*":
			estado="qR"
			
	elif estado =="q1":
		if entrada=="0":
			estado="q1"
		if entrada=="1":
			estado="q2"
		if entrada=="*" :
			estado="qR"
			
	elif estado=="q2":
		if entrada =="0":
			estado="q2"
		if entrada=="1":
			estado="q1"
		if entrada=="*":
			estado="qA"

	elif estado =="qR" or estado=="qA":
		break
	
	
print estado
