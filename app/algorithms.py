class ResultSubmitter:
    def submit(self, problem_name, result):
        # โค้ดนี้สมมติว่าต้องต่อเน็ตไปส่งค่าให้เซิร์ฟเวอร์ HackerRank
        raise ConnectionError("Cannot connect to HackerRank server in real life!")

# Wrapper ที่เรียกใช้ Submitter
class ProblemSolver:
    def __init__(self, submitter: ResultSubmitter):
        self.submitter = submitter

    def solve_and_submit(self, problem_name, func, *args):
        result = func(*args)
        # ส่งผลลัพธ์ไปที่เซิร์ฟเวอร์
        return self.submitter.submit(problem_name, result)

# ==========================================

# Funny String
def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return "Not Funny"
    return "Funny"

# Alternating Characters
def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

# Caesar Cipher
def caesarCipher(s, k):
    res = []
    k = k % 26
    for char in s:
        if 'a' <= char <= 'z':
            res.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            res.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            res.append(char)
    return "".join(res)

# Two Characters
def alternate(s):
    chars = list(set(s))
    max_len = 0
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            c1, c2 = chars[i], chars[j]
            filtered = [c for c in s if c == c1 or c == c2]
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k-1]:
                    valid = False
                    break
            if valid:
                max_len = max(max_len, len(filtered))
    return max_len

# Grid Challenge
def gridChallenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row-1][col]:
                return "NO"
    return "YES"