# ---------------------------------------------------------------------------------------------------------------------------
# MODULE CLASS
# ---------------------------------------------------------------------------------------------------------------------------

class Module:
    # Object for a single module on a device.
    def  __init__(self, device):
        self.device = device # Should be a device.Device object
    
    def __repr__(self):
        # Canonical representation.
        dict = vars(self)
        string = f"{type(self).__name__}("
        for key in dict:
            string += f"{key}={repr(dict[key])},"
        return string[:-1]+f")"

    def solve(self):
        # Runs the solver for the module. Override and implement for each module.
        return True
