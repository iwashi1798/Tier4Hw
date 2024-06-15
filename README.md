# Tier4Hw
# Test for 台湾茶藝館 https://kogetsu-an.shop/


<TeaTest1.py> -> for login  

Testcase 1: Login with correct account/pw
Expect: show login page    
  Data:  
      - Account: yingpei.liu81@gmail.com  
      - PW: Admin1234  
  
Testcase 2: Login with wrong account/pw  
Expect: stay in same page  
    Data:  
      - Account: yingpei.liu81@gmail.com  
      - PW: Admin1234

<TeaTest2.py> -> for shopping cart  
Testcase 1: add 2 Abag and 1 Bbag to cart and show correct price and quantity on the page  
Expect: Price==4800 and quantity==3  

Testcase 2: add 2 Abag and 1 Bbag to cart, and then change Abag from 2 to 3, and show correct price and quantity on the page
Expect: Price==6400 and quantity==4  

Testcase3: Delete 2 Abag from cart, and show correct price and quantity on the page  
Expect: Price==1600 and quantity==1  
