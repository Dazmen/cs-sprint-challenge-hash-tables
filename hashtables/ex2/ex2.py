#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    # def __str__(self):
    #     print(f'Source: {self.source}, Destination: {self.destination}')


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route_lookup = {}
    
    travel_route = [] # initialize array with starting location
    

    for ticket in tickets:
        route_lookup[ticket.source] = ticket.destination

    next_destination = route_lookup["NONE"] # this will always be the key to start

    while next_destination != "NONE":
        travel_route.append(next_destination)
        next_destination = route_lookup[next_destination]

    travel_route.append("NONE")

    return travel_route


# the text "NONE"s caught me off gaurd. I also was not expecting the tests to was the last "NONE" value, it doesn't make much sense from a question standpoint and it also is not shown to be expected in the README example.