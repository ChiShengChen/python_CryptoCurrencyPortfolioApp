from tkinter import *    #tkinter 是一個python視窗的庫
import matplotlib.pyplot as plt
import requests
import json
import os
os.system('cls')  #windows清視窗

###############################
api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content.decode('utf-8'))   

root = Tk()  #建立視窗物件root

root.title("Crypto Currency Portfolio")
#root.iconbitmap(r'c:\mmm.jpg')  #設定視窗左上小圖標(放圖片檔案路徑)

#name = Label(root, text = "Meow", bg = "blue", fg = "white")  #視窗中的文字  #bg=background color  #fg=front ground color
#name.grid(row = 0, column = 0, sticky = N+E+W+S)  #視窗中的行列順續數(第幾行幾列)(塞文字用)#row是-的，column是|的   #sticky是讓視窗能夠拉大

def red_green(amount):
	if amount >= 0:
		return "green"
	else:
		return "red"

# ******************* CREATE HEADER ********************** header就是視窗表格的最上排標題(以表格呈現)
header_name = Label(root, text="Name", bg="white", font = "Verdana 8 bold")
header_name.grid(row=0, column=0, sticky=N+S+E+W)

header_rank = Label(root, text="Rank", bg="silver", font = "Verdana 8 bold")
header_rank.grid(row=0, column=1, sticky=N+S+E+W)

header_current_price = Label(root, text="Current Price", bg="white", font = "Verdana 8 bold")
header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

header_price_paid = Label(root, text="Price Paid", bg="silver", font = "Verdana 8 bold")
header_price_paid.grid(row=0, column=3, sticky=N+S+E+W)

header_profit_loss_per = Label(root, text="Profit/Loss Per", bg="white", font = "Verdana 8 bold")
header_profit_loss_per.grid(row=0, column=4, sticky=N+S+E+W)

header_1_hr_change = Label(root, text="1 HR Change", bg="silver", font = "Verdana 8 bold")
header_1_hr_change.grid(row=0, column=5, sticky=N+S+E+W)

header_24_hr_change = Label(root, text="24 HR Change", bg="white", font = "Verdana 8 bold")
header_24_hr_change.grid(row=0, column=6, sticky=N+S+E+W)

header_7_day_change = Label(root, text="7 Day Change", bg="silver", font = "Verdana 8 bold")
header_7_day_change.grid(row=0, column=7, sticky=N+S+E+W)

header_current_value = Label(root, text="Current Value", bg="white", font = "Verdana 8 bold")
header_current_value.grid(row=0, column=8, sticky=N+S+E+W)

header_profit_loss_total = Label(root, text="Profit/Loss Total", bg="silver", font = "Verdana 8 bold")
header_profit_loss_total.grid(row=0, column=9, sticky=N+S+E+W)

#################################################################




currencies = ["BTC", "ETH", "MIOTA", "ZEC"]



print("--------------------------------------")

