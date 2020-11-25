import unittest

from solution.wchain import WChain

path = '../test_files/'


class WChainTest(unittest.TestCase):

    def test_chain1(self):
        w = WChain()
        self.assertEqual(6, w.count_chains(path + "wchain1.in"))

    def test_chain2(self):
        w = WChain()
        self.assertEqual(4, w.count_chains(path + "wchain2.in"))

    def test_chain3(self):
        w = WChain()
        self.assertEqual(1, w.count_chains(path + "wchain3.in"))

    def test_chain4(self):
        w = WChain()
        self.assertEqual(4, w.count_chains(path + "wchain4.in"))

    if __name__ == '__main__':
        unittest.main()
