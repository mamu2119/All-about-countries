class India():
    def capital(self):
        print("New Delhi Is the capital of India!")
    def language(self):
        print("Hindi is the widely spoken language of India.")
    def type(self):
        print("India is a developing country!!!")
class USA():
    def capital(self):
        print("Washingtoon, D.C. is the capital of USA!")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is the developed country!!!")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()