def lookcyc():
	api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
	api = json.loads(api_request.content.decode('utf-8'))   #json.loads(api_request.content.decode('utf-8'))
    #print(api)

    #my_portfolio
	my_portfolio = [
		{
			"sym": "BTC",
			"amount_owned": 0,
			"price_paid_per": 0
		},

		{
			"sym": "STEEM",
			"amount_owned": 3000,
			"price_paid_per": .80
		},
		{
			"sym": "XRP",
			"amount_owned": 5000,
			"price_paid_per": .20
		},
		{
			"sym": "XLM",
			"amount_owned": 2000,
			"price_paid_per": .10
		},
		{
			"sym": "EOS",
			"amount_owned": 1000,
			"price_paid_per": 2.00
		}

    ]

	total_profit_loss = 0
	row_count = 1
	total_current_value = 0

	pie = []
	pie_size = []

	for x in api:
	    for coin in my_portfolio:          #可以試試 for coin in currencies
		    if coin["sym"] == x["symbol"]:

			    total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
			    current_vaslue = float(coin["amount_owned"]) * float(x["price_usd"])
			    profit_loss = current_vaslue - total_paid
			    total_profit_loss += profit_loss
			    profit_loss_percoin = float(x["price_usd"]) - float(coin["price_paid_per"])

			    pie.append(x["name"])
			    pie_size.append(coin["amount_owned"])

			    #print(x["name"])
			    #print("${:.3f}".format(float(x["price_usd"])))
			    #print("Rank:{:.0f}".format(float(x["rank"])))
			    #print("total_paid ${:.3f}".format(float(total_paid)))
			    #print("current_vaslue ${:.3f}".format(float(current_vaslue)))
			    #print("profit_loss ${:.3f}".format(float(profit_loss)))
			    #print("profit_loss_percoin: ${:3f}".format(float(profit_loss_percoin)))
			    #print("--------------------------------------")

			    name = Label(root, text=x["name"], bg="white")
			    name.grid(row=row_count, column=0, sticky=N+S+E+W)

			    rank = Label(root, text=x["rank"], bg="silver")
			    rank.grid(row=row_count, column=1, sticky=N+S+E+W)

			    current_price = Label(root, text="${0:.2f}".format(float(x["price_usd"])), bg="white",)
			    current_price.grid(row=row_count, column=2, sticky=N+S+E+W)

			    price_paid = Label(root, text="${0:.2f}".format(float(coin["price_paid_per"])), bg="silver")
			    price_paid.grid(row=row_count, column=3, sticky=N+S+E+W)

			    profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_percoin)), bg="white", fg=red_green(float(profit_loss_percoin)))
			    profit_loss_per.grid(row=row_count, column=4, sticky=N+S+E+W)

			    one_hr_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_1h"])), bg="silver", fg=red_green(float(x["percent_change_1h"])))
			    one_hr_change.grid(row=row_count, column=5, sticky=N+S+E+W)

			    tf_hr_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_24h"])), bg="white", fg=red_green(float(x["percent_change_24h"])))
			    tf_hr_change.grid(row=row_count, column=6, sticky=N+S+E+W)

			    seven_day_change = Label(root, text="{0:.2f}%".format(float(x["percent_change_7d"])), bg="silver", fg=red_green(float(x["percent_change_7d"])))
			    seven_day_change.grid(row=row_count, column=7, sticky=N+S+E+W)

			    current_value = Label(root, text="${0:.2f}".format(float(current_vaslue)), bg="white")
			    current_value.grid(row=row_count, column=8, sticky=N+S+E+W)

			    profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss)), bg="silver", fg=red_green(float(profit_loss)))
			    profit_loss_total.grid(row=row_count, column=9, sticky=N+S+E+W)

			    row_count += 1

				    
    #print("total_profit_loss: ${:3f}".format(float(total_profit_loss)))		#不知為啥印不出來@@
	total_profit_loss = Label(root, text="P/L: ${0:.2f}".format(float(total_profit_loss)), font="Verdana 8 bold", fg=red_green(float(total_profit_loss)))
	total_profit_loss.grid(row=row_count, column=0, sticky=W, padx=10, pady=10)
	#total_current_value_output = Label(root, text="P/L: ${0:.2f}".format(float(total_current_value)), font="Verdana 8 bold", fg=red_green(float(total_profit_loss)))
	#total_current_value_output.grid(row=row_count+1, column=1, sticky=W, padx=10, pady=10)

	#更新數值
	api = ""
	update_button = Button(root, text="Update Prices", command=lookcyc) #更新按鈕 command=lookcyc是按按鈕後執行lookcyc()
	update_button.grid(row=row_count, column=9, sticky=E+S, padx=10, pady=10)


	def graph(pie, pie_size):
		labels = pie
		sizes = pie_size
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
		patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
		plt.legend(patches, labels, loc="best")
		plt.axis('equal')
		plt.tight_layout()
		plt.show()

	graph_button = Button(root, text="Pie Chart", command= lambda: graph(pie, pie_size))
	graph_button.grid(row=row_count, column=8, sticky=E+S, padx=10, pady=10)

lookcyc()
	
root.mainloop()  #去不斷loop來更新視窗

