class DeviceManager:
    def __init__(self):
        self.devices = {}

    def use_device(self, name):
        pass

    def acquire_device(self, device_id):
        if device_id in self.devices and self.devices[device_id]:
            print(f"Device {device_id} is already acquired.")
        else:
            self.devices[device_id] = True
            print(f"Device {device_id} acquired.")

    def release_device(self, device_id):
        if device_id in self.devices and self.devices[device_id]:
            self.devices[device_id] = False
            print(f"Device {device_id} released.")
        else:
            print(f"Device {device_id} is not currently acquired.")

    def add_device(self, device_id):
        if device_id in self.devices:
            print(f"Device {device_id} already exists.")
        else:
            self.devices[device_id] = False
            print(f"Device {device_id} added.")

    def query_device_usage(self):
        return self.devices

# # Example usage
# manager = DeviceManager()
# manager.acquire_device(1)  # Acquire device 1
# manager.acquire_device(2)  # Acquire device 2
# manager.release_device(1)  # Release device 1
# manager.release_device(3)  # Try to release device 3 (not acquired)
# manager.add_device(4)  # Add device 4
# manager.add_device(2)  # Try to add device 2 (already exists)
# manager.query_device_usage()  # Query device usages
