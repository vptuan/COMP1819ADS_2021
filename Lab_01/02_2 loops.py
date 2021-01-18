

def stairs2(n, a = 1):
    for a in range(1,n + 1):
        
        for i in range(n - a):
            print(" ", end = "");
        #print(n);
        
        for i in range(a):
            print("#", end = "");

        print("");

stairs2(4);   
