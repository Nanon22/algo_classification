# "python -m unittest test" to run test

import unittest

from recommand_data import critics, eucli, pearson, similarity

class test_compare(unittest.TestCase):

    def test1_eucli(self):
        self.assertEqual(eucli(critics['Lisa Rose'], critics['Gene Seymour']), 0.29429805508554946)

    def test2_pearson(self):
        self.assertEqual(pearson(critics['Lisa Rose'], critics['Michael Phillips']), 0.40451991747794525)
        self.assertEqual(pearson(critics['Lisa Rose'], critics['Toby']), 0.9912407071619304)

    def test3_similarity(self):
        self.assertEqual(similarity(critics, "Toby"), {'Just My Luck': 2.5309807037655645, 'Lady in the Water': 2.8325499182641614, 'The Night Listener': 3.3477895267131013})

if __name__ == '__main__':
    unittest.main()