def is_anagram(a: str, b: str) -> bool:
    first = [0]*26
    second = [0]*26

    for c in a:
        i = ord(c)-ord('a')
        first[i]+=1

    for c in b:
        i = ord(c) - ord('a')
        second[i]+= 1

    return first == second