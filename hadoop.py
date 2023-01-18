from mrjob.job import MRJob # MRJob version

class Flight(MRJob): #MRJob version
    def mapper_init(self):
        self.flights = {}
        self.passengers = {}
        
    def mapper(self, key, line):
        if line.startswith("ITIN_ID"):
            pass
        else:
            parts = line.split(",")
            state = parts[4]
            passengers = float(parts[7])
            self.flights[state] = 1.0 + self.flights.get(state,0)
            self.passengers[state] = passengers + self.passengers.get(state,0)
            # generate two dictionaries:  self.flights{state: flight_count},  self.passengers{state: passengers_count}
            
    def mapper_final(self):
        for i in self.flights:
            yield i, (self.flights[i], "flight")
        for j in self.passengers:
            yield j, (self.passengers[j], "passenger")
            # this should be (state, (flight_count, "flight"))
                   
    # the mapper would send pairs to reducer:   (state, [(1, flight),(2, passenger)]) same key will be grouped together
    def reducer(self, key, values):
        flight_count = 0
        passenger_count = 0
        for values in values:
            if values[1] == "flight":
                flight_count += values[0]
            if values[1] == "passenger":
                passenger_count += values[0]
        yield key, (passenger_count, flight_count)
             
            

if __name__ == '__main__':
    Flight.run() # MRJob version
