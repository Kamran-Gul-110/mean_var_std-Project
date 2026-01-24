import numpy as np


def calculate(input_list):
    try:

        array = np.array(input_list)
        reshaped = array.reshape(3, 3)

        dict = {
            "mean": [np.mean(reshaped, axis=0).tolist(), np.mean(reshaped, axis=1).tolist(), np.mean(reshaped).tolist()],
            "variance": [np.var(reshaped, axis=0).tolist(), np.var(reshaped, axis=1).tolist(), np.var(reshaped).tolist()],
            "standard deviation": [np.std(reshaped, axis=1).tolist(), np.std(reshaped, axis=0).tolist(), np.std(reshaped).tolist()],
            "max": [np.max(reshaped, axis=0).tolist(), np.max(reshaped, axis=1).tolist(), np.max(reshaped).tolist()],
            "min": [np.min(reshaped, axis=0).tolist(), np.min(reshaped, axis=1).tolist(), np.min(reshaped).tolist()],
            "sum": [np.sum(reshaped, axis=0).tolist(), np.sum(reshaped, axis=1).tolist(), np.sum(reshaped).tolist()],
        }
        print(dict)
    except ValueError:
        print("List must contain nine numbers.")


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
e = int(input("Enter 5th number: "))
f = int(input("Enter 6th number: "))
g = int(input("Enter 7th number: "))
h = int(input("Enter 8th number: "))
i = int(input("Enter 9th number: "))
input_list = [a, b, c, d, e, f, g, h, i]

calculate(input_list)
