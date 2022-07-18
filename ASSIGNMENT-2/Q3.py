def fib(num):
    n1=0
    n2=1
    if num==1 or num==0:
        print(num)
    else:
            print(n1)
            print(n2)
            for i in range(2,num):
                nth=n1+n2
                n1=n2
                n2=nth
                print(nth)

            fib(10)
            

