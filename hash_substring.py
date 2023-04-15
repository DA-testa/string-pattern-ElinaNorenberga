# python3

def read_input():
    ievade = input()

    if ievade[0] == "F":
        textFile = "./tests/" +  input() 
        with open(textFile) as f: 
            return(f.readline().rstrip(), f.readline().rstrip())
    if ievade[0] == "I":
        return (input().rstrip(), input().rstrip())
    

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []

    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    d = 256
    q = 101 

    for i in range(M-1):
        h = (h*d) % q

    for i in range(M):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == M:
                occurrences.append(i)

        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % q

        if t < 0:
             t = t+q     

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

