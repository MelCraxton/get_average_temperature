def temperatures():
    with open('files/temperatures.txt', 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]
    total = round(sum(values)/len(values),2)
    return total


output = temperatures()
print(output)