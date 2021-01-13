class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def print_score(self):
        print('%s %s' % (self.name,self.__score))
    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B' 
        else:
            return 'C'
bart = Student('Bart Smipson',59)
lisa = Student('Lisa Smipson',78)
bart.print_score()
bart.__score = 90
bart.print_score()
lisa.print_score()
print(lisa.get_grade(),bart.get_grade())