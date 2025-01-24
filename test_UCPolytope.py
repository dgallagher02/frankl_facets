import unittest
from UCPolytope import *

class TestUCPolytope(unittest.TestCase):

    def test_init(self):
        shape = UCPolytope(3, 3)
        self.assertEqual(shape.__repr__(), "Union Closed polytope(3, 3, built = False, integral = False)")

    def test_powerset(self):
        shape = UCPolytope(3, 3)
        self.assertEqual(shape.powerset, ((), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)))


    def test_union_closed(self):
        shape = UCPolytope(3,3)
        actual = [[(1,), (2,), (1,2)],[(1,), (3,), (1,3)], [(2,), (3,), (2,3)],[(1,), (2, 3), (1,2,3)], [(2,), (1,3), (1,2,3)], [(3,), (1,2), (1,2,3)],[(1,2), (1,3), (1,2,3)], [(1,2), (2,3), (1,2,3)], [(1,3), (2,3), (1,2,3)]]

        # actual = [set([(1,), (2,), (1,2)]), set([(1,), (3,), (1,3)]), set([(2,), (3,), (2,3)]),
        # set([(1,), (2, 3), (1,2,3)]), set([(2,), (1,3), (1,2,3)]), set([(3,), (1,2), (1,2,3)]),
        # set([(1,2), (1,3), (1,2,3)]), set([(1,2), (2,3), (1,2,3)]), set([(1,3), (2,3), (1,2,3)])]
        self.assertEqual(len(shape.union_closed_ab()), 9)

    def test_union_closed_4(self):
        shape = UCPolytope(4,4)
        #len comes from 4 choose 2 + 6 choose 2 + 4 choose 2 + 4 (from single and triple) + 4*3 (from triple and double) + 6*2
        self.assertEqual(len(shape.union_closed_ab()), 55)

    def test_max_occ(self):
        shape = UCPolytope(3,3)
        self.assertEqual(len(shape.less_than_max_occurence()), 3)

    def test_max_occ_4(self):
        shape = UCPolytope(4,4)
        self.assertEqual(len(shape.less_than_max_occurence()), 4)



if __name__ == "__main__":
    unittest.main()