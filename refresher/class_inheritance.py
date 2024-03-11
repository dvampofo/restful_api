class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self) -> str:
        # The !r calls the repr method. so that way I dont need to use '' around it
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)

# creating new class that inherits from Device
class Printer(Device):     
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity      # Max amount of pages
        self.remaining_pages = capacity# current capacity remaining
    
    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
        print("Printing {pages} pages.")
        self.remaining_pages -= pages

docu_print = Printer("Printer", "USB", 500)
docu_print.print(20)
print(docu_print)
docu_print.disconnect()