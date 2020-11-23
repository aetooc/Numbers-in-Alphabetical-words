# Syntax--> n should be a digit
            ftn(1,0)= one
            ftn(10,0)= ten
            ftn(60,6)= sixty six

def ftn(n,m):
    num_names = {
        0:" ",
        1 :"one", 
        2:"two", 
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"tweleve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty", 
        30:"thirty",
        40:"fourty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninty",
        100:"hundered"
    }
    n=num_names[n]
    m=num_names[m]
    print(n,m)
