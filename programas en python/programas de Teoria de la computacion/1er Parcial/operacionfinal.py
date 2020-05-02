palabra=raw_input("Ingrese la operacion: ") + ";"
estado="q0"
n1=""
n2=""
op=""

for entrada in palabra:
    if estado == "q0":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
            estado="q1"
            n1 = entrada
        if entrada == ";" or entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":

            estado="qr"
            
    elif estado == "q1":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
            estado="q1"
            n1 += entrada
        if  entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
            estado="q2"
            op += entrada
        if entrada == ";":
            

            
            estado="qr"
            
    elif estado == "q2":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
           estado="q3"
           n2 = entrada
        if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/" or entrada==";":
           estado="qr"

    elif estado == "q3":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
           estado="q3"
           n2 += entrada
        if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
           estado="q2"
        if entrada==";":
           estado="qa"
    
           
    
               
    if estado=="qa":
        n1=int(n1)
        n2=int(n2)
        op=(op)
        
        if op=="+" or op=="-" or  op=="*" or op=="/":
            if op=="+":
                r=n1+n2
              
            elif op=="*":
                r=n1*n2
                
            elif op=="-":
                r=n1-n2
                                    
            elif op=="/":
                r=n1/n2

            print "Resultado = ",(r)
        print estado
