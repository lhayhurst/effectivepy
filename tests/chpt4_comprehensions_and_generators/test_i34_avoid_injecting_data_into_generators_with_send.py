# the send method can be used to inject data into a generator by giving the yield expression a value
# that can be assigned to a variable

# using send with yield expressions may cause surprising behavior, such as None values appearing at
# unexpected times in the generator output

# provide an input generator to a set of composed generators instead of using send
