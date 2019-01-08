### dxfReader


 **介绍** 
- 这里是列表文本用来解析,提取CAD中的dxf文件格式所保存的图像信息

 **软件架构** 
- 主要采用简单工厂模式：


1. SectionFactory
1. TableFactory
1. EntityFactory


方便扩展还未解析的类型


 **安装教程** 
- python3.X

 **使用说明** 

- 最简单的用法：

```
#提取圆弧 返回一个包含字典的数组
DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.ARC)
#提取直线
DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.LINE)
#提取圆
DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.CIRCLE)
#提取椭圆
DxfReader.GetShapeData("DxfReader/test/test.dxf", Entity.ELLIPSE)
#提取所有的图层名
DxfReader.GetLayers("DxfReader/test/坡口图-2004版.dxf")
```

- 基本用法:

```
dxfReader = DxfReader("DxfReader/test/坡口图-2004版.dxf")
sections = dxfReader.ParseSections()
for section in sections:
    if isinstance(section, HeaderSection):
        vars = section.ParseVars()#解析出一个 cad 变量的 字典
    if isinstance(section,EntitiesSection):
        entities = section.ParseEntities()#解析出各种类型的实体,圆形，直线，弧形，椭圆
        for entity in entities:#每种实体都可调用parse解析出一个带有实际数据的字典
            print(entity.parse())#如直线的{'type': 'line', 'layer': '0', 'x0': -111.6999999999999, 'y0': -6.0, 'z0': 0.0, 'x1': -101.7, 'y1': -6.0, 'z1': 0.0, 'tensile_x': '0', 'tensile_y': '0', 'tensile_z': '1'}
    if isinstance(section, TablesSection):
        tables = section.ParseTables()
        for table in tables:
            entries = table.ParseEntries()
            for entry in entries:
                print(entry.parse())#可以解析出dxf中的表段，现在只实现了提取图层的
                #如{'type': 'layer', 'name': '轮廓'}
```


 **参与贡献** 

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request