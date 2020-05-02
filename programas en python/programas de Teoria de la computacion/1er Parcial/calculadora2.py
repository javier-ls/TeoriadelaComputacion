import math
while True:
        palabra=raw_input("Ingrese la operacion: \n Tome en cuenta:\n raiz=#\nelevacion=&:\n ") 
        if palabra == "":
             break
        palabra += ";"    
        estado="q0"
        n1 = ""
        n2 = ""
        op = ""
        nn2 = ""
    

        for en in palabra:
            if estado=="q0":
                if en in "0123456789":
                    estado="q1"
                    n1 = en
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q7"
                    n1 = en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="&" or en=="#":
                    print "error "
                    exit
                    estado="qr"
            
            elif estado=="q1":
                if en in "0123456789":
                    estado="q1"
                    n1 += en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="&" or en=="#" or en in "abcdefghijklmnopqrstuvxyz":
                    estado="qr"
                if en==" ":
                    estado="q2"
           
            
            elif estado=="q2":
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q3"
                    op = en
                if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="&" or en=="#":
                    estado="q4"
                    op += en
                if en in "0123456789" or en==";" or en==" ":
                    estado="qr"
            
            elif estado=="q3":
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q3"
                    op += en
                if en in "0123456789" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="&" or en=="#":
                    estado="qr"
                if en==" ":
                    estado="q5"
            
            elif estado=="q4":
                if en==" ":
                    estado="q5"
                if en in "0123456789" or en=="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="&" or en=="#":
                    estado="qr"

            elif estado=="q5":
                if en in "0123456789":
                    estado="q6"
                    n2 = en
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q8"
                    n2 = en
                if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="&" or en=="#":
                    estado="qr"
            
            elif estado=="q6":
                if en in "0123456789":
                    estado="q6"
                    n2 += en
                if en==";":
                    estado="qa"
                if en in "abcdefghijklmnopqrstuvxyz" or en=="+" or en=="-" or en=="*" or en=="/" or en=="&" or en=="#":
                    estado="qr"
            
            elif estado=="q7":
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q7"
                    n1 += en
                if en==" ":
                    estado="q2"
                if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="&" or en=="#":
                    estado="qr"
            
            elif estado=="q8":
                if en in "abcdefghijklmnopqrstuvxyz":
                    estado="q8"
                    n2 += en
                if en==";":
                    estado="qa"
                if en == " " or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="&" or en=="#":
                    estado="qr"
        print estado
       
        
            
        if estado=="qr":
                print ("Intentelo de Nuevo\n")
        if estado=="qa":
            if n1 == "uno":
              n1=1
            if n1 == "dos":
                n1=2
            if n1 == "tres":
                n1=3   
            if n1 == "cuatro":
                n1=4
            if n1 == "cinco":
                n1=5
            if n1 == "seis":
                n1=6
            if n1 == "siete":        
                n1=7         
            if n1 == "ocho":        
                n1=8
            if n1 == "nueve":      
                n1=9
            if n1 == "cero":
                n1=0
            
            if n2 == "uno":
              n2=1
            if n2 == "dos":
                n2=2
            if n2 == "tres":
                n2=3   
            if n2 == "cuatro":
                n2=4
            if n2 == "cinco":
                n2=5
            if n2 == "seis":
                n2=6
            if n2 == "siete":        
                n2=7         
            if n2 == "ocho":        
                n2=8
            if n2 == "nueve":      
                n2=9
            if n2 == "cero":
                n2=0

                
            if op == "mas":
                op="+" 
            if op == "menos":
                op="-" 
            if op == "por":
                op="*" 
            if op == "entre":
                op="/" 
            if op == "raiz":
                op="#" 
            if op == "potencia":
                op="&"
            if op=="coseno":
                op=="cos"
            if op=="seno":
                op="sen"
            if op=="tangente":
                op="tan"

            
           
            n1=int(n1)
            n2=int(n2)
        
            
      
            if op=="+" or op=="-" or op=="*" or op=="/" or op=="&" or op=="#" or op=="cos" or op=="sen" or op=="tan":
                if op=="+":
                    r=n1+n2
          
                elif op=="*":
                    r=n1*n2
            
                elif op=="-":
                    r=n1-n2
           
                elif op=="/":
                    r=n1/n2

                elif op=="#":
                    r=n1**1.0/n2
                
                elif op=="&":
                    r=n1**n2

                elif  op=="cos":
                    r=math.cos(n2)

                elif op=="sen":
                    r=math.sin(n2)

                elif op=="tan":
                    r=math.tan(n2)
      
            print ("El resultado de:  %s %s %s = %s\n" % (n1, op, n2, r))
