import pandas as pd


def hello() -> str:
    print(" not hello")
    return "hello"


x = pd.DataFrame()
hello()
print(x)
