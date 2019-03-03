import unittest
from ..DxfReader import DxfReader
from ..Sections import TablesSection

class TablesTest(unittest.TestCase):

    def test_layer_table(self):
        dxfReader = DxfReader("DxfReader/test/坡口图-2004版.dxf")
        sections = dxfReader.ParseSections()
        print("sectionNum:" + str(len(sections)))
        for section in sections:
            if isinstance(section, TablesSection):
                tables = section.ParseTables()
                print("tableNum:" + str(len(tables)))
                for table in tables:
                    print(table.content)
                    print("start_entry")
                    entries = table.ParseEntries()
                    for entry in entries:
                        print(entry.parse())