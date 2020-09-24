import os
class Adb(object):

    def get_devices_name(self):
        data = os.popen("adb devices").read().split("\n")
        devices_list = []
        for device in data:
            if "\t" in device:
                devices_list.append(device.split('\t')[0])
        return devices_list

    def get_android_version(self):
        data = os.popen('adb shell getprop ro.build.version.release').read()
