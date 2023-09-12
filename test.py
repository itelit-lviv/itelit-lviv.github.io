class Animal:
  def __init__(self,type,voice):
    self.type = type
    self.voice = voice
  def make_voice(self):
    print(self.voice)

class Cat:
    def catch_mouse(self):
        print("Киця зловила мишу")
        self.make_voice()
	

class Cat(Animal):
	def __init__(self, name, breed):
        super().__init__("кіт", "мяу!")
        self.name = name # ім'я кота
        self.breed = breed # порода 

    def catch_mouse(self):
        print("Киця зловила мишу")
        self.make_voice()

tom = Cat("кіт", "мяу!")
	
