with open("坡口图-2004版.dxf", 'rb') as f:
    i = 0
    while True:
        code = f.readline()
        value = f.readline()  # str(f.readline(), encoding="ansi")
        code = str(code, encoding="ansi")
        try:
            value = str(value, encoding="ansi")
        except Exception as e:
            value = str(value)
        if not code:
            break
        i += 2
        print(i-1," ",code)
        print(i," ",value)