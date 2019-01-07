import unittest
from DxfReader.DxfReader import DxfReader

class DxfReaderTest(unittest.TestCase):

    def test_GetSections(self):
        print("______sections_start_________")
        dxfReader = DxfReader("DxfReader/test/坡口图-2004版.dxf")
        sections = dxfReader.ParseSections()
        print(len(sections))
        for section in sections:
            print()
            print("section_start______")
            print(section)
            print("section_end______")
        print()
        print("______sections_end___________")