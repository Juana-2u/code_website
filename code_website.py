import requests

def check_website(url):
    # 如果用户没写协议，加上 http://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if status_code == 200:
            print(f"[+] 可访问: {url} (状态码 {status_code})")
            return url
        else:
            print(f"[-] {url} 返回状态码: {status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[!] {url} 访问失败: {e}")
        return None


if __name__ == "__main__":
    input_file = "urls.txt"   # 存放子域名的文件
    output_file = "alive_urls.txt"  # 存放可访问的URL

    alive_urls = []

    with open(input_file, "r") as f:
        for line in f:
            url = line.strip()
            if url:  # 跳过空行
                result = check_website(url)
                if result:
                    alive_urls.append(result)

    # 保存结果到文件
    with open(output_file, "w") as f:
        for url in alive_urls:
            f.write(url + "\n")

    print(f"\n[✓] 检测完成，可访问的URL已保存到 {output_file}")
