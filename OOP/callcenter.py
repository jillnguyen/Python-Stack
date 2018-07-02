class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print (self.id, "  ", self.name, "  ", self.number, "  ", self.time, "  ", self.reason)

class CallCenter(object):
    def __init__(self, calls):
        self.calls = []
        for i in range(0, len(calls)):  
            self.calls.append(calls[i])
        self.queue_size = len(self.calls)
    def add(self, my_call):
        self.calls.append(my_call)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def info(self):
        for i in range (0, len(self.calls)):
            print str(self.calls[i].name), "  ", str(self.calls[i].number), "  ", str(self.calls[i].time)

caller1 = Call("123456", "Zoel", 3102109870, 20, "phone bill")
caller2 = Call("23416", "Jill", 7145078179, 10, "Los Angeles")
caller3 = Call("93693", "Justin", 3128936570, 5, "Travel")
callcenter1 = CallCenter([caller1,caller2])
callcenter2 = CallCenter([caller2,caller3])
callcenter2.add(caller1).remove().info()


