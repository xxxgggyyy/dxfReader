

class Section:

    def __init__(self, type,section_content):
        self.content = section_content
        self.type = type

    def GetSectionType(self):
        return self.type

class EntitiesSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self,type,section_content)

class HeaderSection(Section):
    def __init__(self, type, section_content):
        Section.__init__(self, type, section_content)

class SectionFactory:

    __section_types = {"ENTITIES": "EntitiesSection","HEADER":"HeaderSection"}

    def __init__(self):
        pass

    @staticmethod
    def CreateSection(type, section_content):
        section = None
        if type in SectionFactory.__section_types:
            section = eval(SectionFactory.__section_types[type]+"(type, section_content)")
        return section

