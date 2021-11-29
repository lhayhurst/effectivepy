# classes also support polymorphic behavior in method.
# this two are not the same thing in Python!

# class polymorphism enables classes in a hierarchy to implement their own unique versions of a method
# this allows class instances to vary their implementation but still provide the same abstract public interface

# he gives as a very long example an input into a map reduce function for which it is unreasonable to expect
# every single input subclass to provide the same constructor argument, which is a good example of a common
# pain point when writing object oriented code: because everyone is the same, you can't reap the benefits of
# real polymorphic semantics while programming. or, stated more practically:

# you only get one __init__() function signature.

# or ... do you? enter: classmethod polymorphism

# his hypothetical example is a map reduce program where he wants polymorphmic behavior from both his workers
# and the input data that those workers take in.
