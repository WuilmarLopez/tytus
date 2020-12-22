from Expresion.Expresion import Expresion
from Expresion.Terminal import *
from Entorno import Entorno
import math
import random as rn
import hashlib
import base64
from reportes import *
from Tipo import Tipo

class FuncionesNativas(Expresion) :
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, identificador, expresiones) :
        Expresion.__init__(self)
        self.identificador = identificador
        self.expresiones = expresiones
        #print("en funci==========",self.identificador,self.expresiones[0])
        
    def getval(self,entorno):
        #print("++++++++++++++++++")
        sizeparametro = len(self.expresiones)
        funcion = self.identificador.lower()
       
        for param in self.expresiones:
            if isinstance(param,Terminal):
                if param.tipo.tipo=='identificador':
                    return  self
        
        #print("aqqqqqqqqqqqqq")
        try: 
            #print("retornamos el id")
            if(funcion=="abs" or funcion=="cbrt" or funcion=="ceil" or funcion=="ceiling" or 
            funcion=="degrees" or funcion=="exp" or funcion=="factorial" or funcion=="floor" or
            funcion=="ln" or funcion=="log" or funcion=="radians" or funcion=="sing" or 
            funcion=="trunc" or funcion=="acos" or funcion=="acosd" or funcion=="asin" or 
            funcion=="asind" or funcion=="atan" or funcion=="atand" or funcion=="cos" or
            funcion=="cosd" or funcion=="cot" or funcion=="cotd" or funcion=="sin" or 
            funcion=="sind" or funcion=="tan" or funcion=="tand" or funcion=="sinh" or
            funcion=="cosh" or funcion=="tanh" or funcion=="asinh" or funcion=="acosh" or 
            funcion=="atanh"
            ):
                valexpresion= self.expresiones[0].getval(entorno)
                return self.FunctionWithOneParameter(funcion,sizeparametro,valexpresion)
            elif(funcion=="div" or funcion=="gcd" or funcion=="mod" or funcion=="power" or 
                funcion=="round" or funcion=="atan2" or funcion=="atan2d"
                ):
                val1expresion = self.expresiones[0].getval(entorno)
                val2expresion = self.expresiones[1].getval(entorno)
                return self.FunctionWithTwoParameter(funcion,sizeparametro,val1expresion,val2expresion)
            elif(funcion=="width_bucket"):
                val1expresion = self.expresiones[0].getval(entorno)
                val2expresion = self.expresiones[1].getval(entorno)
                val3expresion = self.expresiones[2].getval(entorno)
                val4expresion = self.expresiones[3].getval(entorno)
                return self.FunctionWithBucket(funcion,sizeparametro,val1expresion,val2expresion,val3expresion,val4expresion)
        except:
             return "Error: La función: "+funcion+" solo recibe valores númericos"
     
        if(funcion=="length" or funcion=="md5" or funcion=="sha256" or funcion=="convert"):
            valexpresion= self.expresiones[0].getval(entorno)
            #print(valexpresion,'valooooor')
            return self.FunctionWithOneParameter(funcion,sizeparametro,valexpresion)
            
        elif(funcion=="get_byte" or funcion=="set_byte" or funcion=="encode" or funcion=="decode" or funcion=="trim" or funcion=="date_part"):
            val1expresion = self.expresiones[0].getval(entorno)
            val2expresion = self.expresiones[1].getval(entorno)
            return self.FunctionWithTwoParameter(funcion,sizeparametro,val1expresion,val2expresion)

        elif(funcion=="substr" or funcion=="substring" ):
            val1expresion = self.expresiones[0].getval(entorno)
            val2expresion = self.expresiones[1].getval(entorno)
            val3expresion = self.expresiones[2].getval(entorno)
            return self.FunctionWithTreeParameter(funcion,sizeparametro,val1expresion,val2expresion,val3expresion)
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"no existe",0, 0))
            return "Error: La función: "+funcion+" no existe"
        
    def FunctionWithOneParameter(self,funcion,parametros,exp):
        if(parametros==1):
            if(funcion=="abs"): 
                if(exp<0): 
                    return Terminal(Tipo('numeric',exp*-1,-1,-1),exp*-1)
                    
                else:
                    return Terminal(Tipo('numeric',exp,-1,-1),exp)

            elif(funcion=="cbrt"): 
                return Terminal(Tipo('decimal',math.pow(exp,3),-1,-1),math.pow(exp,3))

            elif (funcion=="ceil"): 
                return Terminal(Tipo('numeric',math.ceil(exp),-1,-1),math.ceil(exp))

            elif (funcion=="ceiling"): 
                return Terminal(Tipo('numeric',math.ceil(exp),-1,-1),math.ceil(exp))

            elif (funcion=="degrees"): 
                return Terminal(Tipo('decimal',math.degrees(exp),-1,-1),math.degrees(exp))

            elif (funcion=="exp"): 
                return Terminal(Tipo('numeric',math.exp(exp),-1,-1),math.exp(exp))
          

            elif (funcion=="factorial"): 

                return Terminal(Tipo('numeric',math.factorial(exp),-1,-1),math.factorial(exp))

            elif (funcion=="floor"): 
 
                return Terminal(Tipo('integer',math.floor(exp),-1,-1),math.floor(exp))

            elif (funcion=="ln"): 
                 return Terminal(Tipo('decimal',math.log(exp),-1,-1),math.log(exp))

                
            elif (funcion=="log"): 
                return Terminal(Tipo('decimal',math.log10(exp),-1,-1),math.log10(exp))

            elif (funcion=="radians"): 
                return Terminal(Tipo('decimal',math.radians(exp),-1,-1),math.radians(exp))

            elif (funcion=="sing"):
                if(exp>0):
                    return Terminal(Tipo('integer',1,-1,-1),1)

                else:
                    return Terminal(Tipo('integer',-1,-1,-1),-1)

            elif (funcion=="sqrt"): 
                return Terminal(Tipo('decimal',math.sqrt(exp),-1,-1),math.sqrt(exp))

            elif (funcion=="trunc"): 
                return Terminal(Tipo('numeric',math.trunc(exp),-1,-1),math.trunc(exp))

            elif (funcion=="acos"): 
    
                return Terminal(Tipo('decimal',math.acos(exp),-1,-1),math.acos(exp))

            elif (funcion=="acosd"): 
                return Terminal(Tipo('decimal',math.degrees(math.acos(exp)),-1,-1),math.degrees(math.acos(exp)))

            elif (funcion=="asin"): 
                return Terminal(Tipo('decimal',math.asin(exp),-1,-1),math.asin(exp))

            elif (funcion=="asind"): 
                return Terminal(Tipo('decimal',math.degrees(math.asin(exp)),-1,-1),math.degrees(math.asin(exp)))

            elif (funcion=="atan"): 
                return Terminal(Tipo('decimal',math.atan(exp),-1,-1),math.atan(exp))

            elif (funcion=="atand"): 
                return Terminal(Tipo('decimal',math.degrees(math.atan(exp)),-1,-1),math.degrees(math.atan(exp)))

            elif (funcion=="cos"): 
                return Terminal(Tipo('decimal',math.cos(exp),-1,-1),math.cos(exp))

            elif (funcion=="cosd"): 
                return Terminal(Tipo('decimal',math.degrees(math.cos(exp)),-1,-1),math.degrees(math.cos(exp)))

            elif (funcion=="cot"): 
                return Terminal(Tipo('decimal',(1/math.tan(exp)),-1,-1),(1/math.tan(exp)))

            elif (funcion=="cotd"): 
                return Terminal(Tipo('decimal',math.degrees(1/math.tan(exp)),-1,-1),math.degrees(1/math.tan(exp)))

            elif (funcion=="sin"): 
               
                return Terminal(Tipo('decimal',math.sin(exp),-1,-1),math.sin(exp))

            elif (funcion=="sind"): 
             
                return Terminal(Tipo('decimal',math.degrees(math.sin(exp)),-1,-1),math.degrees(math.sin(exp)))

            elif (funcion=="sin"): 
                return Terminal(Tipo('decimal',math.sin(exp),-1,-1),math.sin(exp))

            elif (funcion=="sind"): 
                return Terminal(Tipo('decimal',math.degrees(math.sin(exp)),-1,-1),math.degrees(math.sin(exp)))

            elif (funcion=="tan"): 
                return Terminal(Tipo('decimal',math.tan(exp),-1,-1),math.tan(exp))

            elif (funcion=="tand"): 
                return Terminal(Tipo('decimal',math.degrees(math.tan(exp)),-1,-1),math.degrees(math.tan(exp)))

            elif (funcion=="sinh"): 
                return Terminal(Tipo('decimal',math.sinh(exp),-1,-1),math.sinh(exp))

            elif (funcion=="cosh"): 
                return Terminal(Tipo('decimal',math.cosh(exp),-1,-1),math.cosh(exp))

            elif (funcion=="tanh"): 
                return Terminal(Tipo('decimal',math.tanh(exp),-1,-1),math.tanh(exp))

            elif (funcion=="asinh"): 
                return Terminal(Tipo('decimal',math.asinh(exp),-1,-1),math.asinh(exp))

            elif (funcion=="acosh"): 
                return Terminal(Tipo('decimal',math.acosh(exp),-1,-1),math.acosh(exp))

            elif (funcion=="atanh"): 
                return math.atanh(exp)
                return Terminal(Tipo('decimal',math.atanh(exp),-1,-1),math.atanh(exp))

            elif (funcion=="length"):
                 self.leng=len(exp)
                 return Terminal(Tipo('smallint',self.leng,-1,-1),self.leng)

            elif (funcion=="md5"):
                m=exp
                result = hashlib.md5(m.encode()) 
                return Terminal(Tipo('varchar',result.hexdigest(),-1,-1),result.hexdigest())
            elif (funcion=="sha256"):
                m=exp
                result= hashlib.sha256(m.encode()).hexdigest()
                return Terminal(Tipo('decimal',result,-1,-1),result)

            elif (funcion=="convert"):
                print("convert")
                 
            
                
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe un parametro"
    
    def FunctionWithTwoParameter(self,funcion,parametros,exp1,exp2):
        if(parametros==2):
            if (funcion=="div"):
                return Terminal(Tipo('decimal',exp1/exp2,-1,-1),exp1/exp2)

            elif (funcion=="gcd"): 
                return Terminal(Tipo('integer',math.gcd(exp1,exp2) ,-1,-1),math.gcd(exp1,exp2) )
      
            elif (funcion=="mod"):
                return Terminal(Tipo('integer',exp1%exp2,-1,-1),exp1%exp2)

            elif (funcion=="power"):
                return Terminal(Tipo('decimal',math.pow(exp1,exp2),-1,-1),math.pow(exp1,exp2))

            elif (funcion=="round"):
                return Terminal(Tipo('decimal',round(exp1,exp2),-1,-1),round(exp1,exp2))

            elif (funcion=="atan2"):
                return Terminal(Tipo('decimal',math.atan(exp1/exp2),-1,-1),math.atan(exp1/exp2))

            elif (funcion=="atan2d"):
                return Terminal(Tipo('decimal',math.degrees(math.atan(exp1/exp2)),-1,-1),math.degrees(math.atan(exp1/exp2)))

            elif (funcion=="encode"):
                if(exp2.lower()=="base64"):
                    cascci=exp1.encode('ascii')
                    codificado=base64.b64encode(cascci)
                    return Terminal(Tipo('varchar',codificado.decode('utf-8'),-1,-1),codificado.decode('utf-8'))

                elif (exp2.lower()=="hex"): 
                    cascci=exp1.encode('utf-8')
                    codificado=base64.b16encode(cascci)
                    return Terminal(Tipo('varchar',codificado.decode('utf-8'),-1,-1),codificado.decode('utf-8'))

                elif (exp2.lower()=="escape"):
                    codificado=exp1.encode('unicode_escape').decode('utf-8')
                    return Terminal(Tipo('varchar',codificado,-1,-1),codificado)

            elif (funcion=="decode"):
                if(exp2.lower()=="base64"):
                    codificado=base64.b64decode(exp1)
                    return Terminal(Tipo('varchar',codificado.decode('utf-8'),-1,-1),codificado.decode('utf-8'))

                elif (exp2.lower()=="hex"): 
                    codificado=base64.b16decode(exp1)
                    return codificado.decode('utf-8')
                    return Terminal(Tipo('varchar',codificado.decode('utf-8'),-1,-1),codificado.decode('utf-8'))

                elif (exp2.lower()=="escape"):
                    codificado=exp1.encode('utf-8').decode('unicode_escape')
                    return codificado
                    return Terminal(Tipo('varchar',codificado,-1,-1),codificado)

            elif(funcion=="date_part"):
                datepart=Date_Part(exp1, exp2)
                return datepart
                return Terminal(Tipo('integer',datepart,-1,-1),datepart)

        else:
 
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe 2 parametro"
    
    def FunctionWithTreeParameter(self,funcion,parametros,exp1,exp2,exp3):
        if(parametros==3):
            if (funcion=="substring"):
                inicio=exp2-1
                fin=inicio + exp3
                sub=exp1[inicio:fin]
                return Terminal(Tipo('decimal',sub,-1,-1),sub)

            elif (funcion=="substr"):
                inicio=exp2-1
                fin=inicio + exp3
                sub=exp1[inicio:fin]
                return Terminal(Tipo('decimal',sub,-1,-1),sub)
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 3 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe 3 parametro"
    
    def FunctionWithBucket(self,funcion,parametros,exp1,exp2,exp3,exp4):
        if(parametros==4):
            if(exp1<exp2 or exp1>exp3):
                reporteerrores.append(Lerrores("Error Semantico","Valor"+str(exp1)+"no se encuentra en el rango",0, 0))
                return "Error: El valor: "+str(exp1)+" no esta en el rango de: ("+str(exp2)+","+str(exp3)+")"
            else:
                contador = 1
                for x in range(exp2,exp3):
                    contador = contador+1
                
                columnas = int(contador/exp4)
                inicio = int(exp2)
                final = int(exp2)+(columnas) 
                posbucket = 0       
                for fila in range(0,exp4):
                    for valores in range(inicio,final):
                        if(exp1==valores):
                            posbucket = fila+1
                            return "El valor de: "+str(exp1)+" esta en el bucket: "+str(posbucket)
                    inicio=final
                    final=final+columnas    
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe 4 parametro"
            

class Date_Part(FuncionesNativas):
    'This is an abstract class'

    def __init__(self,field=None,interval=None):
        self.field=field
        self.interval=interval


    def getval(self,entorno):
        'spliteo el timestamp'
        splited=self.interval.getval(entorno).split(' ')
        cont=0
        for contenido in splited:
            if contenido == self.field:
                print(splited[cont-1])
                return splited[cont-1]
            cont=cont+1
        return None