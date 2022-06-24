from seleniumbase import BaseCase

#Project Name: Test_Sauce_Demo
#Created by: Shashank Pereddigari
#Creation Date: 6/23/2022
#Reviewed By: 
#Reviewed Date: 

class Test_Sauce_Demo(BaseCase):
    
    #Test_Scenario_ID = TS_0001
    #Test Scenario Description = Verify the functionality of the saucedemo.com login page
    #Test Case ID = TC_0001
    #Test Case Description = Enter a valid username and password and verify the login works properly
    #Test Preconditions = valid url, valid username, valid password
    #Postconditions: User should be able to see the inventory page after successful login
    def test_login_page(self,usr="standard_user",pwd="secret_sauce"):
        u=["standard_user","locked_out_user","problem_user","performance_glitch_user"]
        if usr not in u:
            self.fail("Error, invalid username: "+usr)
        if pwd != "secret_sauce":
            self.fail("Error, incorrect password")
        self.open("saucedemo.com")
        self.assert_element("#user-name")
        self.send_keys("#user-name",usr)
        self.assert_element("#password")
        self.send_keys("#password",pwd)
        self.assert_element('input[type="submit"]')
        self.click('input[type="submit"]')
        self.assert_not_equal(self.get_current_url(),"saucedemo.com")
    #Expected Result: Successful Login
    #Actual Result: Successful Login    
    #Status: Successful
        
        
    #Test_Scenario_ID = TS_0002
    #Test Scenario Description = Verify functionality of the login page
    #Test Case ID = TC_0002
    #Test Case Description = Enter a valid username and invalid password and verify invalid login
    #Test Preconditions = valid url, valid username, invalid password
    #Postconditions: User should stay on the login page and receive an error message
    def test_failed_login(self,usr="standard_user"):
        self.open("saucedemo.com")
        self.assert_element("#user-name")
        self.send_keys("#user-name","standard_user")
        self.assert_element("#password")
        self.send_keys("#password","Not_real_password")
        self.assert_element("#login-button")
        self.click("#login-button")
        if self.assert_element("#login-button"):
            self.fail("Error, invalid username/password")
    #Expected Result: "Error Message for wrong username/password"
    #Actual Result: "Error message for wrong username/password"
    #Status: Successful
        
    #Test_Scenario_ID = TS_0003
    #Test Scenario Description = Verify the functionality of the item order button
    #Test Case ID = TC_0003
    #Test Case Description = Check each method of ordering inventory items and see if valid 
    #Test Preconditions = valid url, valid username, valid password
    #Postconditions: User should see all items in respective order based on order by choice
    def test_order_of_items(self):
        self.test_login_page()
        self.assert_element("#shopping_cart_container")
        self.select_option_by_value("select.product_sort_container","za")
        if "Test.allTheThings() T-Shirt" not in self.get_text("div.inventory_item"):
            self.fail("Error, sort from Z-A is invalid")
        
        self.select_option_by_value("select.product_sort_container","az")
        if "Sauce Labs Backpack" not in self.get_text("div.inventory_item"):
            self.fail("Error, sort from A-Z is invalid")

        self.select_option_by_value("select.product_sort_container","lohi")
        if "Sauce Labs Onesie" not in self.get_text("div.inventory_item"):
            self.fail("Error, Low to High sort is invalid")

        self.select_option_by_value("select.product_sort_container","hilo")
        if "Sauce Labs Fleece Jacket" not in self.get_text("div.inventory_item"):
            self.fail("Error, High to Low sort is invalid")
    #Expected Result: No error, all items match respective order
    #Actual Result: No error, all items match respective order
    #Status: Successful
            
    #Test_Scenario_ID = TS_0004
    #Test Scenario Description = Verify the functionality of the checkout button
    #Test_Case_ID = TC_0004
    #Test Case Description = Perform a checkout with 0 items and throw an error if order is successful
    #Test Preconditions = valid url, valid username, valid password
    #Postconditions: User should get error when checking out with 0 items
    def test_invalid_checkout(self):
        # TEST TO CHECKOUT WITH 0 ITEMS, INTENTIONAL ERROR MESSAGE
        self.test_login_page()
        self.assert_element("#shopping_cart_container")
        self.click("#add-to-cart-sauce-labs-backpack")
        self.click("#remove-sauce-labs-backpack")
        self.click("#shopping_cart_container")
        self.click("#checkout")
        self.assert_element("#first-name")
        self.send_keys("#first-name","Shashank")
        self.assert_element("#last-name")
        self.send_keys("#last-name","Pereddigari")
        self.assert_element("#postal-code")
        self.send_keys("#postal-code","00000")
        self.assert_element("#continue")
        self.click("#continue")
        self.assert_element("#finish")
        self.click("#finish")
        if self.assert_exact_text("THANK YOU FOR YOUR ORDER", "h2"):
            self.fail("Error, no items in cart: invalid order")
    #Expected Result: Error Message for invalid checkout
    #Actual Result: Successful checkout message
    #Status: Failed
            
    #Test_Scenario_ID = TS_0005
    #Test_Scenario_Description = Verify the functionality of the login page
    #Test_Case_ID = TC_0005
    #Test Case Description = Perform login with invalid username and valid password for error
    #Test Preconditions = valid url, invalid username, valid password
    #Postconditions: User should stay on login page and receive and error message
    def test_failed_login_2(self,usr="not_a_user",pwd="secret_sauce"):
        self.open("saucedemo.com")
        self.assert_element("#user-name")
        self.send_keys("#user-name",usr)
        self.assert_element("#password")
        self.send_keys("#password",pwd)
        self.assert_element("#login-button")
        self.click("#login-button")
        if self.assert_element("#login-button"):
            self.fail("Error, invalid username/password")
    #Expected Result: "Error Message for wrong username/password"
    #Actual Result: "Error message for wrong username/password"
    #Status: Successful
            
    #Test_Scenario_ID = TS_0006
    #Test_Scenario_Description = Verify the functionality of the login page
    #Test_Case_ID = TC_0006
    #Test Case Description = Perform login with invalid username and invalid password for error
    #Test Preconditions = valid url, invalid username, invalid password
    #Postconditions: User should stay on login page and receive and error message
    def test_failed_login_3(self,usr="not_a_user",pwd="secret_sauces"):
        self.open("saucedemo.com")
        self.assert_element("#user-name")
        self.send_keys("#user-name",usr)
        self.assert_element("#password")
        self.send_keys("#password",pwd)
        self.assert_element("#login-button")
        self.click("#login-button")
        if self.assert_element("#login-button"):
            self.fail("Error, invalid username/password")
    #Expected Result: "Error Message for wrong username/password"
    #Actual Result: "Error message for wrong username/password"
    #Status: successful
            
    #Test_Scenario_ID = TS_0007
    #Test Scenario Description = Test the functionality of the continue button
    #Test Case ID = TC_0007
    #Test Case Description = 
    # def test_continue_button(self):
    #     self.test_login_page()
    #     self.assert_element("#shopping_cart_container")




