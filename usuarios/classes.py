from django.core.mail import send_mail
import random


class Email():
        def __init__(self):
            self.codigo = None

        def mandarEmail(self, destino):
            send_mail('codigo', f'O código é {self.codigo}',  None, [destino], fail_silently=False)
        
        def mudarCodigo(self):
            self.codigo = ''
            while len(self.codigo) < 7:
                self.codigo += str(random.randint(0, 9))