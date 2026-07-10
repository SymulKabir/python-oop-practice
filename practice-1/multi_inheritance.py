class FrontedDeveloper:
    def write_code(self):
        print("Writing code by FrontedDeveloper")
        
class BackendDeveloper:
    def write_code(self):
        print("Writing code by BackendDeveloper")
        
class FullStakeDeveloper(FrontedDeveloper, BackendDeveloper):
    pass

employee = FullStakeDeveloper()

employee.write_code()