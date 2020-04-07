## 版本變更
目前主程式有兩個，Scrapy版本是改良過  
1. [.ipynb版本](./.ipynb_checkpoints/爬蟲國中時期的照片-checkpoint.ipynb)使用selenium爬蟲  
2. [Scrapy版本](./ScrapyCrawlerJHS/)使用Scrapy爬取圖片的下載Spyder專案
## 功能簡述
從網站的相簿中下載圖片到本地端，  
使用selenium取得DOM，使用multiprocessing並行下載圖片。  

## 環境
macOS Mojave 10.14.6（18G2022）  
Python 3.6.10 :: Anaconda, Inc.  
selenium                  3.5.0  
urllib3                   1.22  

#### 其實底下這幾行，只要conda install jupyter就完成
jupyter                   1.0.0  
jupyter_client            5.3.4  
jupyter_console           6.1.0  
jupyter_core              4.6.1  

上面這些都可以使用conda安裝，  
但selenium需要一個chromedriver，  
建議自行去官網[下載](https://chromedriver.chromium.org/downloads/)(對應的Chrome版本＆作業系統)，  
解壓縮在與.ipynb同樣資料夾底下即可。  

Scrapy版本不需要安裝selenium，且速度更快。
但Scrapy目前只先產生[下載圖片URL的JSON檔](./ScrapyCrawlerJHS/scrapyJHS/hello.json)，尚未實作下載部分。
### 備註
預設的輸出資料夾名稱為result，執行.ipynb會自動建立(包含子目錄)

## 程式大綱
程式由Part1 ~Part5組成。
### Part 1~3 
使用selenium對整個網頁進行DOM分析並產生new_url_results.json。
### Part 4
 讀取new_url_results.json並將其轉為字典(key:網頁圖片的下載網址, value:將儲存圖片的本地端絕對位置)，  
 同時也建立本地端對應圖片的資料夾。  
### Part 5
多程序(Multiprocess)下載圖片到本地端。

