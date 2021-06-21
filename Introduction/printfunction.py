if __name__ == '__main__':
    n = int(input())
    ar=range(1,n+1)
    for i in ar:
        print(i,end="")
        
        
"""
Alternate solution:
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep ='')
"""
