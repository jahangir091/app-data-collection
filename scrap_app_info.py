from bs4 import BeautifulSoup as soup
import os


output_filename = "output_files/slideshow/app_info/app_info.csv"
output_file = open(output_filename, "a")
headers = "title, subtitle, publisher, country, year, last_month_downloads, last_month_revenue\n"
output_file.write(headers)


def clean_value(value):
    if not value:
        return ""
    return value.text.strip()


for filename in os.listdir(os.getcwd() + "/input_files/slideshow/app_info"):
    if filename.endswith(".html"):
        with open(os.path.join(os.getcwd() + "/input_files/slideshow/app_info", filename), 'r') as f:
            file_content = f.read()

            page_soup = soup(file_content, 'html.parser')
            title = clean_value(page_soup.find("span", {"class": "app-name-wrapper"}))
            sub_title = clean_value(page_soup.find("h3", {"class": "subtitle-text"}))
            last_month_downloads = clean_value(page_soup.find("span", {"class": "downloads"}))
            last_month_revenue = clean_value(page_soup.find("span", {"class": "revenue"}))
            about_items = page_soup.find("table", {"class": "about-app-table"}).find_all("tr")
            for item in about_items:
                if item.find("td", {"class": "name"}).text.strip() == "Support URL:":
                    publisher = clean_value(item.find("td", {"class": "value"}))
                if item.find("td", {"class": "name"}).text.strip() == "Most Popular Country:":
                    country = clean_value(item.find("td", {"class": "value"}))
                if item.find("td", {"class": "name"}).text.strip() == "Country Release Date:":
                    release_date = clean_value(item.find("td", {"class": "value"}))
        output_file.write(title + ", " + sub_title + ", " + publisher + ", " + country + ", " + release_date + ", " + last_month_downloads + ", " + last_month_revenue + "\n")
output_file.close()
