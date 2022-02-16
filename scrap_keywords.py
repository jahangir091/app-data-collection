from bs4 import BeautifulSoup as soup
import os


def clean_value(value):
    if not value:
        return ""
    return value.text.strip()


for filename in os.listdir(os.getcwd() + "/input_files/slideshow/keywords"):
    if filename.endswith(".html"):
        with open(os.path.join(os.getcwd() + "/input_files/slideshow/keywords", filename), 'r') as f:
            file_content = f.read()
            page_soup = soup(file_content, 'html.parser')

            output_filename = "output_files/slideshow/keywords/" + os.path.splitext(filename)[0]+'.csv'
            output_file = open(output_filename, "a")
            headers = "search term, traffic, iphone difficulty, ipad difficulty\n"
            output_file.write(headers)

            table_rows = page_soup.find("div", {"class": "keyword-ranking-content"}).table.tbody.find_all("tr")
            for table_row in table_rows:
                table_cols = table_row.find_all("td")[:4]

                search_term = clean_value(table_cols[0])
                traffic = clean_value(table_cols[1])
                iphone_difficulty = clean_value(table_cols[2])
                ipad_difficulty = clean_value(table_cols[3])

                output_file.write(search_term + ", " + traffic + ", " + iphone_difficulty + ", " + ipad_difficulty + "\n")
            output_file.close()
