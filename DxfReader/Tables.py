
class TableFactory:

    __table_types = {'LAYER': 'LayerTable'}

    @staticmethod
    def CreateTable(type, content):
        table = None
        if type in TableFactory.__table_types:
            table = eval(TableFactory.__table_types[type]+"(type, content)")
        return table


class Table:

    LAYER = "LAYER"

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def ParseEntries(self):
        pass

class Entry:

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def parse(self):
        pass

class LayerEntry(Entry):
    def __init__(self, type, content):
        Entry.__init__(self, type, content)

    def parse(self):
        content_copy = self.content.copy()
        layer = {'type': 'layer', 'name': "未知图层名或者文件错误"}
        while len(content_copy)!=0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == "100" and value == "AcDbLayerTableRecord":
                code = content_copy.pop(0)
                value = content_copy.pop(0)
                if code == "  2":
                    layer['name'] = value
                return layer
        return layer


class LayerTable(Table):

    def __init__(self, type, content):
        Table.__init__(self, type, content)

    def ParseEntries(self):
        entries = []
        content_copy = self.content.copy()
        while len(content_copy) != 0:
            code = content_copy.pop(0)
            value = content_copy.pop(0)
            if code == "  0":#type must be layer
                entry_type = value
                _content = []
                while len(content_copy) != 0:
                    if content_copy[0] != "  0":
                        _content.append(content_copy.pop(0))
                        _content.append(content_copy.pop(0))
                    else:
                        break
                layer_entry = LayerEntry(entry_type, _content)#这里的type一定是 layer就不用工厂模式了
                if layer_entry:  # 同样的，还没有编写的类型，返回的None直接忽略
                    entries.append(layer_entry)
        return entries
