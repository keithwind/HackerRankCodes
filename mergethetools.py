def merge_the_tools(string, k):
    # your code goes here
    n=len(string)

    for i in range(0,n,k):
        stri=string[i:i+k]
        emp=''
        for c in stri:
            if c not in emp:
                emp+=c
        print(emp)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)