import pandas as pd
from flask import Flask, jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/coffe', methods=['GET'])
def get_coffe_price():
    coffe_data = pd.read_csv(
        "C:..\\..\\web scrap\\Combine scrape price in Script(pycharm)\\webscrapingGui\\web_scraping\\data\\kopi o price.csv")
    coffe_data["Date"] = coffe_data["Date"].apply(lambda x: pd.to_datetime(x.replace("/", "-"), format="%d-%m-%Y"))
    coffe_date_by_month = coffe_data.groupby(pd.Grouper(key='Date', freq="M"))[
        ["Shopee Price", "Lazada Price", "PGMall Price"]].mean()
    coffe_date_by_month.index = coffe_date_by_month.index.astype(str)
    coffe_date_by_month = coffe_date_by_month.reset_index()
    # coffe_date_by_month = coffe_date_by_month.where(pd.notna(coffe_date_by_month), None)
    coffe_date_by_month.fillna(0,inplace = True)
    data_to_return ={
        "Date":coffe_date_by_month["Date"].to_list(),
        "Shopee":coffe_date_by_month["Shopee Price"].to_list(),
        "Lazada":coffe_date_by_month["Lazada Price"].to_list(),
        "PGMall":coffe_date_by_month["PGMall Price"].to_list()
    }

    return data_to_return

if __name__=='__main__':
    app.run(debug=True)
