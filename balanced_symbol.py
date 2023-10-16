from stack import StaskLinkedList

s = "(ere[try{uu}iu]uoo)iuo"

opening_symbol = ["(", "[", "{"]
close_symbol = [ ")", "]", "}"]
stack = StaskLinkedList()
characters = []

def matches(open_car, close_car) -> bool :
    if open_car == "{" and close_car == "}" :
        return True
    if open_car == "[" and close_car == "]" :
        return  True
    if open_car == "(" and close_car == ")" :
        return  True

    return  False

def balance_symbol(sentence):
    balance = 1
    for e in sentence:
        print(e)
        if e in opening_symbol:
            stack.push(e)
        elif e in close_symbol :
            if stack.is_empty():
                # raise Exception("not balancing symbol. Empty stack")
                balance = 0
                break
            elif not matches(stack.pop(), e):
                # raise Exception("not balance ce symbol. Not match balanced symbol")
                balance = 0
                break
        else:
            characters.append(e)

    if not stack.is_empty():
        # raise Exception("not balance symbol. Stack is not empty at end.")
        balance = 0
    else:
        print("Your sentence is balance!")
        print("characters meet :", characters)
        return balance

print(f"Balance status : { balance_symbol(s) } ")