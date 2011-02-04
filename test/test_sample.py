import unittest


class SampleTests(unittest.TestCase):
  
  def setUp(self):
    self.value = 25
    
  def testSample(self):
    self.assertEqual(self.value/5, 5)