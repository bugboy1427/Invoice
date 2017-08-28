
class Address:
    def __init__(self,street,city,state,zipCode):
        self.address = [street,city,state,zipCode]
        
    def __str__(self):
        return('{}\n{},{},{}\n'.format(self.address[0],self.address[1],self.address[2],self.address[3]))
 
    def __getitem__(self,key):
        return(self.address[key])

    def street(self):
        return(self.address[0])
    
    def city(self):
        return(self.address[1])
    
    def state(self):
        return(self.address[2])
    
    def zipCode(self): 
        return(self.address[3])

    @staticmethod
    def parse(str,del):
        addressStr = str.split(del)
        address = Address(addressStr[0],addressStr[1],addressStr[2],addressStr[3])
        return(address)
        
