from stack import StaskLinkedList, SmartStackGetMin,SmartPlusStackGetMin

def priority_rule(c):
    if c in ["(", ")", "[", "]"]:
        return  11
    if c in ["*", "/"] :
        return  13
    if c in ["+", "-"]:
        return  12


exp = '5*2-(9+3)+6'
stack = StaskLinkedList()
operators = ["*", "/", "-", "+"]

def infix_to_postfix (expr):
    postfix = []
    for car in expr:
        if car in "0123456789" or car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # car is command
            postfix.append(car)

        elif car == "(":
             stack.push(car)

        elif car == ")" :
            top_car = stack.pop()
            while  top_car != "(":
                postfix.append(top_car)
                top_car = stack.pop()  # add characters if different to (

        else: #car is operator
            while (not stack.is_empty()) and priority_rule(car) <= priority_rule(stack.top()) :
                postfix.append(stack.pop()) #pop higher priority character inside de stack
            stack.push(car)

    while not stack.is_empty():
        postfix.append(stack.pop())

    print(postfix)
    return  postfix


# inf_post_expr = infix_to_postfix(exp)


def math_eval(op, op1, op2):
    if op == "+":
        return  op1+op2
    elif op == "-":
        return  op1-op2
    elif op == "*" :
        return  op1*op2
    else :
        try:
            return float(op1) / op2
        except ZeroDivisionError :
            print(ZeroDivisionError)

def eval_postfix_expression(expr):
    postfix_epr = expr
    print(postfix_epr)
    stack_operand = StaskLinkedList()
    operands = "0123456789"
    oper = ["*", "/", "-", "+"]

    for car in postfix_epr:
        if car in operands:
            stack_operand.push(float(car))
        elif car in oper:
            op2 = stack_operand.pop()
            op1 = stack_operand.pop()
            result = math_eval(car, op1, op2)
            stack_operand.push(result)

    print("result %.2f" % stack_operand.pop())


# eval_postfix_expression(inf_post_expr)
# infix_to_postfix(exp)



# problem 4 : how to evaluate infix expression in one pass :
#tip :  use 2 stack to evaluate infix expression directly
# exp = '5*2-(9+3)+6'
def eval_infix_expression(infix_expr):

    stack_operand = StaskLinkedList()
    stack_operator = StaskLinkedList()

    operands = "0123456789"

    for car in infix_expr:

        if car in operands:  # car is command
            stack_operand.push(float(car))

        elif car == "(":
            stack_operator.push(car)

        elif car == ")":
            top_car = stack_operator.pop()
            while top_car != "(": #pop operand character do de operation and put result in stack_operand
                op = top_car
                op2 = stack_operand.pop()
                op1 = stack_operand.pop()
                result = math_eval(op, op1, op2)
                stack_operand.push(result)

                top_car = stack_operator.pop()

        else:  # car is operator
            while (not stack_operator.is_empty()) and priority_rule(car) <= priority_rule(stack_operator.top()):
                op =  stack_operator.pop()  # pop higher priority character inside de stack
                op2 = stack_operand.pop()
                op1 = stack_operand.pop()
                result = math_eval(op, op1, op2)
                stack_operand.push(result)

            stack_operator.push(car)

    while not stack_operator.is_empty():
        op = stack_operator.pop()  # pop higher priority character inside de stack
        op2 = stack_operand.pop()
        op1 = stack_operand.pop()
        result = math_eval(op, op1, op2)
        stack_operand.push(result)

    r = stack_operand.pop()
    print("result : ", r)

# eval_infix_expression(exp)

#problem 5 : how to get min of stack in O(1)
smart_stack = SmartPlusStackGetMin()
smart_stack.push(2)
smart_stack.push(5)
smart_stack.push(1)
smart_stack.push(3)

print(smart_stack.get_min())
smart_stack.pop()
smart_stack.pop()


print(smart_stack.stack)
print(smart_stack.get_min())
