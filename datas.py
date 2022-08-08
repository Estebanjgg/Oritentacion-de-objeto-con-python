

class Data:
    
    def __init__(self, dia, mes, ano ):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def formato(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano ))