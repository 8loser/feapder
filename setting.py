import os

# MYSQL
# MYSQL_IP = ""
# MYSQL_PORT = 3306
# MYSQL_DB = ""
# MYSQL_USER_NAME = ""
# MYSQL_USER_PASS = ""

# REDIS
# IP:PORT
# REDISDB_IP_PORTS = "xxx:6379"
# REDISDB_USER_PASS = ""
# 默認 0 到 15 共16個數據庫
# REDISDB_DB = 0

# 數據入庫的pipeline，可自定義，默認MysqlPipeline
# ITEM_PIPELINES = ["feapder.pipelines.mysql_pipeline.MysqlPipeline"]

# 爬蟲相關
# COLLECTOR
COLLECTOR_SLEEP_TIME = 1  # 從任務隊列中獲取任務到內存隊列的間隔
COLLECTOR_TASK_COUNT = 100  # 每次獲取任務數量

# SPIDER
SPIDER_THREAD_COUNT = 10  # 爬蟲並發數
SPIDER_SLEEP_TIME = 0  # 下載時間間隔 單位秒。 支持隨機 如 SPIDER_SLEEP_TIME = [2, 5] 則間隔為 2~5秒之間的隨機數，包含2和5
SPIDER_MAX_RETRY_TIMES = 5  # 每個請求最大重試次數

# 瀏覽器渲染下載
WEBDRIVER = dict(
    pool_size=2,  # 瀏覽器的數量
    load_images=False,  # 是否加載圖片
    user_agent=None,  # 字符串 或 無參函數，返回值為user_agent
    proxy=None,  # xxx.xxx.xxx.xxx:xxxx 或 無參函數，返回值為代理地址
    headless=False,  # 是否為無頭瀏覽器
    driver_type="CHROME",  # CHROME 或 PHANTOMJS,
    timeout=30,  # 請求超時時間
    window_size=(1024, 800),  # 窗口大小
    executable_path=None,  # 瀏覽器路徑，默認為默認路徑
    render_time=2,  # 渲染時長，即打開網頁等待指定時間後再獲取源碼
    custom_argument=[
        # "--headless",
        "--disable-gpu",
        "--ignore-certificate-errors",
        "--disable-dev-shm-usage"
    ],  # 自定义浏览器渲染参数
    auto_install_driver=False)

# 重新嘗試失敗的requests 當requests重試次數超過允許的最大重試次數算失敗
RETRY_FAILED_REQUESTS = False
# request 超時時間，超過這個時間重新做（不是網絡請求的超時時間）單位秒
REQUEST_LOST_TIMEOUT = 600  # 10分鐘
# 保存失敗的request
SAVE_FAILED_REQUEST = True

# 下載緩存 利用redis緩存，由於內存小，所以僅供測試時使用
RESPONSE_CACHED_ENABLE = False  # 是否啟用下載緩存 成本高的數據或容易變需求的數據，建議設置為True
RESPONSE_CACHED_EXPIRE_TIME = 3600  # 緩存時間 秒
RESPONSE_CACHED_USED = False  # 是否使用緩存 補采數據時可設置為True

WARNING_FAILED_COUNT = 1000  # 任務失敗數 超過WARNING_FAILED_COUNT則報警

# 爬蟲是否常駐
KEEP_ALIVE = False

# 設置代理
PROXY_EXTRACT_API = None  # 代理提取API ，返回的代理分割符為\r\n
PROXY_ENABLE = True

# 隨機headers
RANDOM_HEADERS = True
# requests 使用session
USE_SESSION = False

# 去重
ITEM_FILTER_ENABLE = False  # item 去重
REQUEST_FILTER_ENABLE = False  # request 去重

# 報警 支持釘釘及郵件，二選一即可
# 釘釘報警
# DINGDING_WARNING_URL = ""  # 釘釘機器人api
# DINGDING_WARNING_PHONE = ""  # 報警人 支持列表，可指定多個
# 郵件報警
# EMAIL_SENDER = ""  # 發件人
# EMAIL_PASSWORD = ""  # 授權碼
# EMAIL_RECEIVER = ""  # 收件人 支持列表，可指定多個
# 時間間隔
WARNING_INTERVAL = 3600  # 相同報警的報警時間間隔，防止刷屏; 0表示不去重
WARNING_LEVEL = "DEBUG"  # 報警級別， DEBUG / ERROR

LOG_NAME = os.path.basename(os.getcwd())
LOG_PATH = "log/%s.log" % LOG_NAME  # log存儲路徑
LOG_LEVEL = "DEBUG"
LOG_COLOR = True  # 是否帶有顏色
LOG_IS_WRITE_TO_CONSOLE = True  # 是否打印到控制台
LOG_IS_WRITE_TO_FILE = False  # 是否寫文件
LOG_MODE = "w"  # 寫文件的模式
LOG_MAX_BYTES = 10 * 1024 * 1024  # 每個日志文件的最大字節數
LOG_BACKUP_COUNT = 20  # 日志文件保留數量
LOG_ENCODING = "utf8"  # 日志文件編碼
OTHERS_LOG_LEVAL = "ERROR"  # 第三方庫的log等級