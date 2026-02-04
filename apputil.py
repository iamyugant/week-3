import seaborn as sns
import pandas as pd


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
        x= n%2 + 10*to_binary(n//2)
        return x         
print(to_binary(18))


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

df_bellevue