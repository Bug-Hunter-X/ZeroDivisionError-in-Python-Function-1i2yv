def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

result = function(10, 0) #returns 0
result2 = function(10,2) # returns 5.0