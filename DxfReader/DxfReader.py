from DxfReader.Sections import SectionFactory

class DxfReader:

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def __get_value(value):#主要是用ansi解码是可能会出错
        try:
            value = str(value, encoding="ansi")  # 这里有可能会出错
        except Exception as e:
            value = str(value)
        return value.replace("\r\n", "")

    def GetSections(self, type=None):
        sections = []
        with open(self.filename, 'rb') as f:
            while True:
                code = DxfReader.__get_value(f.readline())
                value = DxfReader.__get_value(f.readline())  # str(f.readline(), encoding="ansi")
                if not code:#文件尾
                    break
                #读取 0 SECTION (紧跟着2 type)和 0 ENDSEC 之间的内容为一个Section
                if code == "  0" and value == "SECTION":
                    #段开始 先读取段的类型
                    f.readline()#必然是2 丢弃
                    section_type = DxfReader.__get_value(f.readline())#Section的type 可能值：ENTITIES HEADER TABLES BLOCKS
                    if type and section_type!=type:
                        continue
                    content = dict()
                    while True:
                        endcode = DxfReader.__get_value(f.readline())
                        endvalue = DxfReader.__get_value(f.readline())
                        if endcode == "  0" and endvalue=="ENDSEC":#读到段尾
                            break
                        content[endcode] = endvalue
                    section = SectionFactory.CreateSection(section_type, content)
                    # 对于还没有实现的type类型直接跳过
                    if section:
                        sections.append(section)
            return sections



    def GetCircles(self):
        pass

    def GetArcs(self):
        pass

    def GetLines(self):
        pass