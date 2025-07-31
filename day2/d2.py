def fibonacci(t):
    series = []
    a, b=0,1
    for _ in range (t):
        series.append(a)
        a,b =b,a +b
    return series
number=int(input("enter the number of terms"))
result= fibonacci(number)
print ("fibonacci series", result)