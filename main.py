from kivy.app import App
import sqlite3
from datetime import date
import daily_data
from daily_data import daily_summary, daily_income, price_by_code, fund_name
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView



# db.execute("DROP TABLE main_table")
# db.execute("CREATE TABLE main_table ("
#            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#            "portfolio_name TEXT NOT NULL,"
#            "fund_code TEXT NOT NULL,"
#            "fund_name TEXT NOT NULL,"
#            "fund_share INTEGER NOT NULL,"
#            "share_value FLOAT NOT NULL,"
#            "invest_amount FLOAT NOT NULL,"
#            "buy_date TEXT NOT NULL"
#            ");")


class MyGridLayout(Widget):
    portfolio_name = ObjectProperty(None)
    fund_code = ObjectProperty(None)
    share_amount = ObjectProperty(None)
    first_price = ObjectProperty(None)
    add_label = ObjectProperty(None)
    my_portfolio_output = ObjectProperty(None)
    search_fund_code = ObjectProperty(None)
    search_button = ObjectProperty(None)
    search_output = ObjectProperty(None)
    delete_id = ObjectProperty(None)
    delete_output = ObjectProperty(None)

    def save_fund_button(self):
        '''
        Saves a new fund to database from user
        :return:
        '''
        # sql connection
        conn = sqlite3.connect("portfolio.db")
        db = conn.cursor()

        # kivy ids
        portfolio_name = self.portfolio_name.text
        fund_code = self.fund_code.text.upper()
        share_amount = self.share_amount.text
        first_price = self.first_price.text

        # clear text boxes input
        self.portfolio_name.text = " "
        self.fund_code = " "
        self.share_amount = " "
        self.first_price = " "

        # sql saving data
        try:
            day = date.today()
            today = f"{day.day}-{day.month}-{day.year}"
            invest_amount = float(share_amount) * float(first_price)
            db.execute(
                "INSERT INTO main_table ("
                "portfolio_name, "
                "fund_code, "
                "fund_name, "
                "fund_share, "
                "share_value, "
                "invest_amount, "
                "buy_date) "
                "VALUES  (?,?,?,?,?,?,?)",
                (portfolio_name, fund_code, fund_name(fund_code), share_amount, first_price, invest_amount, today))

            self.add_label.text = "Fund successfully saved to database!"
        except:
            print("ERROR")
            self.add_label.text = "ERROR: Please be sure your input is correct"
        # for console
        print(
            f"Portfolio name: {portfolio_name} , your fund code: {fund_code}, fund_name{fund_name(fund_code)}, buy "
            f"price: {first_price} ,current share value: {price_by_code(fund_code)}, share_amount: {share_amount}")
        # close sql
        conn.commit()
        conn.close()

    def delete_a_fund(self):
        '''
        Deletes a fund from database
        :return:
        '''
        # sql connection
        conn = sqlite3.connect("portfolio.db")
        db = conn.cursor()

        # kivy id
        delete_id = self.delete_id.text

        try:
            db.execute(f"DELETE FROM main_table WHERE id = {delete_id}")
            self.delete_output.text = f"ID: {delete_id} successfully deleted!"
        except:
            print("ERROR")
            self.delete_output.text = f"Something went wrong. \n Are you sure that id exist?"

        # close sql
        conn.commit()
        conn.close()

    def show_my_portfolio(self):
        '''
        Display current portfolio and calculates Profit/Loss
        :return:
        '''
        # sql connection
        conn = sqlite3.connect("portfolio.db")
        db = conn.cursor()
        db.execute("SELECT * FROM main_table")
        list = db.fetchall()
        conn.commit()
        conn.close()

        output = ""
        self.my_portfolio_output.text = ""

        # Turkish version of headers
        # heads = ("ID:", "Portfoy Adı:", "Fon Kodu:", "Fon ADI:", "Pay Adedi:", "Pay Alış fiyatı:", "Giriş sermayesi: ",
        #          "Kayıt Tarihi: ")

        # English version
        heads = ("ID:", "Portfolio Name:", "Fund Code:", "Fund Name:", "Share Amount:", "Buying Price:",
                 "Buying Price(Total): ", "Fund Adding date: ")

        # iterating data one by one
        for data in list:
            for i in range(len(data)):
                output = f"{output}\n {heads[i]}{data[i]}"
                # self.my_portfolio_output.text = f'{output}'

            # profit or loss calculation with live prices
            fund_value_today = price_by_code(data[2]) * data[4]
            profit = fund_value_today - data[6]
            profit_percent = ((fund_value_today / data[6]) - 1) * 100
            # adding profit/loss to table

            output = f"""{output}\n 
Current Value of Investment: {fund_value_today}
Return : {profit}
Return (%) : %{profit_percent}\n
                        """
            output = f"{output}\n ------------------------------"

            #####Turkish version#######
            # output = f"""{output}\n
            # Fonun bugünkü değeri: {fund_value_today}
            # KAR / ZARAR : {profit}
            # KAR / ZARAR (%) : %{profit_percent}\n
            #             """
            # output = f"{output}\n ------------------------------"

            self.my_portfolio_output.text = f'{output}'

    def search_fund_by_code(self):
        """
        Searches live data of fund
        """
        search_fund_code = self.search_fund_code.text.upper()
        self.search_output.text = daily_data.fund_general_info(search_fund_code)


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
