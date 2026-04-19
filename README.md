<p align="center">
  <pre>
  ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
  ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
  ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
  ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
  ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
  
  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
  ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
  ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  </pre>
</p>

<h1 align="center">🕵️ INSTAGRAM CHECKER<br>EDUCATIONAL TOOL 🔍</h1>

<p align="center">
  <strong>Automated Instagram Account Discovery & Password Reset Flow Analysis</strong><br>
  <em>For authorised security research & educational use only</em>
</p>

<p align="center">
  <a href="https://github.com/Ali-Haidar-Sy/Instagram-Checker-Tool/stargazers"><img src="https://img.shields.io/github/stars/Ali-Haidar-Sy/Instagram-Checker-Tool?style=for-the-badge&color=yellow"></a>
  <a href="https://github.com/Ali-Haidar-Sy/Instagram-Checker-Tool/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ali-Haidar-Sy/Instagram-Checker-Tool?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://t.me/P33_9"><img src="https://img.shields.io/badge/Telegram-@P33_9-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="https://www.instagram.com/_ungn"><img src="https://img.shields.io/badge/Instagram-@_ungn-E4405F?style=for-the-badge&logo=instagram"></a>
  <a href="https://github.com/Ali-Haidar-Sy"><img src="https://img.shields.io/badge/GitHub-Ali--Haidar--Sy-181717?style=for-the-badge&logo=github"></a>
</p>

---

## ⚠️ YOU MUST UPDATE THE TOOL

> **This project evolves rapidly.** Always pull the latest version before each run:
> ```bash
> git pull origin main
> ```
> Instagram changes its API frequently – keep your copy up‑to‑date.

---

## ✨ FEATURES — WHAT IT DOES

| Category | Capabilities |
|----------|--------------|
| **Account Discovery** | Checks Instagram account existence via email/username • Uses Mailnesia temporary inbox |
| **Password Reset Flow** | Sends recovery request • Extracts reset link from email • Parses confirmation page |
| **Profile Harvesting** | Retrieves public info: full name, followers, following, posts count, private status |
| **Multi‑threading** | 10 concurrent workers • Randomised user‑agents & request IDs • HTTP/2 support |
| **Telegram Integration** | Sends found accounts + reset links directly to your Telegram bot (optional) |
| **Output Formats** | Saves results to `hits1.txt` • Clean, formatted console output with colours |

---

## 🚀 QUICK START

```
# 1. Clone the repository
git clone https://github.com/Ali-Haidar-Sy/Instagram-Checker-Tool.git
cd Instagram-Checker-Tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the tool
python checker.py
Example session
text
Enter Your Token: (optional – your Telegram bot token)
Enter ID: (optional – your Telegram chat ID)

[+] Starting Instagram account checker...
[+] Generating random Instagram IDs...
[+] Sending password reset requests...
When a valid account is found, you'll see:

text
username : john_doe
email    : john@mailnesia.com
followers: 1240
Reset link: https://instagram.com/accounts/password/reset/confirm/...
All results are saved to hits1.txt and optionally sent to Telegram.

📸 PREVIEW
Console output	Telegram alert
https://via.placeholder.com/400x200?text=Colourful+terminal+output	https://via.placeholder.com/400x200?text=Telegram+message+with+reset+link
(Replace placeholders with actual screenshots after running the tool)

🛡️ LEGAL DISCLAIMER
This tool is for educational purposes and authorised security research only.
Using it to recover or compromise Instagram accounts without explicit permission violates Instagram’s Terms of Service and may be illegal in your jurisdiction.
The author is not responsible for any misuse. Always obtain written consent before testing any account that is not your own.

🤝 CONTRIBUTING
Found a bug? Want to add support for another temporary email service?
Open an Issue or submit a Pull Request. Contributions are welcome!

📞 CONNECT WITH ME
Platform	Handle
Telegram	@P33_9
Instagram	@_ungn
GitHub	Ali-Haidar-Sy
<p align="center"> <strong>🕵️ Use responsibly, stay ethical, and keep learning. 🔍</strong><br> ⭐ If this tool helped you understand Instagram’s recovery flow, give it a star! ⭐ </p> ```
