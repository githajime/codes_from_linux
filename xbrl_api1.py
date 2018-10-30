import requests
from bs4 import BeautifulSoup
import re
import time

# エンドポイントにリクエスト
response = requests.get("http://resource.ufocatch.com/atom/edinet/query/G01003")
response.encoding = response.apparent_encoding

# レスポンスをBS4でHTMLを解析
soup = BeautifulSoup(response.text, "lxml")
links = soup.find_all("link")

# 返ってきた一覧のうち、.xbrlかどうかを正規表現で判別
pattern = ".*PublicDoc.*\.xbrl"

for lin in links:
	result = re.search(pattern , lin.get("href"))

	# .xbrlであれば、xbrlを取得
	if result != None:
		print(lin.get("href"))
		response = requests.get(lin.get("href"))
		response.encoding = response.apparent_encoding
		print(response.text)

	else:
		pass

	time.sleep(2.0)
