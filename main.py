# creating a smart phone class
class Phone:
  
  def __init__(self,color,):
    self.color = color
    
    
# method to turn on phone
  def turn_on(self):
    return 'turning on'
   
# method to turn off phone
  def turn_off(self):
    return 'turning off' 
    
class ButtonPhone(Phone):
  def __init__(self,name,brand):
    self.name = name
    self.brand = brand
    
  # override to turn on method
  def turn_on(self):
    return f'{self.name} is turning on'
   
  # override to turn off method
  def turn_off(self):
    return f'{self.name} is turning off' 
    
phone = Phone('blue')
buttonPhone = ButtonPhone('itel','A13')

print(phone.turn_off())
print(buttonPhone.turn_off())