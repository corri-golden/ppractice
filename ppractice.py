corri_shoes = list()

corri_shoes.append("Nike")

corri_shoes.append("Reebox")

# print(corri_shoes)

def corri_guest(first_name, last_name, age):
    return{
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
    }



melissa = corri_guest("Lina", "Bracamonte", 34)
doug = corri_guest("Doug", "McCall", 12)



def run(name):
    print(f'{name} ran like a drunk man')
def swing(name):
    print(f'{name} swing like a little girl')
def slide(name):
    print(f'{name} slide slow')
def hide_and_seek(name):
    print(f'{name} hide and seek with girls')

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# for kid in running_kids:
    
# for kid in swinging_kids:
#     swing(kid)

# for kid in sliding_kids:
#     slide(kid)

# for kid in hiding_kids:
#     hide_and_seek(kid)


# for i in range(1, 101):
    
#     if i % 5 == 0 and i % 7 == 0: 
#         print("ChickenMonkey")
#     elif i % 7 == 0:
#         print("Monkey")
#     elif i % 5 == 0:
#         print("Chicken")
#     else:
#         print(i)

# for i in range(1, 101):
   
#     if i % 5 == 0 and i % 7 == 0:
#         print("ChickenMonkey")
#     elif i % 5 == 0:
#         print("Chicken")
#     elif i % 7 == 0:
#         print("Monkey")


# overriding
class Foo:
    def __init__(self):
        self.name = "Bubba"

    def __str__(self):
        return self.name

dude = Foo()
print(dude)



