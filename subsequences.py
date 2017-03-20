def  buildSubsequences( s):
    subseq = []
    for i in range(len(s)):
        subseq.extend(testfn(s[:i]+s[i+1:]))
    return sorted(subseq)
def testfn(my_string):
    s_chars = []
    subseq = []
    for char in my_string:
        s_chars.append(my_string)
    if len(s_chars) == 1:
        return s_chars[0]
    if len(s_chars) == 2:
        return [s_chars[0], s_chars[1], s_chars[0]+s_chars[1]]
    for i in range[s_chars]:
        return testfn(my_string[:i] + my_string[i+1:])

print buildSubsequences("abc")