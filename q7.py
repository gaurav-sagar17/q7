def gcd(a,b) :
    if(b == 0) :
        return abs(a) 
    
    return gcd(b,a%b)


def main() :
    count = 0
    pi = 3.14
    converge = 6/(pi**2)

    # n = int(input("enter value for n : ")) 
    for n in range(1,50) :
        for x in range(1,(n+1)//2) : 
            for y in range(1,(n+1)//2) :
                if(gcd(x,y) == 1) :
                    count += 1 
        count = count * 4

        # for x in range(1,(n+1)//2) :
        #     if(gcd(x,0)==1) :
        #         count += 1 
        # we already know thw answer of the above part only (1,0) will satsisfy
        count += 4 ## (1,0) ,(-1,0),(0,1),(0,-1) 
        # print(count)
        density = count/(n*n) 

        if(density >= (converge - 0.2*converge)  and density <= (converge + 0.2*converge)) :
            return n 
    
    print("please extend the range for n !!")

 

    
    
main()
        

