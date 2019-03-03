from .Entities import EntityFactory
from .Tables import TableFactory

class Section:

    ENTITIES = "ENTITIES"#这里只定义了三种类型，还可以扩展dxf存在的
    HEADER = "HEADER"
    TABLES = "TABLES"

    def __init__(self, type,section_content):
        self.content = section_content
        self.type = type

    def GetSectionType(self):
        return self.type

    def __str__(self):
        return str(self.content)


class EntitiesSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self, type, section_content)

    def ParseEntities(self, type=None):#获取所有的图元实体 也就是LineEntity ArcEntiry等的实例
        entities = []
        content_copy = self.content.copy()
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == "  0":
                if type and type != value:
                    continue
                entity_type = value
                content = []
                while len(content_copy) != 0:
                    if content_copy[0] != "  0":
                        content.append(content_copy.pop(0))
                        content.append(content_copy.pop(0))
                    else:
                        break
                entity = EntityFactory.CreateEntity(entity_type, content)
                if entity:#同样的，还没有编写的类型，返回的None直接忽略
                    entities.append(entity)
        return entities




class HeaderSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self, type, section_content)

    def ParseVars(self):
        #解析出一个cad变量字典
        content_copy = self.content.copy()
        vars = dict()
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == "  9":
                vars[value] = dict()
                while len(content_copy) != 0:
                    if content_copy[0] != "  9":
                        _code = content_copy.pop(0)
                        _value = content_copy.pop(0)
                        vars[value][_code] = _value
                    else:
                        break
        return vars


class TablesSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self, type, section_content)

    def ParseTables(self, type=None):
        tables = []
        content_copy = self.content.copy()
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == "  0" and value == "TABLE":#一张表的开始
                content_copy.pop(0)#必是2 丢弃
                table_type = content_copy.pop(0)
                if type and type != table_type:
                    continue
                content = []
                while len(content_copy) != 0:
                    _code = content_copy.pop(0)
                    _value = content_copy.pop(0)
                    if _code == "  0" and _value == "ENDTAB":#一张表结束
                        break
                    content.append(_code)
                    content.append(_value)
                table = TableFactory.CreateTable(table_type, content)
                if table:  # 同样的，还没有编写的类型，返回的None直接忽略
                    tables.append(table)
        return tables

class SectionFactory:

    __section_types = {"ENTITIES": "EntitiesSection","HEADER":"HeaderSection","TABLES":"TablesSection"}

    def __init__(self):
        pass

    @staticmethod
    def CreateSection(type, section_content):
        section = None
        if type in SectionFactory.__section_types:
            section = eval(SectionFactory.__section_types[type]+"(type, section_content)")
        return section

