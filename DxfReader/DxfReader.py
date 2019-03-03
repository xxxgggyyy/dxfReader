from .Sections import SectionFactory

class DxfReader:

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def __trans_value(value):#主要是用ansi解码是可能会出错
        try:
            value = str(value, encoding="ansi")  # 这里有可能会出错
        except Exception as e:
            value = str(value)
        value = value.replace("\r\n", "")
        value = value.replace("\n", "")
        value = value.replace("\r", "")

        return value

    def ParseSections(self, type=None):
        sections = []
        with open(self.filename, 'rb') as f:
            while True:
                code = f.readline()
                if not code:#文件尾
                    break
                value = f.readline()  # str(f.readline(), encoding="ansi")
                if not value:#不是偶数行
                    raise Exception("文件已损坏")

                #读取 0 SECTION (紧跟着2 type)和 0 ENDSEC 之间的内容为一个Section
                if DxfReader.__trans_value(code) == "  0" and DxfReader.__trans_value(value) == "SECTION":
                    #段开始 先读取段的类型
                    f.readline()#必然是2 丢弃
                    section_type = f.readline()#Section的type 可能值：ENTITIES HEADER TABLES BLOCKS
                    if not section_type:
                        raise Exception("文件已损坏")
                    if type and DxfReader.__trans_value(section_type)!=type:
                        continue
                    content = []
                    while True:
                        endcode = f.readline()
                        endvalue = f.readline()
                        trans_endcode = DxfReader.__trans_value(endcode)
                        trans_endvalue = DxfReader.__trans_value(endvalue)
                        if not endvalue:
                            raise Exception("文件已损坏")
                        if trans_endcode == "  0" and trans_endvalue == "ENDSEC":#读到段尾
                            break
                        content.append(trans_endcode)
                        content.append(trans_endvalue)#section的内容保存为了数组
                    section = SectionFactory.CreateSection(DxfReader.__trans_value(section_type), content)
                    # 对于还没有实现的type类型直接跳过
                    if section:
                        sections.append(section)
        return sections

    @staticmethod
    def GetShapeData(fileName, type):
        from .Sections import EntitiesSection
        result = []
        dxfReader = DxfReader(fileName)
        sections = dxfReader.ParseSections()
        for section in sections:
            if isinstance(section, EntitiesSection):
                entities = section.ParseEntities(type)
                for entity in entities:
                    result.append(entity.parse())
                return result

    @staticmethod
    def GetLayers(fileName):
        from .Sections import TablesSection
        from .Tables import Table
        dxfReader = DxfReader(fileName)
        sections = dxfReader.ParseSections()
        result = []
        for section in sections:
            if isinstance(section, TablesSection):
                tables = section.ParseTables(Table.LAYER)
                for table in tables:
                    entries = table.ParseEntries()
                    for entry in entries:
                        result.append(entry.parse())
                    return result