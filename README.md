# HTTP Security Headers Scanner

A lightweight Python utility designed to analyze web application response headers against industry security best practices.

## Overview
Web application security often starts with fundamental HTTP response headers. This tool scans a given target domain and evaluates the presence of critical defensive headers, highlighting potential security misconfigurations.

## Headers Checked
- **Strict-Transport-Security (HSTS):** Prevents man-in-the-middle attacks via forced HTTPS.
- **Content-Security-Policy (CSP):** Mitigates XSS and data injection vulnerabilities.
- **X-Frame-Options:** Prevents Clickjacking attacks.
- **X-Content-Type-Options:** Prevents MIME-sniffing exploits.
- **Referrer-Policy:** Protects sensitive referrer metadata from leaking.
- **Permissions-Policy:** Restricts browser hardware access (e.g., camera, microphone).

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/http-headers-scanner.git
   cd http-headers-scanner