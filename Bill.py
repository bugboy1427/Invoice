class BillItem:
    def __init__(self, name, price, quantity):
        self.name = name
        
        if price >= 0.0:
            self.price = price
        
        if quantity > 0:
            self.quantity = quantity

    def __str__(self):
        return('{:20} {:>10.2f} {:>2d}'.format(self.name,self.price,self.quantity))
        
    def Total(self):
        return(self.price * self.quantity)
        
class Bill:
    def __init__(self,customerName,taxRate=0.06):
        self.customerName = customerName
        self.items = []
        self.TaxRate = taxRate
    
    def __str__(self):
        bill = '{}\n\n'.format(self.customerName)
        
        for i in self.items:
            bill += '{} {:>10.2f}\n'.format(i.__str__(),i.Total())
        
        subTotal = self.SubTotal()
        bill += '\n{:>20} {:>10.2f}\n'.format('Sub:',subTotal)
        
        tax = subTotal*self.TaxRate
        bill += '{:>20} {:>10.2f}\n'.format('Tax:',tax)
        
        total = subTotal + tax
        bill += '{:>20} {:>10.2f}\n'.format('Total:',total)
        
        return(bill)    
    
    def __len__(self):
        return(len(self.items))
            
    def __getitem__(self,key):
        return(self.items[key])
    
    def Add(self,item):
        self.items.append(item)
    
    def Remove(self,index):
        self.items.remove(index)
    
    def SubTotal(self):
        total = 0.0
        
        for i in self.items:
            total += i.Total()
        
        return(total)