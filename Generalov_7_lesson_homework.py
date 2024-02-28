class Microbe:
    
    def __init__(self, name: str, form, lysis_diameter, long_flagellum, age):
        self.name = name
        self.form = form
        self.lysis_diameter = lysis_diameter
        self.long_flagellum = long_flagellum
        self.age = age
        print(self.name, self.form, self.lysis_diameter, self.long_flagellum)

    def grow_lysis(self):
        self.age += 1
        if self.long_flagellum > 5:
            self.lysis_diameter = self.lysis_diameter + self.age/2
        elif self.long_flagellum < 5 and self.long_flagellum > 2:
            self.lysis_diameter =self.lysis_diameter + self.age/10
        elif self.long_flagellum <= 2:
            self.lysis_diameter = self.lysis_diameter          
        return self.lysis_diameter

    def ifpathogenic(self):
        if self.lysis_diameter > 10 and self.long_flagellum > 0:
            return 'microbe is pathogenic'
        elif self.lysis_diameter <= 10 and self.lysis_diameter > 0:
            return 'microbe is  week pathogenic'
        else:
            return 'microbe is  non-pathogenic'
            
       

bacillus_1 = Microbe('Bacillus generalovi', 'bacillus', 0, 10, 0)
bacillus_2 = Microbe('Bacillus victory', 'bacillus', 0, 3, 0)
bacillus_3 = Microbe('Bacillus blastimi', 'bacillus', 0, 0, 0)

for day in range(10):
    print (f'ДЕНЬ РОСТА {day}')
    print (f"""{bacillus_1.name}  лизировал среду на {bacillus_1.grow_lysis()} мм.
           {bacillus_1.ifpathogenic()}""")
    print (f"""{bacillus_2.name}  лизировал среду на {bacillus_2.grow_lysis()} мм.
           {bacillus_2.ifpathogenic()}""")
    print (f"""{bacillus_3.name}  лизировал среду на {bacillus_3.grow_lysis()} мм.
           {bacillus_3.ifpathogenic()}""")
