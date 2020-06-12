from PrintClass import PrintClass
from Stringwrapper import StringWrapper

test = PrintClass()
test.sayhi("value")
test.sayhi(StringWrapper("Testing using wrapper", ": Seems to be working"))
test.sayhi(123)
test.sayhi(float(123)) #Will throw an error
