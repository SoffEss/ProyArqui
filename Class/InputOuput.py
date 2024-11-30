## Clase de entrada y salida
# # Responsabilidades:
# # - Realiza operaciones de entrada y salida de datos.

class InputOutput:
    def __init__(self):
        self.value = 0
        self.mapeo_binario = {
            "buton1": "10",
        }
    
    def read(self, value):    
        return self.mapeo_binario.get(value, "0")
    
    def decode(self, value):
        ## Programa para encender el led
        instruction = ["LOAD R1, 10","SUB R1,"+value]
        return instruction

       