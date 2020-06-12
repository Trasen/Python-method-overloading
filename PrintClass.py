from functools import singledispatchmethod
from Stringwrapper import StringWrapper


class PrintClass:
    @singledispatchmethod
    @classmethod
    def sayhi(cls, value): #Default base method for overloading, part of the Py3.8 specification/ documentation
        raise NotImplementedError("Value type has no overloaded method, please implement: " + value)

    @sayhi.register(int)
    @classmethod
    def overloadedsayhi(cls, value): #Overloaded method is allowed any name, except for in this case: sayHi(), that would throw an error that is hard to understand
        print(value + value + value + value)
        return value

    @sayhi.register(str)
    @classmethod
    def overloadedsayhi(cls, value):
        print(value + value)
        return

    @sayhi.register(StringWrapper)
    @classmethod
    def overloadedsayhi(cls, stringwrapper: StringWrapper):
        print(stringwrapper.internalstring1 + stringwrapper.internalstring2)
        return
