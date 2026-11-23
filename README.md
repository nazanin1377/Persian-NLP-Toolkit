# Persian NLP Toolkit

<p align="center">
  <strong>Persian Text Cleaning · Normalization · Word & Sentence Tokenization</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white">
  <img alt="Hazm" src="https://img.shields.io/badge/NLP-Hazm-276749">
  <img alt="PySide6" src="https://img.shields.io/badge/Desktop-PySide6-41CD52">
</p>

<p align="center">
  <a href="#مستندات-فارسی">مستندات فارسی</a> · <a href="#english-documentation">English documentation</a> · <a href="https://github.com/nazanin1377/Persian-NLP-Toolkit">Repository</a>
</p>

A desktop application for exploring **Persian-language text preprocessing**, built with Python, Hazm and PySide6. The interface shows each preprocessing stage separately so the effect of every transformation can be inspected.

## Application preview

<p align="center">
  <img src="docs/preview.png" alt="Screenshot of the Persian NLP Toolkit desktop application" width="650">
</p>

---

# مستندات فارسی

<div dir="rtl" align="right">

## معرفی پروژه

**Persian NLP Toolkit** یک برنامه دسکتاپ برای پیش‌پردازش متن فارسی است. کاربر متن خام را وارد می‌کند و نتیجه چهار مرحله را به‌صورت جداگانه می‌بیند: پاک‌سازی، نرمال‌سازی، جداسازی واژه‌ها و جداسازی جمله‌ها.

هدف پروژه، نمایش عملی مراحل آماده‌سازی داده‌های متنی برای تحلیل و پردازش زبان طبیعی (NLP) است. این ابزار **مدل هوش مصنوعی آموزش‌دیده یا سامانه کامل تصحیح املا نیست**.

## امکانات فعلی

- پاک‌سازی لینک‌های اینترنتی، تگ‌های ساده HTML و فاصله‌های زائد
- حذف برخی نویسه‌های کنترلی و نامرئی، با حفظ نیم‌فاصله فارسی
- یکسان‌سازی برخی حروف عربی و فارسی مانند `ك` به `ک` و `ي` به `ی`
- نرمال‌سازی متن با کتابخانه **Hazm**، شامل اصلاح بخشی از فاصله‌ها و نیم‌فاصله‌ها
- جداسازی واژه‌ها و جمله‌ها با Hazm
- نمایش نتیجه هر مرحله در تب مستقل
- رابط کاربری راست‌به‌چپ، ورود متن، کپی/پیست و کپی خروجی

## فناوری‌های استفاده‌شده

| ابزار | کاربرد |
| --- | --- |
| Python | پیاده‌سازی منطق برنامه |
| Hazm | نرمال‌سازی و توکن‌سازی زبان فارسی |
| PySide6 | رابط گرافیکی دسکتاپ و نمایش راست‌به‌چپ |
| `re`, `html`, `unicodedata` | پردازش الگوها، موجودیت‌های HTML و نویسه‌های Unicode |

## نصب و اجرای برنامه در ویندوز

نسخه مورد استفاده در توسعه پروژه **Python 3.13** بوده است. Git و Python به‌همراه pip باید نصب باشند. دستورات زیر را در PowerShell اجرا کنید:

</div>

```powershell
git clone https://github.com/nazanin1377/Persian-NLP-Toolkit.git
cd Persian-NLP-Toolkit
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe gui.py
```

<div dir="rtl" align="right">

در این روش لازم نیست محیط مجازی را فعال کنید؛ دستورات مستقیماً از Python داخل `.venv` استفاده می‌کنند. برای اجرای نسخه ساده خط فرمان، دستور زیر نیز در دسترس است:

</div>

```powershell
.\.venv\Scripts\python.exe main.py
```

<div dir="rtl" align="right">

## خط لوله پردازش

| مرحله | ورودی و عملیات | نتیجه |
| --- | --- | --- |
| ۱. پاک‌سازی (Cleaning) | حذف موارد زائد مانند URL، تگ HTML و فاصله‌های تکراری | متن تمیزتر |
| ۲. نرمال‌سازی (Normalization) | یکسان‌سازی حروف و اصلاح بخشی از قواعد فاصله‌گذاری با Hazm | نوشتار استانداردتر فارسی |
| ۳. جداسازی واژه (Word Tokenization) | تقسیم متن نرمال‌شده به توکن | فهرست واژه‌ها و احتمالاً علائم نگارشی |
| ۴. جداسازی جمله (Sentence Tokenization) | تشخیص مرز جمله‌ها با Hazm | فهرست جمله‌ها |

## مثال ورودی و خروجی

**متن خام:**

</div>

```text
سلام   دوستان! من كتاب هاي زيادي دارم و مي خواهم برنامه نويسي ياد بگيرم. https://example.com
```

<div dir="rtl" align="right">

**پس از پاک‌سازی (نمونه):**

</div>

```text
سلام دوستان! من كتاب هاي زيادي دارم و مي خواهم برنامه نويسي ياد بگيرم.
```

<div dir="rtl" align="right">

**پس از نرمال‌سازی (نمونه تقریبی):**

</div>

```text
سلام دوستان! من کتاب‌های زیادی دارم و می‌خواهم برنامه نویسی یاد بگیرم.
```

<div dir="rtl" align="right">

