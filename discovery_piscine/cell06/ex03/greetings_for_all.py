#define defalt parameter value for txt as "noble stranger"
def greetings(txt="noble stranger"):
    if not isinstance(txt, str):
        return print(f"Error! It was not a name.")
    else:
        return print(f"Hello, {txt}.")

greetings('Alexandra')
greetings('Wil')
greetings() #not send any arg, so it will use default parameter value
greetings(42)
