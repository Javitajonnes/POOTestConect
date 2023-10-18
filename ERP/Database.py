import mysql.connector

class Database():
    def __init__(self):
            self.conexion=mysql.connector.connect(
                host='localhost',
                user='root',
                password='inacap2023',
                database='empresa')
            self.cursor=self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()  

    def select_todos(self):
        sql='select * from repuestos'
        try:
            self.cursor.execute(sql)
            repu=self.cursor.fetchall() #devuelve una tupla con los registros
            print('Código\tNombre de Repuesto\tFecha Fabr.\tPrecio Proveed. Precio de venta Peso')
            for rep in repu:
                print(rep[0],rep[1],'\t\t',rep[2].strftime('%d/%m/%Y'),'\t',rep[3],'\t',rep[4],'\t',rep[5])
        except Exception as err:   #captura el error y lo asigna a err
            print(err)

    def select_uno(self,cod):
        sql='select* from repuestos where codrep='+repr(cod)
        try:
            self.cursor.execute(sql)
            rep=self.cursor.fetchone()
            if rep!=None:
                print('Código\tNombre de Repuesto\tFecha Fabr.\tPrecio Proveed. Precio de venta Peso')
                print(rep[0],rep[1],'\t\t',rep[2].strftime('%d/%m/%Y'),'\t',rep[3],'\t',rep[4],'\t',rep[5])
            else:
                print('Codigo no esta')
        except Exception as err:
            print(err)            

    def insert(self):
        codR=input('codigo=')
        sql1='select codrep from repuestos where codrep='+repr(codR)
        try:
            self.cursor.execute(sql1)    
            if self.cursor.fetchone()==None: #si el codigo no existe(none)
                nomR=input('Nombre=')
                fechaF=input('Fecha de fabricacion (dd/mm/aaaa)=')
                precioProv=float(input('Precio de Proveedor='))
                precioVen=float(input('Precio de Venta='))
                peso=float(input('Peso(Kg)='))
                sql2="insert Into repuestos value("+repr(codR)+","+repr(nomR)+\
                ",str_to_date("+repr(fechaF)+",'%d/%m/%y'),"+repr(precioProv)+\
                ","+repr(precioVen)+","+repr(peso)+","
            try:
                self.cursor.execute(sql2)
                self.conexion.commit()
            except Exception as err:
                self.conexion.rollback()
                print(err)
            else:
                print('Ya existe ese codigo')
        except Exception as err:
                print(err)
               
    def eliminar(self):
        codR=input('Código=')
        sql1='select * from repuestos where codrep='+repr(codR)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone()!=None:  #valida que el código exista
                sql2='select * from ventas where codrepuesto='+repr(codR)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchone()!=None:   #si el código está en Vendido
                        print('No se puede eliminar, porque está en la tabla Ventas')
                    else:
                        sql3 = 'delete from repuestos where codrep='+repr(codR)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print('No existe ese código')
        except Exception as err:
            print(err)