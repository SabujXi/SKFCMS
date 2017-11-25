def prefix_decorator_for_say(say_fun, prefix="Says: "):

    def wrapper_fun(w):
        print(prefix)
        say_fun(w)

    return wrapper_fun


# Normal Way
print("Normal Way")


def say(what):
    print(what)

say = prefix_decorator_for_say(say)

say("Hello")

print()
# Decorator Way
print("Decorator Way")


@prefix_decorator_for_say
def say2(what):
    print(what)

say2("Hello")


