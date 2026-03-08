import unittest
from app.algorithms import (
    funnyString, alternatingCharacters, caesarCipher, 
    alternate, gridChallenge, ResultSubmitter, ProblemSolver
)

class SubmitterStub(ResultSubmitter):
    def __init__(self):
        self.submitted_data = {}

    def submit(self, problem_name, result):
        self.submitted_data[problem_name] = result
        return f"Stubbed: {problem_name} result {result} saved offline."

# ==========================================
# Test Cases 
# ==========================================
class TestHackerRankAlgorithms(unittest.TestCase):

    # --- Test Stub ---
    def test_stub_submission(self):
        stub = SubmitterStub()
        solver = ProblemSolver(stub)
        response = solver.solve_and_submit("FunnyString", funnyString, "acxz")
        
        self.assertIn("Stubbed", response)
        self.assertEqual(stub.submitted_data["FunnyString"], "Funny")

    # Grid Challenge Tests
    def test_gridChallenge_yes(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES") # จัดเรียงได้
        
    def test_gridChallenge_no(self):
        grid = ["mpxz", "abcd", "wlmm"]
        self.assertEqual(gridChallenge(grid), "NO") # จัดเรียงไม่ได้

    # Alternating Characters Tests
    def test_alternatingCharacters_no_deletions(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        
    def test_alternatingCharacters_all_same(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    # Caesar Cipher Tests
    def test_caesarCipher_normal_shift(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        
    def test_caesarCipher_large_shift(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    # Funny String Tests
    def test_funnyString_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny") # Normal case
        
    def test_funnyString_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny") # Defect case 

    # Two Characters Tests
    def test_alternate_success(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        
    def test_alternate_no_valid(self):
        self.assertEqual(alternate("abba"), 0)

if __name__ == '__main__':
    unittest.main()