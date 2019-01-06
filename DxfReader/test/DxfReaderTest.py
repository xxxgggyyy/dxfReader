import unittest
from DxfReader.DxfReader import DxfReader

class DxfReaderTest(unittest.TestCase):

    def test_GetSections(self):
        print("______sections_start_________")
        dxfReader = DxfReader("DxfReader/test/test.dxf")
        for section in dxfReader.GetSections():
            print()
            print("section_start______")
            print(section)
            print("section_end______")
        print()
        print("______sections_end___________")