خروجی دقیق، به نسخه Hazm و ویژگی‌های متن ورودی بستگی دارد. توکن‌سازی به معنی حذف خودکار علائم نگارشی نیست.

## ساختار مخزن

</div>

```text
Persian-NLP-Toolkit/
├── gui.py               # PySide6 desktop interface and NLP pipeline
├── main.py              # Basic command-line cleaning and normalization
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Files excluded from Git
└── docs/
    ├── PROCESSING.md    # Additional technical notes
    └── preview.png      # Application screenshot
```

<div dir="rtl" align="right">

## محدودیت‌ها و دامنه پروژه

- تمرکز پردازش تخصصی روی **زبان فارسی** است؛ انگلیسی در این مخزن بخش پردازش مستقل ندارد. بخش انگلیسی همین README فقط برای معرفی پروژه است.
- نرمال‌سازی همه اشتباه‌های املایی، عبارت‌های محاوره‌ای یا ترکیب‌های دارای نیم‌فاصله را اصلاح نمی‌کند.
- پاک‌سازی HTML با عبارت منظم انجام می‌شود و برای اسناد HTML پیچیده جایگزین یک HTML parser کامل نیست.
- برنامه در نسخه فعلی شامل آموزش مدل یادگیری ماشین، تحلیل احساسات یا پردازش انبوه فایل‌ها نیست.
- برای استفاده در مدل‌های Transformer، باید از Tokenizer اختصاصی همان مدل استفاده شود.

## مشارکت

گزارش خطا، پیشنهاد و درخواست تغییر از طریق بخش [Issues](https://github.com/nazanin1377/Persian-NLP-Toolkit/issues) قابل ثبت است. توسعه‌دهندگان می‌توانند تغییرات پیشنهادی را در قالب Pull Request ارسال کنند.

</div>

---

# English Documentation

## Overview

**Persian NLP Toolkit** is a Python desktop application that demonstrates a transparent preprocessing workflow for **Persian text**. It accepts raw text and displays cleaning, normalization, word tokenization, and sentence tokenization in separate output tabs.

The project is intended for learning and experimenting with NLP preprocessing. It is **not** a trained artificial-intelligence model or a comprehensive spelling corrector.

## Current features

- Clean URLs, simple HTML tags, redundant spaces, and selected control or invisible characters.
- Preserve the Persian zero-width non-joiner where applicable.
- Convert common Arabic-script variants to standard Persian characters.
- Normalize Persian text using **Hazm**.
- Tokenize words and sentences using Hazm.
- Inspect and copy outputs in separate tabs in a **PySide6** desktop interface.
- Enter, edit, copy, and paste right-to-left Persian text.

## Technology stack

| Technology | Purpose |
| --- | --- |
| Python | Application logic |
| Hazm | Persian text normalization and tokenization |
| PySide6 | Desktop user interface and RTL text display |
| Python standard library | Regular expressions, HTML entities, Unicode handling |

## Installation and usage (Windows)

The project was developed using **Python 3.13**. Install Git and Python (with pip), then run the following in PowerShell:

```powershell
git clone https://github.com/nazanin1377/Persian-NLP-Toolkit.git
cd Persian-NLP-Toolkit
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe gui.py
```

This approach invokes the virtual environment directly, so activation is optional. To use the simpler command-line prototype:

```powershell
.\.venv\Scripts\python.exe main.py
```

## Processing pipeline

| Step | Processing | Purpose |
| --- | --- | --- |
| 1 | Cleaning | Remove URLs, simple HTML tags, unnecessary whitespace, and selected control characters. |
| 2 | Normalization | Standardize Persian character variants and selected spacing conventions. |
| 3 | Word tokenization | Split normalized text into tokens, which may include punctuation. |
| 4 | Sentence tokenization | Segment normalized text into sentences. |

## Example

**Raw input**

```text
سلام   دوستان! من كتاب هاي زيادي دارم و مي خواهم برنامه نويسي ياد بگيرم. https://example.com
```

**After cleaning (illustrative)**

```text
سلام دوستان! من كتاب هاي زيادي دارم و مي خواهم برنامه نويسي ياد بگيرم.
```

**After normalization (illustrative)**

```text
سلام دوستان! من کتاب‌های زیادی دارم و می‌خواهم برنامه نویسی یاد بگیرم.
```

Exact results can vary with the installed Hazm version and input text.

## Repository structure

```text
Persian-NLP-Toolkit/
├── gui.py               # Desktop GUI and preprocessing workflow
├── main.py              # Basic CLI prototype
├── requirements.txt     # Project dependencies
├── README.md            # Bilingual documentation
├── .gitignore           # Git exclusions
└── docs/
    ├── PROCESSING.md    # Technical documentation
    └── preview.png      # Application screenshot
```

## Scope and limitations

- The NLP pipeline is designed for **Persian**, not for separate English-language preprocessing. English in this README is documentation only.
- Normalization does not correct every spelling error, colloquial expression, or half-space convention.
- Regular-expression-based HTML cleaning is not intended for complex HTML parsing.
- The application does not currently train ML models, perform sentiment analysis, or batch-process external datasets.
- Transformer-based models require their own model-specific tokenizers.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/nazanin1377/Persian-NLP-Toolkit/issues). Contributions may be proposed through Pull Requests.

---

**Repository:** https://github.com/nazanin1377/Persian-NLP-Toolkit
