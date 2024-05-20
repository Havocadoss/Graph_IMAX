import pandas
import matplotlib.pyplot as plt
with open('stock.html', 'r') as f:
  webpage = f.read()
tables = pandas.read_html(webpage)
df = tables[0]
print(df.info())
plt.plot(df[('IMAX Historical Annual Stock Price Data', 'Year')], df[('IMAX Historical Annual Stock Price Data', 'Year Close')])
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('IMAX Stock Price History')
plt.show()