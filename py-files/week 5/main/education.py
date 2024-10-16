class Education:
    def __init__(self, inst, lev):
        self.institution = inst
        self.level = lev

    def print(self):
        print(self.institution, self.level)