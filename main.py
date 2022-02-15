from bs4 import BeautifulSoup as soup

INPUT_FILES = {
    "1": False,
    "2": False,
    "3": False,
    "4": False,
    "5": False,
    "6": False,
    "7": False,
    "8": False,
    "9": False,
    "10": False,
    "11": False,
    "12": False,
    "13": False,
    "14": False,
    "15": False,
    "16": False,
    "17": False,
    "18": False,
    "19": False,
    "20": False,
    "22": False,
    "23": False,
    "24": False,
    # "25": False,
}
READ_ALL = False

output_filename = "output_files/slidesho_apps" + ".csv"
output_file = open(output_filename, "a")
headers = "title, subtitle, publisher, country, year, last_month_downloads, last_month_revenue\n"
# output_file.write(headers)

def clean_value(value):
    if not value:
        return ""
    return value.text.strip()

for file_name, visited in INPUT_FILES.items():
    if not visited or READ_ALL:
        input_file = open("input_files/" + file_name + ".html", "r+")
        file_content = input_file.read()
        page_soup = soup(file_content, 'html.parser')
        title = clean_value(page_soup.find("span", {"class":"app-name-wrapper"}))
        sub_title = clean_value(page_soup.find("h3", {"class":"subtitle-text"}))
        last_month_downloads = clean_value(page_soup.find("span", {"class":"downloads"}))
        last_month_revenue = clean_value(page_soup.find("span", {"class": "revenue"}))
        about_items = page_soup.find("table", {"class":"about-app-table"}).find_all("tr")
        for item in about_items:
            if item.find("td", {"class": "name"}).text.strip() == "Support URL:":
                publisher = clean_value(item.find("td", {"class": "value"}))
            if item.find("td", {"class": "name"}).text.strip() == "Most Popular Country:":
                country = clean_value(item.find("td", {"class": "value"}))
            if item.find("td", {"class": "name"}).text.strip() == "Country Release Date:":
                release_date = clean_value(item.find("td", {"class": "value"}))
        input_file.close()

    output_file.write(title + ", " + sub_title + ", " + publisher + ", " + country + ", " + release_date +", " + last_month_downloads +", " + last_month_revenue + "\n")
output_file.close()
