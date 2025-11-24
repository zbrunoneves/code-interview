def group_anagrams(words: list[str]) -> list:
    groups={}
    for w in words:
        key = [0]*26
        for c in w:
            key[ord(c)-ord('a')]+=1
        key = tuple(key)

        groups[key] = groups.get(key, [])
        groups[key].append(w)

    return [x for x in groups.values()]