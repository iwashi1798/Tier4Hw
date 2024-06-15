import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class SamplePageSearch(unittest.TestCase):
    
    def setUp(self):
        """テスト前の準備を行います。"""
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("--no-sandbox")

        # ChromeDriverを使用してWebDriverのインスタンスを作成
        self.driver = webdriver.Chrome(options=self.options)
        # サイトにアクセス
        self.driver.get('https://kogetsu-an.shop/category/item/')
        # 画面最大化
        self.driver.maximize_window()

    # Testcase1: add 2 Abag and 1 Bbag to cart and show correct price and quantity on the page
    def test_cart_ADD(self):
        self.button=self.driver.find_element(By.XPATH, "/html/body/section[1]/div/div/main/div[3]/div/div/article[1]/a/div/div[1]/div/img")
        self.button.click()
        self.driver.find_element(By.ID, "quant[10395][item28]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28]").send_keys("2")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28]")
        self.button.click()
        self.button=self.driver.find_element(By.ID, "previouscart")
        self.button.click()

        self.driver.find_element(By.ID, "quant[10395][item28-1]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28-1]").send_keys("1")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28-1]")
        self.button.click()

        #total price and quantity are correct
        expect_number="¥4,800"
        actual_number=self.driver.find_element(By.XPATH,"/html/body/div[2]/main/article/form/div[1]/table/tfoot/tr/th[5]").text
            #print(actual_number)
        assert actual_number==expect_number,"Expectednumber'{expect_number}',but got'{actual_number}'"
        #show correct quantity on cart icon
        expect_quantity = "3"
        actual_quantity=self.driver.find_element(By.XPATH,"/html/body/header/div/div[4]/div[2]/a/span").text
            #print(actual_quantity)
        assert actual_quantity==expect_quantity,"expect_quantity'{expect_quantity}',but got'{actual_quantity}'"




    # Testcase2: change Abag from 2 to 3, and show correct price and quantity on the page
    def test_cart_CHANGE(self):
        self.button=self.driver.find_element(By.XPATH, "/html/body/section[1]/div/div/main/div[3]/div/div/article[1]/a/div/div[1]/div/img")
        self.button.click()
        self.driver.find_element(By.ID, "quant[10395][item28]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28]").send_keys("2")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28]")
        self.button.click()
        self.button=self.driver.find_element(By.ID, "previouscart")
        self.button.click()

        self.driver.find_element(By.ID, "quant[10395][item28-1]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28-1]").send_keys("1")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28-1]")
        self.button.click()

        self.driver.find_element(By.NAME, "quant[0][10395][item28]").clear()
        self.driver.find_element(By.NAME, "quant[0][10395][item28]").send_keys("3")
        self.button=self.driver.find_element(By.NAME, "upButton")
        self.button.click()

        #total price and quantity are correct
        expect_number="¥6,400"
        actual_number=self.driver.find_element(By.XPATH,"/html/body/div[2]/main/article/form/div[1]/table/tfoot/tr/th[5]").text
            #print(actual_number)
        assert actual_number==expect_number,"Expectednumber'{expect_number}',but got'{actual_number}'"
        #show correct quantity on cart icon
        expect_quantity = "4"
        actual_quantity=self.driver.find_element(By.XPATH,"/html/body/header/div/div[4]/div[2]/a/span").text
            #print(actual_quantity)
        assert actual_quantity==expect_quantity,"expect_quantity'{expect_quantity}',but got'{actual_quantity}'"


    # Testcase3: Delete 2 Abag from cart, and show correct price and quantity on the page
    def test_cart_DELETE(self):
        self.button=self.driver.find_element(By.XPATH, "/html/body/section[1]/div/div/main/div[3]/div/div/article[1]/a/div/div[1]/div/img")
        self.button.click()
        self.driver.find_element(By.ID, "quant[10395][item28]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28]").send_keys("2")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28]")
        self.button.click()
        self.button=self.driver.find_element(By.ID, "previouscart")
        self.button.click()

        self.driver.find_element(By.ID, "quant[10395][item28-1]").clear()
        self.driver.find_element(By.ID, "quant[10395][item28-1]").send_keys("1")
        self.button=self.driver.find_element(By.ID, "inCart[10395][item28-1]")
        self.button.click()

        self.button=self.driver.find_element(By.NAME, "delButton[0][10395][item28]")
        self.button.click()

        #total price and quantity are correct
        expect_number="¥1,600"
        actual_number=self.driver.find_element(By.XPATH,"/html/body/div[2]/main/article/form/div[1]/table/tfoot/tr/th[5]").text
            #print(actual_number)
        assert actual_number==expect_number,"Expectednumber'{expect_number}',but got'{actual_number}'"
        #show correct quantity on cart icon
        expect_quantity = "1"
        actual_quantity=self.driver.find_element(By.XPATH,"/html/body/header/div/div[4]/div[2]/a/span").text
            #print(actual_quantity)
        assert actual_quantity==expect_quantity,"expect_quantity'{expect_quantity}',but got'{actual_quantity}'"
        

    # テスト後の後処理
    def tearDown(self):
        """テスト後の後処理を行います。"""
        # 10秒待機する
        time.sleep(2)
        # ブラウザを閉じる
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()