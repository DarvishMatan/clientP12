from infi.devicemanager import DeviceManager
dm = DeviceManager()
dm.root.rescan()
disks = dm.disk_drives
names = [disk.friendly_name for disk in disks]
print(names)