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
        self.driver.get('https://kogetsu-an.shop/usces-member/')
        # 画面最大化
        self.driver.maximize_window()

    # Testcase 1: can be login with right pw    
    def test_login_successful(self):
        self.driver.find_element(By.NAME, "loginmail").send_keys("yingpei.liu81@gmail.com")
        #pw input
        self.driver.find_element(By.NAME, "loginpass").send_keys("Admin1234")
        
        self.button=self.driver.find_element(By.NAME, "member_login")
        self.button.click()

        member_page=self.driver.find_element(By.ID, "usces_purdate")
        assert member_page.is_displayed(),"Login successful page not found"

    # Testcase 2: cannot be login with wrong pw    
    def test_login_failed(self):
        self.driver.find_element(By.NAME, "loginmail").send_keys("yingpei.liu81@gmail.com")
        #pw input
        self.driver.find_element(By.NAME, "loginpass").send_keys("Admin1233")
        
        self.button=self.driver.find_element(By.NAME, "member_login")
        self.button.click()

        stayin_loginpage=self.driver.find_element(By.ID, "loginform")
        assert stayin_loginpage.is_displayed(),"Login failed page not found"

    def test_search_successed(self):
        """商品検索機能が正しく動作するかテストします。"""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "input-search"))
        )
        search_box.send_keys("mac" + Keys.ENTER)
        
        # 検索結果が表示されるまで待機
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-layout .product-thumb"))
        )

        # 検索結果が期待通りに表示されるか確認
        self.assertNotIn("There is no product that matches the search criteria.", self.driver.page_source)



    # テスト後の後処理
    def tearDown(self):
        """テスト後の後処理を行います。"""
        # 10秒待機する
        time.sleep(3)
        # ブラウザを閉じる
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()