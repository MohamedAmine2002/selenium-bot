from selenium import webdriver #webdriver est un classe  de base qui permet d'interagir avec le navigateur importé pour utiliser les méthodes et attributs de cette classe
import nouvelair.constants as const
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait #attente explicite  sur un élément de la page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Booking (webdriver.Chrome): 
    #constructeur
    def __init__(self, driver_path=r"C:/Users/medamine/selenium" ):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__() #on a utiliser super() parceque quand  on crée un objet de la class "booking", on veut que python appelle aussi le constructeur de la classe webdriver 
        self.implicitly_wait(15)
        self.maximize_window()
    
    #ouvrir le lien 
    def land_first_page (self) :
        self.get(const.url)

    
    #cliquer sur accepter les cookies 
    def accept_cookies(self):
        try:
            accept_bouton = WebDriverWait(self,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="rcc-confirm-button"]'))
            )
            accept_bouton.click()    
            print("Cookies accept button clicked successfully.")
        except:
            print("Could not find or click the accept button. Error:")
    
    #remplir le ville de depart 
    def select_place_of_departure(self,place_of_departure) :
        try :
            country_of_departure = WebDriverWait(self,10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,'input[class="MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused"]'))
            )
            print("input selectionné avec succes")
            country_of_departure.send_keys(place_of_departure)
            city_of_departure= self.find_element(By.CSS_SELECTOR,'li[data-option-index="2"]')
            city_of_departure.click()
        except :
            print("Could not select place of departure ")
    def select_place_of_arrival(self , place_of_arrival): 
        try :
            #skipping to the next input
            next_input=self.find_element(By.XPATH,'//*[@id="reservation-flight-tab"]/div/div[1]/div[1]/button')
            country_of_arrival = next_input.send_keys(Keys.TAB)
            print("input selectionné avec succes")
            country_of_arrival=WebDriverWait(self,10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,'input[class="MuiInputBase-input MuiInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused"][value=""]'))
            )
            country_of_arrival.send_keys(place_of_arrival)

            menu_des_aereport = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="MuiButtonBase-root MuiListItem-root country-collapse MuiListItem-gutters MuiListItem-button"][role="button"]')))
            menu_des_aereport.click()
            print("menu cliqué")

            
            city_of_arrival = WebDriverWait(self, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR , 'li[data-option-index="0"]')))
            city_of_arrival.click()
        except : 
            print("Could not select place of arrival ")
    #ajouter la date de vol
    def select_dates (self ,check_in_date , check_out_date, type):
        try :
            
            calendar = self.find_element(By.CSS_SELECTOR, 'div[class="MuiGrid-root date-selector-container-input   MuiGrid-container"]')
            calendar.click()
            
            
            if  type == "aller_retour" :
                selcted_type = self.find_element(By.NAME,'roundTrip').click()  
                date_check_in = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_in_date}"]')))
                print('Setting check in date ...')
                date_check_in.click()
                
                #si la date est invalable 
                classe = date_check_out.get_attribute('class').split()        
                if 'Mui-disabled' not in classe:
                    print('Setting check out date ...')


                date_check_out = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_out_date}"]')))
                print('Setting check out date ...')
                date_check_out.click()  
                
                #si la date est invalable 
                classe = date_check_out.get_attribute('class').split()        
                if 'Mui-disabled' not in classe:
                    print('Setting check out date ...') 
            
            
            
            else :
                selcted_type = self.find_element(By.NAME,'oneWay').click()  
                date_check_in = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_in_date}"]')))
                print('Setting check in date ...')
                date_check_in.click()
                
                #si la date est invalable 
                classe = date_check_out.get_attribute('class').split()        
                if 'Mui-disabled' not in classe:
                    print('Setting check out date ...')
        except:
            print("Could not select dates")

    def click_search(self):
        #submiting the form
        submiting_btn = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="reservation-flight-tab"]/div/div[2]/div[2]/button'))
        )
        print('Clicking submit button ...')
        submiting_btn.click()
    def page_loaded(self):
        time.sleep(5)
        print("The url of current page  : ", self.current_url)



    

    