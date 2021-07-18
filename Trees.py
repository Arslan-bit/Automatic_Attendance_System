class node:
    def _init_(self,data):
        self.left=None
        self.right=None
        self.Data=data
    def inserNode(self,value):
        if self.Data:
            if self.Data<value:
                if self.right==None:
                    self.right=node(value)
                    # print(self.right.inserNode(self.right))
                else:
                    (self.right.inserNode(value))
                    # self.right=self.right.inserNode(value)

            elif self.Data>value:
                if self.left==None:
                    self.left=node(value)
                    # print(self.left)
                else:
                    # self.left=self.left.inserNode(value)
                    (self.left.inserNode(value))
                    # print(self.left)
        else:
            value=value
            # print("Nothing in list")

    def LeftrootRight_Traverse(self):

        if self.right:
            self.right.LeftrootRight_Traverse()
        print(self.Data)
        if self.left:
            self.left.LeftrootRight_Traverse()


root = node(12)
root.inserNode(1)
root.inserNode(4)
root.inserNode(5)
root.inserNode(7)