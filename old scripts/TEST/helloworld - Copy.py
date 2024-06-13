
possible_inputs = ["hello", "hi", "hey"]
greeting = input("Hello world\n")
while greeting != possible_inputs:
    greeting = input("(you're supposed to say hello back lol)\n")
while greeting == possible_inputs:
    break
