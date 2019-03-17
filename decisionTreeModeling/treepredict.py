#-*-coding:utf-8-*-
my_data = [line.split('\t') for line in open('desicision_tree_example.txt')]

class decsionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb
    
