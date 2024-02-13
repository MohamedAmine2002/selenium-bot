from nouvelair.reservation import Booking
import time
inst = Booking()
inst.land_first_page()
inst.accept_cookies()
inst.select_place_of_departure("Tunis")
inst.select_place_of_arrival("paris")
inst.select_dates ( "23 fév 2024",None,"allersimple" )
inst.click_search()
inst.page_loaded()
time.sleep(5) #wait for the page to load