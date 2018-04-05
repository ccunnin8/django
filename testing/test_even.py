import unittest

def isEven(n):
    return n % 2 == 0

class isEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertFalse(isEven(3))

def insert_val_at(index,my_list,value):
    if index > len(my_list) - 1 or index < 0:
        return False
    else:
        new_list = my_list
        new_list.insert(index,value)
    return new_list

class InsertValueTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [0,1,2,3,4]
        self.result = insert_val_at(2, self.test_list, 100)
        self.result2 = insert_val_at(6,self.test_list,100)
    def testInsertAtIndexTwo(self):
        return self.assertEqual([0,1,100,2,3,4], self.result)
    def testReturnFalseForInvalidIndex(self):
        return self.assertEqual(False, self.result2)
if __name__ == "__main__":
    unittest.main()
