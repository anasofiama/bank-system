from datetime import datetime
import pytz

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        print(datetime.now(pytz.timezone('America/Recife')))
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(pytz.timezone('America/Recife')).strftime("%d-%m-%Y %H:%M:%S"),
            }
        )