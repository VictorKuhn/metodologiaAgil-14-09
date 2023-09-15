from datetime import datetime, timedelta


class CalculadoraHoras:
    def __init__(self):
        self.registros = {}
        self.intervalos = {}

    def inserir_horarios(self, data, entrada, saida):
        # Validação do formato H:mm ou HHmm
        if not self.validar_formato_horario(entrada) or not self.validar_formato_horario(saida):
            return "Erro: Formato de horário inválido. Use H:mm ou HHmm."

        # Adicionar ":" se o formato for H:mm
        entrada, saida = self.adicionar_dois_pontos_se_necessario(entrada), self.adicionar_dois_pontos_se_necessario(
            saida)

        # Registra os horários
        if data not in self.registros:
            self.registros[data] = {"entrada": entrada, "saida": saida}
        else:
            self.registros[data]["entrada"] = entrada
            self.registros[data]["saida"] = saida

        # Retorna None em caso de sucesso
        return None

    def inserir_intervalo(self, data, duracao_intervalo):
        # Validação do formato H:mm ou HHmm
        if not self.validar_formato_horario(duracao_intervalo):
            return "Erro: Formato de duração de intervalo inválido. Use H:mm ou HHmm."

        # Adicionar ":" se o formato for H:mm
        duracao_intervalo = self.adicionar_dois_pontos_se_necessario(duracao_intervalo)

        # Registra a duração do intervalo
        self.intervalos[data] = duracao_intervalo

    def adicionar_dois_pontos_se_necessario(self, horario):
        # Adiciona ":" se o horário está no formato H:mm (sem dois pontos)
        if len(horario) == 3:
            return horario[0] + ":" + horario[1:]
        return horario

    def validar_formato_horario(self, horario):
        try:
            datetime.strptime(horario, "%H:%M")
            return True
        except ValueError:
            try:
                datetime.strptime(horario, "%H%M")
                return True
            except ValueError:
                return False

    def calcular_horas_trabalhadas(self):
        horas_trabalhadas = 0
        for data, registro in self.registros.items():
            if registro["entrada"] and registro["saida"]:
                entrada = datetime.strptime(registro["entrada"], "%H:%M")
                saida = datetime.strptime(registro["saida"], "%H:%M")

                # Verifica se o horário de término é anterior ao de entrada
                if saida < entrada:
                    diferenca = timedelta(hours=24) - (entrada - saida)
                else:
                    diferenca = saida - entrada

                horas_trabalhadas += diferenca.total_seconds() / 3600

        # Desconto do intervalo
        for data, duracao in self.intervalos.items():
            duracao = datetime.strptime(duracao, "%H:%M")
            horas_trabalhadas -= duracao.hour + duracao.minute / 60

        return horas_trabalhadas

    def calcular_total_horas_trabalhadas(self):
        return round(self.calcular_horas_trabalhadas(), 2)