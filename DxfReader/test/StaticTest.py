import unittest
from DxfReader.DxfReader import DxfReader
from DxfReader.Entities import Entity

class StaticTest(unittest.TestCase):

    def test_GetShapeData(self):
        #arc
        print("ARC")
        print(DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.ARC))
        print()
        #line
        print("LINE")
        print(DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.LINE))
        print()
        #circle
        print("CIRCLE")
        print(DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.CIRCLE))
        print()
        #ellipse
        print("ELLIPSE")
        print(DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.ELLIPSE))
        print()

    def test_GetLayers(self):
        print("layers")
        print(DxfReader.GetLayers("DxfReader/test/坡口图-2004版.dxf"))