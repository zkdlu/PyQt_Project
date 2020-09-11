class Preconditioning:
    def __init__(self, preTime, term, posture, met, clo, preEnvironment, bodyProfile, tsvCsvProfile):
        self.preCoreTemp = float(preTime / term) + 1, 16