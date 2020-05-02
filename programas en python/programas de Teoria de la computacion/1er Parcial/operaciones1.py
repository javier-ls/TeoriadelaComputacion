palabra =raw_input("ingresa tu operacion: ")+";"

estado="q0"

for entrada in palabra:
	if estado == "q0":
		if entrada=="0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
			estado="q1"
		if entrada=="+":
			estado="qR"
		if entrada=="-":
			estado="qR"
		if entrada=="*":
			estado="qR"
		if entrada== "/":
			estado="qR"
		if entrada== ";":
			estado="qR"
			
	elif estado =="q1":
		if entrada=="0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
			estado="q1"
		if entrada=="+":
			estado="q2"
		if entrada=="-":
			estado="q2"
		if entrada=="/":
			estado="q2"
		if entrada=="*":
			estado="q2"
		if entrada==";":
			estado="qR"
			
	elif estado=="q2":
		if entrada == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
			estado="q3"
		if entrada=="+":
			estado="qR"
		if entrada=="-":
			estado="qR"
		if entrada=="/":
			estado="qR"
		if entrada=="*":
			estado="qR"
		if entrada==";":
			estado="qR"
			
	elif estado=="q3":
		if entrada == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
			estado="q3"
		if entrada=="+":
			estado="q2"
		if entrada=="-":
			estado="q2"
		if entrada=="/":
			estado="q2"
		if entrada=="*":
			estado="q2"
		if entrada==";":
			estado="qA"

	elif estado =="qR" or estado=="qA":
		break
	
print estado
