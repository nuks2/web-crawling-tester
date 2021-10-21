class Person():
    def __init__(self, name):
        self.name = name

class MDPerson():
    def __init__(self, name):
        self.name = 'Docter ' + name

class JDPerson():
    def __init__(self, name):
        self.name = name + ', Esquire'

class EmailPerson():
    def __init__(self, name, email):
        super().__init__(name)
        self.emali = email

class Car():
    def exclaim(self):
        print('I am a car')

class Yugo(Car):
    def exclaim(self):
        print('I am a Yuo much like a car, but more yugo-ish')

    def need_a_push(self):
        print('a little help here?')


person = Person('fudd')
doctor = MDPerson('fudd')
lawyer = JDPerson('fudd')
email = EmailPerson('fudd', 'fudd@fudd.com')
print(person.name)
print(doctor.name)
print(lawyer.name)
print(email.name)


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.exclaim()