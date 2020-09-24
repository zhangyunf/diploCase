from appium import webdriver
from public.padb import Adb
class Driver:
    """获取连接的手机生成的句柄"""
    def get_desired(self, ):
        adb = Adb()
        devices = adb.get_devices_name()
        drivers_list = []
        desired_caps = {
            'platformName': 'Android',
            'appPackage': 'com.fltrp.organ.teacher',
            'appActivity': 'com.fltrp.organ.mainmodule.view.SplashActivity'
        }
        for index, device in enumerate(devices):
            desired_caps.update({"deviceName": device})
            print(desired_caps, 4723 + index * 2)
            driver = webdriver.Remote('http://127.0.0.1:%d/wd/hub' % (4723 + index * 2), desired_caps)
            drivers_list.append(driver)
        return drivers_list







