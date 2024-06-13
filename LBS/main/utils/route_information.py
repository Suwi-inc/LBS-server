class RouteInfo:
    def __init__(self, endpoint, methods):
        self.endpoint = endpoint
        self.methods = methods

    def __repr__(self):
        return f"<endpoint={self.endpoint}, methods={self.methods}>"
