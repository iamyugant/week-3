import seaborn as sns
import pandas as pd


# update/add code below ...
def fibonacci(n):
    if n<=1:
        return n
    
    while n>1:
        x= fibonacci(n-1) + fibonacci(n-2)
        return x

print(fibonacci(9))



def to_binary(n):
    if n<=1:
        return n
    
    while n>1:
        