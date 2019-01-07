from DxfReader.Entities import EntityFactory

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

class TablesSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self, type, section_content)

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

