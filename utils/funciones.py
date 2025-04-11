import time
def slow_print(string):
    for character in string:
        time.sleep(0.015)
        if character == "." or character == "!" or character == "?":
            print(character, end="")
            i = input() # input para que le dé a enter cada que se muestre una línea de diálogo
        else:
            print(character, end="")