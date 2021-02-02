import textwrap
def wrap(n, m):
    s = ""
    message = "WELCOME"
    for i in range (1, int((n+1)/2)):
        s = s +  "-"*int((m-(3*(1+(i-1)*2)))/2)  +".|."*(1+(i-1)*2) + "-"*int((m-(3*(1+(i-1)*2)))/2) + "\n"
    s = s +  "-"*int((m-len(message))/2)   + message + "-"*int((m-len(message))/2) + "\n"
    for i in range (int((n-1)/2), 0,-1):
        s = s +  "-"*int((m-(3*(1+(i-1)*2)))/2)  +".|."*(1+(i-1)*2) + "-"*int((m-(3*(1+(i-1)*2)))/2) + "\n"
    return s

if __name__ == '__main__':
    data = input()
    n = int(data.split(" ")[0])
    m = int(data.split(" ")[1])
    print(wrap(n,m))
