# Subdomain Fetcher by 91233





从 [crt.sh](https://crt.sh/) 抓取指定域名的子域名，并生成 TXT 文件。支持彩色命令行输出，动态进度条显示。

------

## 功能

- 抓取指定主域名的子域名（自动去重、去掉通配符 `*.`）
- 彩色命令行 Logo 和信息输出
- 彩色进度条显示写入 TXT 文件进度
- 命令行参数支持自定义输出文件名
- 每行一个子域名，方便后续处理或安全分析

------

## 环境要求

- Python 3.6+
- 第三方库：
  - [requests](https://pypi.org/project/requests/)
  - [rich](https://pypi.org/project/rich/)

安装依赖：

```
pip install requests rich
```

------

## 使用方法

### 查看帮助

```
python crt.py -h
```

输出示例：

```
从 crt.sh 抓取子域名并保存到 TXT 文件
示例: python crt.py -u tal.com

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     主域名，例如 tal.com
  -o OUTPUT, --output OUTPUT
                        输出文件名，默认 <domain>_subdomains.txt
```

### 抓取子域名并生成 TXT 文件

```
python crt.py -u tal.com
```

- 默认生成 `tal.com_subdomains.txt`
- 子域名输出为白色，进度条显示写入进度

### 指定输出文件名

```
python crt.py -u tal.com -o my_subdomains.txt
```

- 输出文件名为 `my_subdomains.txt`

------

## 脚本效果

- 彩色 Logo 动态打印
- 彩色进度条显示写入 TXT 文件
- 子域名列表白色输出，整洁清晰

示例：

```
  _____ _____ _______       _     
 / ____|_   _|__   __|/\   | |   
| |      | |    | |  /  \  | |   
| |      | |    | | / /\ \ | |   
| |____ _| |_   | |/ ____ \| |____
 \_____|_____|  |_/_/    \_\______|

    Subdomain Fetcher by 91233
抓取 crt.sh 子域名并生成 TXT 文件

[*] 正在请求: https://crt.sh/?q=%.tal.com&output=json
[+] 共发现 25 个子域名，保存到 tal.com_subdomains.txt

autodiscover.tal.com
cloud.tal.com
mail.tal.com
...
```

------

## 文件说明

- `crt.py`：主脚本
- `<domain>_subdomains.txt`：抓取的子域名列表，每行一个

------

## 许可证

MIT License © 2025 91233
