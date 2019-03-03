import unittest
from ..DxfReader import DxfReader
from ..Sections import HeaderSection

class HeaderTest(unittest.TestCase):

    def test_header_vars(self):
        dxfReader = DxfReader("DxfReader/test/test.dxf")
        sections = dxfReader.ParseSections()
        print("sectionNum:" + str(len(sections)))
        for section in sections:
            if isinstance(section, HeaderSection):
                print("header start")
                vars = section.ParseVars()
                print(vars)