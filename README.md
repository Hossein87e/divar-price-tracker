# Divar Price Tracker Bot 🤖📉
**Bilingual Repository (English & Persian) | مخزن دو زبانه**

---

## 🇬🇧 English Section

### 📌 About the Project
This project is an intelligent Telegram bot designed to monitor, extract, and analyze advertisement prices from dynamic platforms like Divar. Instead of just basic scraping, it integrates a Machine Learning pipeline to evaluate the market features and predict whether a listed price is reasonable or overvalued.

### 🚀 Key Features
*   **Dynamic Web Scraping:** Utilizes `Playwright` to handle JavaScript-rendered pages and extract real-time data seamlessly.
*   **Machine Learning Integration:** Employs a `Random Forest Regressor` (via Scikit-Learn) to analyze features and predict price trends based on historical data.
*   **Data Management:** Efficiently stores and manages scraped items, user requests, and historical prices using a lightweight `SQLite` database.
*   **User-Friendly Interface:** Operates entirely through a Telegram bot, allowing users to send links and receive instant AI-powered price analysis.

### 🛠️ Built With
*   **Language:** Python
*   **Scraping:** Playwright
*   **Machine Learning:** Scikit-Learn, Pandas
*   **Database:** SQLite
*   **Bot API:** pyTelegramBotAPI (Telebot)

---

## 🇮🇷 بخش فارسی

### 📌 درباره پروژه
این پروژه یک ربات هوشمند تلگرامی است که با هدف ردیابی، استخراج و تحلیل قیمت آگهی‌ها از سایت‌هایی مانند «دیوار» توسعه یافته است. این سیستم فراتر از یک اسکریپر ساده عمل می‌کند؛ با اتصال به یک مدل یادگیری ماشین، ویژگی‌های آگهی را تحلیل کرده و منطقی بودن یا حباب داشتن قیمت را پیش‌بینی می‌کند.

### 🚀 ویژگی‌های کلیدی
*   **استخراج داده‌های پویا (Web Scraping):** استفاده از `Playwright` برای دور زدن محدودیت‌های رندر جاوا اسکریپت و استخراج لحظه‌ای اطلاعات آگهی‌ها.
*   **تحلیل با یادگیری ماشین:** بهره‌گیری از الگوریتم `Random Forest Regressor` برای پردازش ویژگی‌های کالا و پیش‌بینی هوشمند روند قیمت‌گذاری.
*   **مدیریت بهینه داده‌ها:** استفاده از پایگاه داده محلی `SQLite` برای ذخیره‌سازی سریع و ساختاریافته تاریخچه قیمت‌ها و اطلاعات کاربران.
*   **رابط کاربری در دسترس:** تعامل کامل کاربر از طریق تلگرام برای ارسال لینک آگهی و دریافت تحلیل هوشمند در کسری از ثانیه.

### 🛠️ تکنولوژی‌های استفاده شده
*   **زبان برنامه‌نویسی:** پایتون (Python)
*   **استخراج داده:** Playwright
*   **یادگیری ماشین:** Scikit-Learn, Pandas
*   **پایگاه داده:** SQLite
*   **رابط تلگرام:** Telebot
