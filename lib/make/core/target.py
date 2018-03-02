class Target(object):
    def __init__(self,name,compiler):
        self.name = name
        self.compiler = compiler
        self.target = []
        self.source = []
    
    def __str__(self):
        s = self.name + ' : '
        for t in self.target:
            s += t.name + ' '
        objStr = ''
        objName = []
        for r in self.source:
            objStr += r.objName() + ' '
            objName.append(r.objName())
        s += objStr + '\n'
        s += '\t' + self.compiler._buildCommand_(objName, self.name) + '\n'
        return s