#!/usr/bin/env python3
import requests, urllib.parse, json, argparse, time
from rich.console import Console
from rich.progress import Progress

console = Console()

# ================== 彩色 Logo ==================
def print_logo():
    logo_lines = [
        ("  _____ _____ _______       _     ", "cyan"),
        (" / ____|_   _|__   __|/\\   | |   ", "magenta"),
        ("| |      | |    | |  /  \\  | |   ", "yellow"),
        ("| |      | |    | | / /\\ \\ | |   ", "green"),
        ("| |____ _| |_   | |/ ____ \\| |____", "blue"),
        (" \\_____|_____|  |_/_/    \\_\\______|", "red"),
        ("                                   ", "white"),
        ("    Subdomain Fetcher by 91233     ", "bright_cyan"),
        ("抓取 crt.sh 子域名并生成 TXT 文件", "bright_green"),
    ]
    for line, color in logo_lines:
        console.print(line, style=color)
        time.sleep(0.05)

# ================== 获取子域名 ==================
def fetch_subdomains(domain):
    query = urllib.parse.quote(f"%.{domain}")
    url = f"https://crt.sh/?q={query}&output=json"
    console.print(f"[cyan][*][/cyan] 正在请求: {url}")
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        console.print(f"[red][!][/red] 请求失败: {e}")
        return None

    names = set()
    for entry in data:
        nv = entry.get("name_value", "")
        for n in nv.splitlines():
            n = n.strip()
            if n.startswith("*."):
                n = n[2:]
            if n:
                names.add(n)
    return sorted(names)

# ================== 保存子域名 ==================
def save_to_file(names, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for n in names:
            f.write(n + "\n")

# ================== 主函数 ==================
def main():
    print_logo()  # 打印彩色 Logo

    parser = argparse.ArgumentParser(
        description="从 crt.sh 抓取子域名并保存到 TXT 文件\n示例: python crt.py -u tal.com",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--url", required=True, help="主域名，例如 tal.com")
    parser.add_argument("-o", "--output", default=None, help="输出文件名，默认 <domain>_subdomains.txt")
    args = parser.parse_args()

    domain = args.url.strip()
    output_file = args.output if args.output else f"{domain}_subdomains.txt"

    names = fetch_subdomains(domain)
    if names is None:
        console.print("[red][!][/red] 获取子域失败")
        return

    console.print(f"[green][+][/green] 共发现 {len(names)} 个子域名，保存到 [bold]{output_file}[/bold]\n")

    with Progress() as progress:
        task = progress.add_task("[yellow]写入文件中...", total=len(names))
        with open(output_file, "w", encoding="utf-8") as f:
            for n in names:
                f.write(n + "\n")
                console.print(f"[white]{n}[/white]")  # 子域名输出为白色
                progress.update(task, advance=1)

if __name__ == "__main__":
    main()
