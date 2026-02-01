import unittest
from vault import hash_password 

class TestVault(unittest.TestCase):
    def test_hashing_uniqueness(self):
        salt1, hash1 = hash_password("password123")
        salt2, hash2 = hash_password("password123")
        
        self.assertNotEqual(hash1, hash2)
        self.assertNotEqual(salt1, salt2)

if __name__ == '__main__':
    unittest.main()