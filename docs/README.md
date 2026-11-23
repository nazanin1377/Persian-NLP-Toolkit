# Technical Documentation | مستندات فنی

**Repository:** [nazanin1377/Persian-NLP-Toolkit](https://github.com/nazanin1377/Persian-NLP-Toolkit)

This directory contains supporting technical documentation for the Persian text preprocessing desktop application. For a project overview and installation instructions, see the [main README](../README.md).

**Quick links:** [مستندات فارسی](#مستندات-فارسی) · [English documentation](#english-documentation)

---

## مستندات فارسی

### درباره پروژه

این پروژه یک برنامه دسکتاپ برای **پیش‌پردازش متن فارسی** با Python، کتابخانه Hazm و رابط گرافیکی PySide6 است. هدف آن نمایش و مقایسه خروجی مراحل پاک‌سازی، نرمال‌سازی، جداسازی واژه‌ها و جداسازی جمله‌هاست. این برنامه مدل یادگیری ماشین نیست و غلط‌یاب املایی یا تحلیل‌گر احساسات محسوب نمی‌شود.

### روند پردازش

```text
متن خام فارسی
    ↓
پاک‌سازی (Cleaning)
    ↓
نرمال‌سازی (Normalization)
    ├──→ جداسازی واژه‌ها (Word Tokenization)
    └──→ جداسازی جمله‌ها (Sentence Tokenization)
```

| مرحله | کاری که انجام می‌دهد |
| --- | --- |
| پاک‌سازی | حذف لینک‌ها و تگ‌های ساده HTML، اصلاح فاصله‌های اضافی و حذف بعضی نویسه‌های کنترلی؛ حفظ علائم نگارشی و نیم‌فاصله |
| نرمال‌سازی | یکسان‌سازی برخی حروف عربی و فارسی و اصلاح برخی الگوهای فاصله‌گذاری با Hazm |
| جداسازی واژه‌ها | تقسیم متن نرمال‌شده به توکن‌های واژه و علائم با Hazm |
| جداسازی جمله‌ها | تفکیک متن به جمله‌ها با Hazm |

### نمونه کوتاه

**ورودی:**

```text
سلام   دوستان! من كتاب هاي زيادي دارم.
```

**پس از پاک‌سازی:**

```text
سلام دوستان! من كتاب هاي زيادي دارم.
```

**پس از نرمال‌سازی (نمونه تقریبی):**

```text
سلام دوستان! من کتاب‌های زیادی دارم.
```

نتیجه دقیق ممکن است بر اساس نسخه Hazm و متن ورودی تفاوت داشته باشد. این ابزار حذف کلمات توقف، ریشه‌یابی و تصحیح املایی را در رابط گرافیکی فعلی انجام نمی‌دهد.

### فایل‌های مرتبط

- [راهنمای فنی پردازش و سناریوهای آزمون](PROCESSING.md)
- [راهنمای اصلی نصب و اجرا](../README.md)
- [کد رابط گرافیکی](../gui.py)
- [تصویر اجرای برنامه](preview.png)

### محدودیت‌ها

پاک‌سازی HTML با عبارت منظم انجام می‌شود و جایگزین یک HTML Parser کامل نیست. لینک‌ها حذف می‌شوند و ممکن است برخی نشانه‌های چسبیده به لینک نیز حذف شوند. عملکرد قواعد نرمال‌سازی به نسخه Hazm وابسته است. برای استفاده در مجموعه‌داده‌های حساس یا پروژه‌های عملیاتی، خروجی‌ها باید ارزیابی شوند.

---

## English Documentation

### Overview

**Persian-NLP-Toolkit** is a Python desktop application for Persian text preprocessing. It uses **Hazm** for normalization and tokenization and **PySide6** for a right-to-left graphical interface. It is a preprocessing tool, **not** a trained AI model, spell checker, or sentiment classifier.

### Processing pipeline

```text
Raw Persian text
       ↓
Cleaning
       ↓
Normalization
       ├──→ Word tokenization
       └──→ Sentence tokenization
```

| Stage | Behavior |
| --- | --- |
| Cleaning | Decodes HTML entities, removes simple HTML tags and URLs, handles selected control/format characters, and reduces extra whitespace while preserving ZWNJ |
| Normalization | Standardizes selected Arabic/Persian letter variants and applies Hazm normalization |
| Word tokenization | Uses `hazm.word_tokenize()` on normalized text |
| Sentence tokenization | Uses `hazm.sent_tokenize()` on normalized text |

### Example

**Input:**

```text
سلام   دوستان! من كتاب هاي زيادي دارم.
```

**Cleaned:**

```text
سلام دوستان! من كتاب هاي زيادي دارم.
```

**Normalized (illustrative):**

```text
سلام دوستان! من کتاب‌های زیادی دارم.
```

Output may vary with the Hazm version and input. The current GUI does not perform stopword removal, lemmatization, or automatic spelling correction.

### Documentation and source files

- [Detailed processing specification and manual tests](PROCESSING.md)
- [Main README and installation instructions](../README.md)
- [GUI implementation](../gui.py)
- [Application screenshot](preview.png)

### Known limitations

HTML cleaning uses regular expressions rather than a complete HTML parser. URL removal may also consume adjoining punctuation. Normalization is rule-based and should be evaluated for the intended NLP dataset. RTL display behavior can vary for mixed Persian/Latin text.

---

For issues, suggestions, or contributions, visit the repository's [Issues page](https://github.com/nazanin1377/Persian-NLP-Toolkit/issues).
