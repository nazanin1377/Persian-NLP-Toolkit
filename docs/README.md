# Persian Text Preprocessing

A desktop application for **Persian (Farsi) text cleaning, normalization, and tokenization**, built with Python, [Hazm](https://github.com/roshan-research/hazm), and [PySide6](https://doc.qt.io/qtforpython-6/).

این پروژه یک برنامه دسکتاپ برای پیش‌پردازش متن فارسی است. کاربران متن را در رابط گرافیکی راست‌به‌چپ وارد می‌کنند و خروجی مراحل پاک‌سازی، نرمال‌سازی، جداسازی واژه‌ها و جداسازی جملات را در تب‌های مستقل مشاهده می‌کنند.

> **Project status:** Educational/prototype application. Check the outputs before using them for production NLP or machine-learning datasets.

## Features | قابلیت‌ها

- **Cleaning:** Decodes HTML entities, strips simple HTML tags and HTTP(S)/www links, removes selected control/invisible characters, and normalizes whitespace while preserving Persian half-spaces (ZWNJ).
- **Normalization:** Converts Arabic letter variants (`ي`, `ى`, `ك`, `ة`) and uses Hazm normalization to improve Persian writing consistency and spacing.
- **Word tokenization:** Splits normalized text into tokens using Hazm's `word_tokenize`.
- **Sentence tokenization:** Splits normalized text into sentences using Hazm's `sent_tokenize`.
- **Desktop UI:** Persian right-to-left editor, separate output tabs, copy/paste, and clear buttons.

## Screenshot | تصویر برنامه

After running the application, save a screenshot to `docs/screenshot.png` and uncomment the next line:

<!-- ![Application screenshot](docs/screenshot.png) -->

## Requirements | پیش‌نیازها

- Python 3.13 (developed in a Python 3.13.3 environment)
- Windows 10/11 is the primary tested workflow; PySide6 may also work on other supported platforms
- Python packages listed in `requirements.txt`

## Installation | نصب

Open PowerShell in the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If activation is restricted by PowerShell policy, run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage | اجرا

```powershell
python gui.py
```

Or directly:

```powershell
.\.venv\Scripts\python.exe gui.py
```

1. Paste/type Persian text into the upper input field.
2. Click **پردازش متن**.
3. Review the **Cleaning**, **Normalization**, **Words**, and **Sentences** tabs.
4. Copy a selected output using **کپی خروجی**; use **پاک کردن** to reset.

### Example | مثال

**Input**

```text
سلام   دوستان، من كتاب هاي زيادي دارم.
من مي خواهم برنامه نويسي ياد بگيرم.
https://example.com
```

**Cleaning (illustrative)**

```text
سلام دوستان، من كتاب هاي زيادي دارم.
من مي خواهم برنامه نويسي ياد بگيرم.
```

**Normalization (illustrative; Hazm version-dependent)**

```text
سلام دوستان، من کتاب‌های زیادی دارم.
من می‌خواهم برنامه نویسی یاد بگیرم.
```

Token boundaries and spacing may differ by Hazm version and input; this application does **not** guarantee spelling correction.

## Processing pipeline | مراحل پردازش

```text
Raw Persian text
   |
   v
Cleaning (HTML/URLs/whitespace/control characters)
   |
   v
Normalization (Persian letters and Hazm)
   |                   |
   v                   v
Word tokenization    Sentence tokenization
```

Detailed explanations, caveats, and test examples: [docs/PROCESSING.md](docs/PROCESSING.md).

## Repository structure | ساختار مخزن

```text
Persian-Text-Preprocessing/
├── gui.py                 # PySide6 desktop application (your existing file)
├── main.py                # Optional CLI demonstration (your existing file)
├── requirements.txt       # Dependencies
├── .gitignore             # Files excluded from version control
├── README.md              # Project overview and quick start
└── docs/
    ├── PROCESSING.md     # Processing methods, limitations and test cases
    └── screenshot.png     # Optional application screenshot
```

**Important:** `gui.py` and `main.py` are not included in the documentation pack. Keep your locally working versions in the project folder.

## Known limitations | محدودیت‌ها

- Cleaning uses regular expressions, not a complete HTML parser; complex or malformed HTML might not be processed correctly.
- Automatic normalization is not the same as spell-checking or semantic correction; it may leave some compound expressions separated.
- Stopword removal, stemming, lemmatization, model inference, and document import are **not** implemented in the current GUI.
- Display and punctuation placement can vary for mixed Persian/English and bidirectional content.
- Tokenization results depend on Hazm's implementation and version.
- No external network calls are performed by the application code for processing text; installation can require internet access.

## NLP use cases | کاربردها

Educational preprocessing, exploring tokenization, preparing text for frequency analysis, and inspecting normalization prior to downstream NLP. For Transformer models such as ParsBERT, use the model's own tokenizer for model inputs.

## Development | توسعه

Contributions and issues are welcome once the repository has been published. Potential improvements: automated tests, configurable cleaning, TXT/CSV import, copy/export JSON, and a clearer distinction between display and model-ready text.

## License | مجوز

No license is included in this starter documentation pack. Before inviting others to reuse or modify the repository, choose and add a suitable `LICENSE` file.
