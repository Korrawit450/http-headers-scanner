import sys
import requests
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)

# รายการ Headers ความปลอดภัยที่ต้องการตรวจสอบ พร้อมคำแนะนำสั้นๆ
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Enforces secure (HTTPS) connections to the server.",
    "Content-Security-Policy": "Mitigates Cross-Site Scripting (XSS) and data injection attacks.",
    "X-Frame-Options": "Protects against clickjacking attacks.",
    "X-Content-Type-Options": "Prevents MIME-type sniffing.",
    "Referrer-Policy": "Controls how much referrer information is included with requests.",
    "Permissions-Policy": "Restricts browser features like camera, microphone, and geolocation."
}

def normalize_url(url: str) -> str:
    """ตรวจสอบและเติม scheme https:// หากผู้ใช้ไม่ได้ระบุ"""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

def scan_headers(target_url: str):
    target_url = normalize_url(target_url)
    print(f"\n{Fore.CYAN}Scanning target: {Style.BRIGHT}{target_url}{Style.RESET_ALL}\n")

    try:
        response = requests.get(target_url, timeout=10, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[Error] Failed to connect: {e}")
        sys.exit(1)

    headers = response.headers
    present_count = 0
    missing_count = 0

    print(f"{'Header':<30} | {'Status':<10} | {'Details'}")
    print("-" * 80)

    for header, description in SECURITY_HEADERS.items():
        if header.lower() in [h.lower() for h in headers.keys()]:
            # ค้นหาค่าจริงจาก headers
            actual_header = next(h for h in headers.keys() if h.lower() == header.lower())
            value = headers[actual_header]
            print(f"{Fore.GREEN}{header:<30} | PRESENT    | {Style.DIM}{value[:35]}...")
            present_count += 1
        else:
            print(f"{Fore.RED}{header:<30} | MISSING    | {Style.RESET_ALL}{description}")
            missing_count += 1

    print("-" * 80)
    print(f"Summary: {Fore.GREEN}{present_count} Present{Style.RESET_ALL}, {Fore.RED}{missing_count} Missing{Style.RESET_ALL}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)

    target = sys.argv[1]
    scan_headers(target)