from PrintClass import PrintClass

test = PrintClass()
value: int = 123
test.sayhi(value)
test.sayhi("value")
test.sayhi(float(123)) #Will throw an error