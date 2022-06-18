def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            print('w is', w)
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
                # print('ans is', ans)
        return ans

s = 'abcd'
print(anagrams(s))
	