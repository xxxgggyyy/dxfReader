import unittest
from ..DxfReader import DxfReader
from ..Sections import EntitiesSection
from ..Entities import LineEntity,ArcEntity,CircleEntity,EllipseEntity

class EntitiesTest(unittest.TestCase):

    def test_Got_Entities(self):
        dxfReader = DxfReader("DxfReader/test/test.dxf")
        sections = dxfReader.ParseSections()
        print("sectionNum:" + str(len(sections)))
        for section in sections:
            print(type(section))
            if isinstance(section,EntitiesSection):
                entities = section.ParseEntities()
                print("entityNum:"+str(len(entities)))
                for entity in entities:
                    print(entity.parse())