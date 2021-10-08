if __name__ == "__main__":

    sum = 0

    for i in range(1, 1001):

        length = len(str(i))
        a = str(i)
        
        x = 0
        count = False

        for x in range(length):

            if a[x] == "5":
                count = True

            x += 1
        
        if count == False:

            sum += i


        i += 1

    print(sum)