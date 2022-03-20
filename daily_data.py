import requests
from bs4 import BeautifulSoup



from fon_code_import import make_code_list


headers = {
    "User-Agernt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}


def daily_summary(code):
    url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={code}"

    r = requests.get(url)
    print(code)
    soup = BeautifulSoup(r.text, "html.parser")
    fon = soup.find("ul", {"class": "top-list"})
    price = fon.findAll("span")
    head = ("Son Fiyat (TL)", "Günlük Getiri (%)", "Pay (Adet)", "Fon Toplam Değer (TL)", "Kategorisi")
    for i in range(len(price)):
        print(head[i])
        print(price[i].text)


def soup_import(code):
    '''
    Main soup code for scrapping. All data comes from Government's official website.
    :param code:
    :return:
    '''
    url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={code}"
    r = requests.get(url)
    # print(code)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def daily_income(code):
    """
    Daily Profit/loss (%)
    Günlük Getiri (%)
    :param code: string fund code
    :return: string ratio
    """
    soup = soup_import(code)
    # url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={code}"
    # r = requests.get(url)
    # print(code)
    # soup = BeautifulSoup(r.text, "html.parser")
    fon = soup.find("ul", {"class": "top-list"})
    price = fon.findAll("span")
    return str(price[1].text)


def total_share(code):
    """
    Total Share Amount
    Pay (Adet)
    :param code: string fund code
    :return: string share
    """
    soup = soup_import(code)
    fon = soup.find("ul", {"class": "top-list"})
    price = fon.findAll("span")
    return str(price[2].text)


def total_value(code):
    """
    Fund Total Value by Turkish Lira
    Fon Toplam Değer (TL)
    :param code: string fund code
    :return: string total value
    """
    soup = soup_import(code)
    fon = soup.find("ul", {"class": "top-list"})
    price = fon.findAll("span")
    return str(price[3].text)


def category(code):
    """
    Category of the fund
    :param code: string fund code
    :return: string fund type
    """
    soup = soup_import(code)
    fon = soup.find("ul", {"class": "top-list"})
    price = fon.findAll("span")
    return str(price[4].text)


def price_by_code(code):
    """
    gets live price of a singe share by code
    :param code: (str) fon code in three letters
    :return: float price
    """
    url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={code}"

    r = requests.get(url)
    # print(code)
    soup = BeautifulSoup(r.text, "html.parser")

    fon = soup.find("ul", {"class": "top-list"})
    price = fon.find("span")
    xx = str(price).strip("<span></")
    xx = xx.replace(",", ".")
    xx = float(xx)
    return xx


# simple test table
# print("Son Fiyat (TL): " + str(price_by_code("YAY")))
# print("Günlük getiri: " + daily_income("YAY"))
# print("Pay (Adet): " + total_share("YAY"))
# print("Fon Toplam Değer (TL): " + total_value("YAY"))
# print("Kategorisi: " + category("YAY"))


def category_rank(code):
    """
    Ranking score in its own category
    Son Bir Yıllık Kategori Derecesi
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "main-indicators"})
    price = fon.findAll("span")
    return str(price[6].text)


def investor_count(code):
    """
    Investor count(people)
    Yatırımcı Sayısı (Kişi)
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "main-indicators"})
    price = fon.findAll("span")
    return str(price[7].text)


def marketshare(code):
    """
    Marketshare
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "main-indicators"})
    price = fon.findAll("span")
    return str(price[8].text)


# simple test table
# print(category_rank("YAY"))
# print(investor_count("YAY"))
# print(marketshare("YAY"))


def one_month_profit(code):
    """
    Son 1 Ay Getirisi
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "price-indicators"})
    price = fon.findAll("span")
    return str(price[0].text)


def three_month_profit(code):
    """
    Son 3 Ay Getirisi
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "price-indicators"})
    price = fon.findAll("span")
    return str(price[1].text)


def six_month_profit(code):
    """
    Son 6 Ay Getirisi
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "price-indicators"})
    price = fon.findAll("span")
    return str(price[2].text)


def one_year_profit(code):
    """
    Son 1 Yıl Getirisi
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("div", {"class": "price-indicators"})
    price = fon.findAll("span")
    return str(price[3].text)


# small test table
# print(one_month_profit("YAY"))
# print(three_month_profit("YAY"))
# print(six_month_profit("YAY"))
# print(one_year_profit("YAY"))


def fund_name(code):
    """
    Fon Adı
    :param code: string fund code
    :return: string
    """
    soup = soup_import(code)
    fon = soup.find("span", {"id": "MainContent_FormViewMainIndicators_LabelFund"})
    return str(fon.text)


# print(fund_name("YAY"))

def fund_general_info(code):
    """
    summarize live data
    :param code: str code 3 letters
    :return:
    """
    return f"""
                Fund Name: {fund_name(code)}
                Current Price (TL): {price_by_code(code)}
                Daily Return (%) : {daily_income(code)}

                Share Amount (Adet):  {total_share(code)}
                Fund Total Value (TL): {total_value(code)}
                Category: {category(code)}
                Annual Ranking (in own category): {category_rank(code)}

                Investor Count (Kişi): {investor_count(code)}
                Marketshare: {marketshare(code)}

                Last-1 month return: {one_month_profit(code)}
                Last-3 month return: {three_month_profit(code)}
                Last-6 month return: {six_month_profit(code)}
                Last-1 year return: {one_year_profit(code)}

"""
#######Turkish Version#########
# def fund_general_info(code):
#     """
#     summarize live data
#     :param code: str code 3 letters
#     :return:
#     """
#     return f"""
#                 FON ADI: {fund_name(code)}
#                 Son Fiyat (TL): {price_by_code(code)}
#                 Günlük Getiri (%) : {daily_income(code)}
#
#                 Pay (Adet):  {total_share(code)}
#                 Fon Toplam Değer (TL): {total_value(code)}
#                 Kategorisi Hisse Senedi Fonu: {category(code)}
#                 Son Bir Yıllık Kategori Derecesi: {category_rank(code)}
#
#                 Yatırımcı Sayısı (Kişi): {investor_count(code)}
#                 Pazar Payı: {marketshare(code)}
#
#                 Son 1 Ay Getirisi: {one_month_profit(code)}
#                 Son 3 Ay Getirisi: {three_month_profit(code)}
#                 Son 6 Ay Getirisi: {six_month_profit(code)}
#                 Son 1 Yıl Getirisi: {one_year_profit(code)}
#
# """
