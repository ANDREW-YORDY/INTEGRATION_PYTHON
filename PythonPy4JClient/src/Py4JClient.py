
from py4j.java_gateway import JavaGateway

#Crear la conexión en el servidor Java.
gateway = JavaGateway()

#Confirmación de conexión activa, de Python.
print( "Test Desde Pyton" )

"""Invocando al método de Java de la clase JavaPy4JServer"""
response = gateway.entry_point.messageTest()
print( "Test, LLamada desde Python a: ", response )



"""MANEJO DE ERRORES, GENERADOS POR JAVA"""

try:
    error_response = gateway.entry_point.induceError(1) #Prueba con el error 1
    print( f"Respuesta de Java: {error_response}" )
except Exception as e:
    print( f"Error capturado de Java: \n {e}" )



