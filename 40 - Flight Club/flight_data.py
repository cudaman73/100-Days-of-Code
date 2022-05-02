class FlightData:
    def __init__(self):
        pass

    def is_flight_cheaper(self, price, low):
        if price <= low:
            return True
        else:
            return False
