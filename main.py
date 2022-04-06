from send_sms import message

import pandas as pd

month_lists = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
GOAL = 55000
for month in month_lists:
    sales_table = pd.read_excel(f"tabelas/{month}.xlsx")
    if (sales_table["Vendas"] > GOAL).any():
        seller = sales_table.loc[sales_table["Vendas"] > GOAL, "Vendedor"].values[0]
        number_of_sales = sales_table.loc[sales_table["Vendas"] > GOAL, "Vendas"].values[0]
        content = f"In {month} month someone has completed more than {GOAL} sells. Seller: {seller}, Sales: {number_of_sales}."
        message(content)