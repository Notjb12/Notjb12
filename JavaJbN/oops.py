class input:
    def got(self):
        self.one=str(int(input("Enter your mobile number")))
        self.tow=str(int(input("Enter your mobile number")))
class main(input):
    def add(self):
        return self.one+self.tow
    def sub(self):
        return self.one-self.tow
    def mul(self):
        return self.one*self.tow
class submain(main):
    def div(self):
        return self.one/self.tow
    def mod(self):
        return self.one%self.tow
obj=main()
obj.got()
obj.add()
obj.sub()
obj.mul()
obj.div()