import unittest
import sys
import primepath

def getAnswer(filePath):
    with open(filePath, 'r') as fr:
        # flag = True
        answers = []
        for line in fr:
            if line[-1] == '\n':
                line = line[:-1]
            line = line[1:-1]
            if line.strip() != "": 
                line = line.strip().replace(' ','')
                data = map(int, line.split(','))
                answers.append(data)
                # print(data)
    answers = sorted(answers, key=lambda a: (len(a), a))
    return answers

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_add(self):
        # j = Count(2,3)
        path = sys.path[0]
        pathName = path + '/answer15.txt'
        answers = getAnswer(pathName)
        primePath = primepath.PrimePath()
        print(self.assertEqual(primePath.GetPath(), answers))

if __name__ == "__main__":
    unittest.main()
    # path = sys.path[0]
    # pathName = path + '/answer15.txt'
    # getAnswer(pathName)
