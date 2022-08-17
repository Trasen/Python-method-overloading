# Python method overloading
Basic proof of concept that it is in fact possible to work with some kind of type polymorphism in Python

While learning Python, coming from Java, C# and C++ i tend to favor established patterns/ polymorphism rather than ever growing if/else/switch control flows.

In Python this is done through annotations and secondary registres, it's not beautiful, but it does that it needs to do.

Limitations: You can only have 1 argument to the overloaded method - aka: (cls, argument), it's not possible to do (cls, argument, argument2>) at least at the moment.
