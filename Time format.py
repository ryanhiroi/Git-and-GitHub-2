if __name__ == "__main__":
    d = int(input())

    h = d // 3600
    d = d % 3600

    m = d // 60
    s =  d % 60 

    print ( h, m, s )
