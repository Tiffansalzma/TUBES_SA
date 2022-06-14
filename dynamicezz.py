import time
start_time = time.time()

def dynamic(n, k):
    result = [0] * (n+1)

    if (n==1) :
        result[1] = k
    elif (n==2) :
        result[2] = k * k
    else :
        result[1] = k
        result[2] = k * k
        for i in range(3,n+1):
            result[i] = ((k-1) * (result[i-1] + result[i-2]))
            print(result[i])
    
    return result[n]

n = 5
k = 5
print("Terdapat", dynamic(n,k), "kombinasi")
print("Waktu untuk menyelesaikan program ini adalah", time.time() - start_time, "detik")