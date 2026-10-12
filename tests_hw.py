
from unittest import TestCase,main
from hw import MyStackInt


class MyTestCase(TestCase):
    def setUp(self):
        self.stack = MyStackInt()


    def test_push(self):

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(),2) #ACTUAL/EXPECTED
        self.assertEqual(self.stack.pop(),1)

    def test_pop(self):

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.assertEqual(len(self.stack),2)
        self.stack.pop()
        self.assertEqual(len(self.stack),1)

    def test_max_is_changed(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.max(),2)
        self.stack.push(3)
        self.stack.push(8)
        self.stack.pop()
        self.assertEqual(self.stack.max(),3)



    def test_max_is_equal(self):
        self.stack.push(11)
        self.stack.push(11)
        self.stack.push(3)
        self.assertEqual(self.stack.current_max[-1],11)
        self.assertEqual(self.stack.max(),11)

        self.stack.pop()
        self.assertEqual(self.stack.current_max[-1],11)
        self.stack.pop()
        self.assertEqual(self.stack.max(),11)



    def test_is_empty_stack(self):
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(len(self.stack),0)

        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_negative_stack(self):
        self.stack.push(-1)
        self.stack.push(-11)
        self.stack.push(-19)
        self.stack.push(-3)
        self.assertEqual(self.stack.max(),-1)

    def test_is_stacks_equal(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack),len(self.stack.current_max))
        self.stack.pop()
        self.assertEqual(len(self.stack),len(self.stack.current_max))

    def test_empty_max_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.max()







if __name__ == '__main__':
    main()