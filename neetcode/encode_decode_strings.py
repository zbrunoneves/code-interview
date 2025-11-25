def encode(strs: list[str]) -> str:
    encoded = ""
    for w in strs:
        length = len(w)
        encoded += f"{length}#{w}"

    return encoded

def decode(s: str) -> list[str]:
    ans = []

    i = 0
    while i < len(s)-1:
        sep = s.index("#", i+1)
        length = int(s[i:sep])

        start = sep+1
        end = start+length
        ans.append(s[start:end])

        i = end

    return ans