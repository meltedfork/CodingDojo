class Call(object):
    #print 'working'
    def __init__(self, idnum, name, phone, time, reason):
        self.id = idnum
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
        self.displayInfo()

    def displayInfo(self):
        print self.id, self.name, self.phone, self.time, self.reason  
        return self

class CallCenter(object):
    def __init__(self):
       self.calls = []
       self.set_queue()
        
    def add(self, call):
        #print 'CallCenter.add: before add', self.calls
        #print call.name
        self.calls.append(call)
        self.set_queue()
        #print 'CallCenter.add: after add', self.calls   
        return self

    def remove(self):
        self.calls.pop(0)
        self.set_queue() 
        return self  

    def set_queue(self):
        self.queue = len(self.calls)
        print 'There are {} in line'.format(self.queue)

    

caller1 = Call(1, 'Suz', '312-404-3931', '3:45 pm', 'complaint')  
#print caller1.name
caller2 = Call(2, 'Jason', '312-404-3931', '3:45 pm', 'complaint')    
callCenter = CallCenter()
callCenter.add(caller1)
callCenter.add(caller2)
callCenter.remove()