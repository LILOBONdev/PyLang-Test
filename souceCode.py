import requests

lib_api = 'https://raw.githubusercontent.com/LILOBONdev/PyLang-Test/refs/heads/main/publicLibrary.json'
enter = """"""

class shell():
    code = None
    def __init__(self,code: str):
        self.code
        code = enter.split('\n')

        VARS = {}
        IMPORT = {}
        for i in code:
            compilate = i.split()
            for a in compilate:
                if a == 'var':
                    TempStroke = compilate
                    if not TempStroke[2].count('='): return print('err')
                    if TempStroke[4] == 'int': VARS[TempStroke[1]] = int(TempStroke[3])

                    print(VARS)
                    VARS[TempStroke[1]] = TempStroke[3]
                
                if a == 'import':
                    TempStroke = compilate
                    TempStroke.remove(TempStroke[0])

                    r = requests.get(lib_api)
                    IMPORT[TempStroke[0]] = r.json()[TempStroke[0]]
                
                if a == 'lib':
                    TempStroke = compilate
                    TempStroke.remove(TempStroke[0])
                    for libs in IMPORT:
                        if TempStroke[0] == libs:
                            pass
                        else: return print('err')
                    if TempStroke[1] == IMPORT[TempStroke[0]]['actionComand']:
                        with open(f'{TempStroke[0]}.py','w') as loaded:
                            reqSource = requests.get(IMPORT[TempStroke[0]]['source_code'])
                            loaded.write(reqSource.text)
                            print(TempStroke[0],'load in Project!')
                        return print(f'{TempStroke[0]} started')

                    if not TempStroke[2] == '=' and not TempStroke[2] : return print('err')
                    IMPORT[TempStroke[0]][TempStroke[1]] = TempStroke[3]

                if a == 'if':
                    TempStroke = compilate
                    if TempStroke.count('>'):
                        elCount = TempStroke.index('>')
                        
                        if int(TempStroke[elCount-1]) > int(TempStroke[elCount+1]):
                            print('true')
                        else: print('false')
                        
                    if TempStroke.count('-'):
                        elCount = TempStroke.index('-')
                        try:
                           a,b=int(VARS[TempStroke[elCount-1]]),int(VARS[TempStroke[elCount+1]])
                        except KeyError:
                            a,b = int(TempStroke[elCount-1]),int(TempStroke[elCount+1])
                        
                        if type(a) and type(b) is int: print(a - b)
                
                if a.count('+'):
                    TempStroke = compilate
                    elCount = TempStroke.index('+')
                    """try:
                        a,b=int(VARS[TempStroke[elCount-1]]),int(VARS[TempStroke[elCount+1]])
                    except KeyError:
                        a,b = int(TempStroke[elCount-1]),int(TempStroke[elCount+1])"""
                    
                    tempMathBox = []
                    DublicateTempMathBox = []

                    for math in TempStroke:
                        tempMathBox.append(math)
                        if tempMathBox.count('+'): tempMathBox.remove('+')
                    
                    for mathPluses in tempMathBox:
                        DublicateTempMathBox.append(int(mathPluses))

                    print(sum(DublicateTempMathBox))
                    print(DublicateTempMathBox)


                #print(TempStroke)
shell(enter)
