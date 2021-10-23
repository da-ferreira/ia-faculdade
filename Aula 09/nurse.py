
import numpy as np

class NurseSchedulingProblem:
    """
    Esta classe encapsula o Nurse Schedulling Problem
    """

    def __init__(self, penalidade_HardConstraint):
        self.penalidade_HardConstraint = penalidade_HardConstraint

        # Lista de funcionarios:
        self.profissional = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
                             'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
                             'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
                             'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
                             'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6']

        # Preferencia de turno dos funcionarios - manha, tarde, noite:
        self.preferenciaDeTurno = [[1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                                   [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                                   [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                                   [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                                   [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                                   [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], 
                                   [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1]]

        # Numeros minimos e maximos de funcionarios por turno - manha, tarde, noite
        self.minTurno = [10, 8, 8]
        self.maxTurno = [18, 14, 10]

        # Numero maximo de turnos que um profissional pode fazer por semana
        self.turnosMaxSemana = 5

        # Numero maximo de semanas que schedule irah cobrir
        self.semanas = 1

        # valores uteis:
        self.turnosPorDia = len(self.minTurno)
        self.turnosPorSemana = 7 * self.turnosPorDia

    def __len__(self):
        """
        :return: numero de turnos de um  schedule
        """
        return len(self.profissional) * self.turnosPorSemana * self.semanas


    def calculaCusto(self, schedule):
        """
        Calcula o valor total das violacoes de um dado schedule
        """

        # Converte todo o schedule em um dicionario com um schedule separado para cada funcionario
        dicionarioTurnos = self.turnosPorProfissional(schedule)
        #print(dicionarioTurnos)

        # Calcula o custo de cada uma das violacoes:
        violacoesTurnosSeguidos = self.contaViolacoesTurnosSeguidos(dicionarioTurnos)
        violacoesTurnosPorSemana = self.contaViolacoesTurnosPorSemana(dicionarioTurnos)[1]
        violacoesProfissionalPorTurno = self.contaViolacoesProfissionalPorTurno(dicionarioTurnos)[1]
        violacoesPreferenciaDeTurno = self.contaViolacoesPreferenciaDeTurno(dicionarioTurnos)

        # calcula os custos totais das violacoes:
        ViolacoesHard = violacoesTurnosSeguidos + violacoesProfissionalPorTurno + violacoesTurnosPorSemana
        ViolacoesSoft = violacoesPreferenciaDeTurno

        return self.penalidade_HardConstraint * ViolacoesHard + ViolacoesSoft

    def turnosPorProfissional(self, schedule):
        """
        Converte toda o schedule em um dicionário com uma programação separada para cada profissonal
        """
        turnoPorProfissional = self.__len__() // len(self.profissional)
        dicionarioTurnos = {}
        indiceTurnos = 0

        for prof in self.profissional:
            dicionarioTurnos[prof] = schedule[indiceTurnos:indiceTurnos + turnoPorProfissional]
            indiceTurnos += turnoPorProfissional

        return dicionarioTurnos

    def contaViolacoesTurnosSeguidos(self, dicionarioTurnos):
        """
        Calcula o numero de turnos seguidos no schedule
        """
        violacoes = 0
        # analisa os turnos de cada profissional:
        for turnosProf in dicionarioTurnos.values(): #todos os turnos de um profissional
            # procura por '1's seguidos
            for turno1, turno2 in zip(turnosProf, turnosProf[1:]):
                if turno1 == 1 and turno2 == 1:
                    violacoes += 1

        return violacoes

    def contaViolacoesTurnosPorSemana(self, dicionarioTurnos):
        """
        Calcula o numero de violacoes do tipo numero maximo de turnos no schedule
        """
        violacoes = 0
        listaTurnoSemanais = []
        # analisa os turnos de cada profissional
        for turnosProf in dicionarioTurnos.values(): #todos os turnos de um profissional
            # percorre todos os turnos de uma semana:
            for i in range(0, self.semanas * self.turnosPorSemana, self.turnosPorSemana):
                # conta todos os '1's de uma semana:
                turnosDaSemana = sum(turnosProf[i:i + self.turnosPorSemana])
                listaTurnoSemanais.append(turnosDaSemana)
                if turnosDaSemana > self.turnosMaxSemana:
                    violacoes += turnosDaSemana - self.turnosMaxSemana

        return listaTurnoSemanais, violacoes

    def contaViolacoesProfissionalPorTurno(self, dicionarioTurnos):
        """
        Conta as violacoes de falta de profissional por turno (nr de profissional menor 
        que o minimo desejado) 
        """
        # lista com o  total profissionais por turno
        listaTotalDeProf = [sum(turno) for turno in zip(*dicionarioTurnos.values())]

        violacoes = 0
        # percorre todos os turnos e conta as violacoes:
        for indiceTurnos, nrDeProfissionais in enumerate(listaTotalDeProf):
            indiceTurnoDiario = indiceTurnos % self.turnosPorDia  # -> 0, 1, ou 2 para os 3 turnos diarios
            if (nrDeProfissionais > self.maxTurno[indiceTurnoDiario]):
                violacoes += nrDeProfissionais - self.maxTurno[indiceTurnoDiario]
            elif (nrDeProfissionais < self.minTurno[indiceTurnoDiario]):
                violacoes += self.minTurno[indiceTurnoDiario] - nrDeProfissionais

        return listaTotalDeProf, violacoes

    def contaViolacoesPreferenciaDeTurno(self, dicionarioTurnos):
        """
        Conta o numero de violacoes das preferencias dos profissionais
        """
        violacoes = 0
        for indiceProf, turnosDePrefereridos in enumerate(self.preferenciaDeTurno):
            preferencias = turnosDePrefereridos * (self.turnosPorSemana // self.turnosPorDia)
            # percorre os turnos e compara com as preferencias:
            turnos = dicionarioTurnos[self.profissional[indiceProf]]
            for pref, turno in zip(preferencias, turnos):
                if pref == 0 and turno == 1:
                    violacoes += 1
        return violacoes

    def printScheduleInfo(self, schedule):
        """
        Mostra o Schedule e as violacoes
        """
        dicionarioTurnos = self.turnosPorProfissional(schedule)

        print("Schedule de cada profissional:")
        for prof in dicionarioTurnos:  # todos os turnos de um profissional
            print(prof, ":", dicionarioTurnos[prof])

        print(f"\n(Hard constraint) Violações de turnos consecutivos: {self.contaViolacoesTurnosSeguidos(dicionarioTurnos)}")
        print()

        listaTurnoSemanais, violacoes = self.contaViolacoesTurnosPorSemana(dicionarioTurnos)
        print(f"(Hard constraint) Violacões do limite máximo de turnos semanais: {violacoes}")
        print(f"Turnos semanais: {listaTurnoSemanais}")
        print()

        listaTotalDeProf, violacoes = self.contaViolacoesProfissionalPorTurno(dicionarioTurnos)
        print(f"(Hard constraint) Violacões do limite mínimo de profissionais por turno: {violacoes}")
        print(f"Profissionais por Turno: {listaTotalDeProf}")
        print()

        violacoesPreferenciaDeTurno = self.contaViolacoesPreferenciaDeTurno(dicionarioTurnos)
        print(f"(Soft constraint) Violacões das preferencias pessoais: {violacoesPreferenciaDeTurno}")
        print()


if __name__ == "__main__":
    # Cria uma instancia do problema
    prof = NurseSchedulingProblem(10)

    solucaoAleatoria = np.random.randint(2, size=len(prof))
    print("Solucao Aleatoria = ")
    print(solucaoAleatoria)
    print()

    prof.printScheduleInfo(solucaoAleatoria)

    print("Custo Total = ", prof.calculaCusto(solucaoAleatoria))
                