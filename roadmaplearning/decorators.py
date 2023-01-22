# декораторы пизда

def bread(func):
    def wrapper():
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)


@bread
@ingredients
def sandwich(food="aaaaaa"):
    print(food)

print(sandwich())