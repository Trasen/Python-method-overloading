from PrintClass import PrintClass
from Stringwrapper import StringWrapper

test = PrintClass()
value: int = 123
test.sayhi(value)
test.sayhi("value")
test.sayhi(StringWrapper("Testing using wrapper", ": Seems to be working"))