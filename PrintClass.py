from functools import singledispatchmethod


class PrintClass:
    @singledispatchmethod
    @classmethod
    def sayhi(cls, value): #Default base method for overloading, part of the Py3.8 specification/ documentation
        raise NotImplementedError("Wrong type for import: " + value)

    @sayhi.register(int)
    @classmethod
    def overloadedSayHi(cls, value): #Overloaded method is allowed any name, except for in this case: sayHi(), that would throw an error that is hard to understand
        print("hi from int overloading")
        print(value + value + value + value)
        return value

    @sayhi.register(str)
    @classmethod
    def overloadedSayHi(cls, value):
        print("hi from string overloading")
        print(value + value)
        return

