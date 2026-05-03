class Field:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class User:
    username = Field() # __set_name__ called here, sets name to "_username"

u = User()
u.username = "admin"
print(u.__dict__) # {'_username': 'admin'}