def permutasiUnik(s):
    hasil = []
    s = sorted(s)
    digunakan = [False] * len(s)

    def backtrack(path):
        if len(path) == len(s):
            hasil.append(''.join(path))
            return
        for i in range(len(s)):
            if digunakan[i]:
                continue
            if i > 0 and s[i] == s[i-1] and not digunakan[i-1]:
                continue  # skip duplikasi
            digunakan[i] = True
            backtrack(path + [s[i]])
            digunakan[i] = False

    backtrack([])
    return hasil

# Input
S = input().strip()
hasil = permutasiUnik(S)
for p in hasil:
    print(p)