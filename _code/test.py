import pandas as pd

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4'
}

class MyClass:
    def my_function(self):
        print("Hello, world!")
        print("bye, world!")

    print("asdf, world!")
    print("fghj, world!")

# Create an instance of MyClass
my_instance = MyClass()

# Call the my_function method
my_instance.my_function()

"""
hello there



"""

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z'],
    'C': [True, False, True]
})
print(df)


def local_fn():
    a = 5
    b = 100

    print(a)

    c = a + b

    return c

import pandas as pdf

# create a dataframe with sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

df
