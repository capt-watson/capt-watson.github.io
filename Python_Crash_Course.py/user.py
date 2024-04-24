

class User:
    def __init__(self, name, last, age, nationality):
        self.name = name
        self.last = last
        self.age = age
        self.nationality = nationality
        
    def describe_user(self):
        print(f"\nAdmin name is {self.name.title()}, last name is {self.last.title()}, age is {self.age} and is of {self.nationality.title()} nationality\n")
        
    def greet_user(self):
        print(f"\nHello! {self.name.title()}, welcome to the Tata Consultancy Services Ltd.\n")
        
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
            print("Privileges of the admin are:\n")
            for privilege in self.privileges:
                print(f"- {privilege}")

class Admin(User):
    def __init__(self, name, last, age, nationality, privileges):
        super().__init__(name, last, age, nationality)
        self.privileges = Privileges(privileges)
