from appium import webdriver
desired_caps = {}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='10'
desired_caps['deviceName']='GBGDU19B20003545'
desired_caps['appPackage']='com.fltrp.organ.teacher'
desired_caps['appActivity']='com.fltrp.organ.mainmodule.view.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)