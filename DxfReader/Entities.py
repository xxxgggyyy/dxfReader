
class EntityFactory:

    __entity_types = {"LINE":"LineEntity","ARC":"ArcEntity","CIRCLE":"CircleEntity","ELLIPSE":"EllipseEntity"}

    @staticmethod
    def CreateEntity(type, entity_content):
        entity = None
        if type in EntityFactory.__entity_types:
            entity = eval(EntityFactory.__entity_types[type]+"(type,entity_content)")
        return entity


class Entity:

    ARC = "ARC"
    CIRCLE = "CIRCLE"
    LINE = "LINE"
    ELLIPSE = "ELLIPSE"

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def parse(self):
        pass

class LineEntity(Entity):
    def __init__(self,type, content):
        Entity.__init__(self, type, content)

    def parse(self):
        content_copy = self.content.copy()
        # 起始位置x0... 结束位置x1.... 拉伸量tensile_x....
        shape = {'type': "line", 'layer': '',"x0": '', 'y0': '', 'z0': '', 'x1': '', 'y1': '', 'z1': '', "tensile_x": '0',
                'tensile_y': '0',
                'tensile_z': '1'}
        while len(content_copy)!= 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == " 10":
                shape['x0'] = float(value)
            elif code == " 20":
                shape['y0'] = float(value)
            elif code == ' 30':
                shape['z0'] = float(value)
            elif code == ' 11':
                shape['x1'] = float(value)
            elif code == " 21":
                shape['y1'] = float(value)
            elif code == ' 31':
                shape['z1'] = float(value)
            elif code == '  8':
                shape['layer'] = value
            elif code == '210':
                shape['tensile_x'] = float(value)
            elif code == '220':
                shape['tensile_y'] = float(value)
            elif code == '230':
                shape['tensile_z'] = float(value)
        return shape


class ArcEntity(Entity):
    def __init__(self, type, content):
        Entity.__init__(self, type, content)

    def parse(self):
        content_copy = self.content.copy()
        # 圆心x... 半径r 起始角angle_0 结束角angle_1 拉伸量tensile_x....
        shape = {'type': "arc" , 'layer': '', "x": '', 'y': '', 'z': '', 'r': '', 'angle_0': '', 'angle_1': '', "tensile_x": '0',
                 'tensile_y': '0',
                 'tensile_z': '1'}
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == " 10":
                shape['x'] = float(value)
            elif code == " 20":
                shape['y'] = float(value)
            elif code == ' 30':
                shape['z'] = float(value)
            elif code == ' 40':
                shape['r'] = float(value)
            elif code == " 50":
                shape['angle_0'] = float(value)
            elif code == ' 51':
                shape['angle_1'] = float(value)
            elif code == '  8':
                shape['layer'] = value
            elif code == '210':
                shape['tensile_x'] = float(value)
            elif code == '220':
                shape['tensile_y'] = float(value)
            elif code == '230':
                shape['tensile_z'] = float(value)
        return shape

class CircleEntity(Entity):
    def __init__(self, type, content):
        Entity.__init__(self, type, content)

    def parse(self):
        content_copy = self.content.copy()
        # 圆心x0... 半径r 拉伸量tensile_x....
        shape = {'type': 'circle', 'layer': '', "x": '', 'y': '', 'z': '', "tensile_x": '0', 'tensile_y': '0',
                'tensile_z': '1'}
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == " 10":
                shape['x'] = float(value)
            elif code == " 20":
                shape['y'] = float(value)
            elif code == ' 30':
                shape['z'] = float(value)
            elif code == ' 40':
                shape['r'] = float(value)
            elif code == '  8':
                shape['layer'] = value
            elif code == '210':
                shape['tensile_x'] = float(value)
            elif code == '220':
                shape['tensile_y'] = float(value)
            elif code == '230':
                shape['tensile_z'] = float(value)
        return shape

class EllipseEntity(Entity):
    def __init__(self, type, content):
        Entity.__init__(self, type, content)

    def parse(self):
        content_copy = self.content.copy()
        # 圆心x... 长轴相对于圆心的坐标x_l.... 起始和结束角度start,end  长轴和短轴的比例k  拉伸量tensile_x....
        shape = {'type': "ellipse", 'layer': '', "x": '', 'y': '', 'z': '', 'x_l': '', 'y_l': '', 'z_l': '', 'k': '', 'start': '', 'end': '', "tensile_x": '0',
                 'tensile_y': '0',
                 'tensile_z': '1'}
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == " 10":
                shape['x'] = float(value)
            elif code == " 20":
                shape['y'] = float(value)
            elif code == ' 30':
                shape['z'] = float(value)
            elif code == ' 11':
                shape['x_l'] = float(value)
            elif code == " 21":
                shape['y_l'] = float(value)
            elif code == ' 31':
                shape['z_l'] = float(value)
            elif code == ' 40':
                shape['k'] = float(value)
            elif code == ' 41':
                shape['start'] = float(value)
            elif code == ' 42':
                shape['end'] = float(value)
            elif code == '  8':
                shape['layer'] = value
            elif code == '210':
                shape['tensile_x'] = float(value)
            elif code == '220':
                shape['tensile_y'] = float(value)
            elif code == '230':
                shape['tensile_z'] = float(value)
        return shape