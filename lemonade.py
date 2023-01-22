class InvalidSalesItemError(Exception):
    """Doc String"""
    pass


class MenuItem:
    """Doc String"""
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name
    
    def get_wholesale_cost(self):
        return self._wholesale_cost
    
    def get_selling_price(self):
        return self._selling_price
    
class SalesForDay:
    """Doc String"""
    def __init__(self, number_of_days, sales_dict):
        self._number_of_days = number_of_days
        self._sales_dict = sales_dict

    def get_days_open_int(self):
        return self._number_of_days
    
    def get_sales_dict(self):
        return self._sales_dict
    
class LemonadeStand:
    """Doc String"""
    def __init__(self, stand_name_string):
        self._stand_name_string = stand_name_string
        self._current_day = 0
        self._menu = {}
        self._sales_record = []
    
    def get_stand_name_string(self):
        return self._stand_name_string
    
    def get_current_day(self):
        return self._current_day

    def get_menu(self):
        return self._menu
    
    def get_sales_record(self):
        return self._sales_record

    def add_menu_item(self, new_menu_item):
        self._menu[new_menu_item.get_name().lower()] = new_menu_item

    def print_menu_items(self):
        menu_dict = self.get_menu()
        for food_item in menu_dict: #food is the key in the Dict
            print(f"{food_item} Wholesale: ${menu_dict[food_item].get_wholesale_cost()}  Retail: ${menu_dict[food_item].get_selling_price()}")

    def search_menu(self, search_str):
        menu_dict = self.get_menu()
        food_item = search_str.lower()
        if food_item in menu_dict:
            print(f"{food_item} Wholesale: ${menu_dict[food_item].get_wholesale_cost()}  Retail: ${menu_dict[food_item].get_selling_price()}")
        else:
            print("Item does not exist.")

    def enter_sales_for_today(self, daily_sales_dict):
        missing_food_item = False
        menu_dict = self.get_menu()
        lower_case_daily_sales_dict = dict((key.lower(), value) for key, value in daily_sales_dict.items()) # sets dict keys to lower
        for food_entry in lower_case_daily_sales_dict:
            if food_entry.lower() not in menu_dict:
                missing_food_item = True
        try:
            if missing_food_item == False:
                day = self.get_current_day()
                self._sales_record.append(SalesForDay(day, lower_case_daily_sales_dict))
                self._current_day += 1
            else:
                raise InvalidSalesItemError
            
        except InvalidSalesItemError:
            print("Invalid sales item. Try again.")
            raise SystemExit()
        
    def sales_of_menu_item_for_day(self, day_number, menu_item_search_str):
        food_item_name = menu_item_search_str.lower()
        if food_item_name in self.get_sales_record()[day_number].get_sales_dict():
            return self.get_sales_record()[day_number].get_sales_dict()[food_item_name]
        else:
            print("Item not found")
            return 0

    def total_sale_for_menu_item(self, menu_item_search_str):
        menu_item_number = 0
        food_item_name = menu_item_search_str.lower()
        for each_day_in_list in self.get_sales_record():
            if food_item_name in each_day_in_list.get_sales_dict():
                menu_item_number += each_day_in_list.get_sales_dict()[food_item_name]
        return menu_item_number
    
    def total_profit_for_menu_item(self, menu_item_search_str):
        item_count = self.total_sale_for_menu_item(menu_item_search_str)
        menu_dict = self.get_menu()
        food_item_name = menu_item_search_str.lower()
        if food_item_name in menu_dict:
            retail = menu_dict[food_item_name].get_selling_price()
            wholesale = menu_dict[food_item_name].get_wholesale_cost()
            # print(f"{food_item_name} Wholesale: ${menu_dict[food_item_name].get_wholesale_cost()}  Retail: ${menu_dict[food_item_name].get_selling_price()}")
            return round(item_count * (retail - wholesale), 2)
        else:
            return ("Item does not exist.")
        
    def total_profit_for_stand(self):
        sum_of_all_sales = 0
        for each_food_item in self.get_menu():
            sum_of_all_sales += self.total_profit_for_menu_item(each_food_item)
        return round(sum_of_all_sales, 2)

if __name__ == '__main__':
    stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
    item1 = MenuItem('Lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    day_0_sales = {
    'lemoNade' : 5,
    'cookie'   : 2
    }
    day_1_sales = {
    'nori' : 1,
    'Cookie'   : 4
    }

    stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    stand.enter_sales_for_today(day_1_sales)  # Record the sales for day zero

    print(f'Total number of cookies sold: {stand.total_sale_for_menu_item("Cookie")}')
    print(f'Total number of lemonade sold: {stand.total_sale_for_menu_item("lemonade")}')
    print(f'Total number nori of sold: {stand.total_sale_for_menu_item("Nori")}')

    print(f'Total profit for cookies sold: ${stand.total_profit_for_menu_item("cookie")}')
    print(f'Total profit for lemonade sold: ${stand.total_profit_for_menu_item("lemonade")}')
    print(f'Total profit for nori sold: ${stand.total_profit_for_menu_item("NORI")}')
    
    print(f"Total lemonade stand profit: ${stand.total_profit_for_stand()}")
    
    day_3_sales = {
        'nori' : 1,
        'drink'   : 4
        }
    stand.enter_sales_for_today(day_3_sales)  # This will raise an exception