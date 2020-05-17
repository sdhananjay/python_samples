def square(x):
    return x * x


def my_map(f, my_list):
    results = []
    for i in my_list:
        results.append(f(i))
    return results

results = my_map(square, [1,2,3,4,5])
print(results)
