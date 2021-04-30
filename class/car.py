class Car():
    def __init__(self, maknish, model, guyn, sharjich, di, qshel):
        self.maknish = maknish 
        self.model = model
        self.guyn = guyn
        self.sharjich = sharjich
        self.di = di
        self.qshel = qshel

    def texekutyun(self):
        print("Maknishy - ", self.maknish)
        print("Modely - ", self.model)
        print("Guyny -", self.guyn, "e")
        print("Sharjichi ", self.sharjich, "litr e")
        print("Hzorutyuny - ", self.di, "diauj e")
    def yntacq(self):
        if self.qshel == 1:
            print("Yntanum e")
        elif self.qshel == 0:
            print("Kangnac e")
car1 = Car("BMW","Sedan", "Sev", 2.8 , 250, 1 )
car1.texekutyun()
car1.yntacq()
car2 = Car("Mercedes", "Crassover", "Arcataguyn", 2 , 300, 0)
car2.texekutyun()
car2.yntacq()