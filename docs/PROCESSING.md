# Persian Text Preprocessing — Technical Documentation

## 1. Scope

The current implementation is a local desktop application for **deterministic preprocessing**, not an AI model. It does not train a model, perform sentiment analysis, or correct spelling automatically.

## 2. Data flow

1. The user types/pastes text into a PySide6 `QPlainTextEdit`.
2. `clean_text(raw)` produces cleaned text.
3. `normalize_text(cleaned)` produces normalized text.
4. Hazm tokenizes normalized text into words and sentences.
5. The application displays four independent outputs.

The original input is not overwritten when the **Process** button is clicked.

## 3. Cleaning — what is changed?

| Operation | Example | Notes |
| --- | --- | --- |
| Decode HTML entities | `&amp;` → `&` | Python `html.unescape` |
| Remove simple HTML tags | `<p>سلام</p>` → `سلام` | Regex-based; not a full parser |
| Remove URL tokens | `https://example.com` → removed | A URL adjacent to punctuation can remove that punctuation depending on input |
| Remove controls | Selected Unicode category `Cc` | Newlines/tabs retained temporarily |
| Remove invisible formatting | Most Unicode category `Cf` | ZWNJ (`U+200C`) preserved |
| Normalize extra spaces | `سلام   دنیا` → `سلام دنیا` | Line breaks are retained |

**Important:** The cleaning stage is purposefully conservative: it preserves ordinary punctuation, numbers, and content-bearing words.

## 4. Normalization — what is changed?

- Arabic `ي` and `ى` → Persian `ی`.
- Arabic `ك` → Persian `ک`.
- Arabic `ة` → `ه` (a simplified rule; may not be linguistically ideal in every text).
- Hazm `Normalizer` improves consistency, especially in common Persian spacing patterns.
- Remove spaces adjacent to an existing ZWNJ.
- Remove unnecessary spaces before selected punctuation.

Hazm is rule-based and version-dependent; it is **not a general-purpose grammar or spelling checker**. Some expressions, such as `برنامه نویسی`, may remain spaced.

## 5. Tokenization

- **Words:** `hazm.word_tokenize(normalized_text)`; punctuation tokens may appear.
- **Sentences:** `hazm.sent_tokenize(normalized_text)`; segmentation is heuristic.

No automatic stopword removal or lemmatization is performed by the GUI, because these would change the NLP meaning for some tasks (e.g. negation).

## 6. Encoding and right-to-left display

Python strings are Unicode. The PySide6 editors use Qt paragraph direction `RightToLeft` and right alignment. Underlying text is stored in logical order; visual punctuation placement is a UI concern. Mixed Latin/Persian segments may still need further UX testing.

## 7. Manual acceptance tests

| # | Input | Expected check |
| --- | --- | --- |
| 1 | `سلام   دنیا` | Extra spaces removed in Cleaning |
| 2 | `كتاب` | `کتاب` after Normalization |
| 3 | `علي` | `علی` after Normalization |
| 4 | `<p>سلام</p>` | Tags removed in Cleaning |
| 5 | `سلام https://example.com` | URL removed in Cleaning |
| 6 | `من آمدم. تو رفتی.` | Two sentences in Sentences (subject to Hazm behavior) |
| 7 | `می‌روم` | ZWNJ preserved |
| 8 | `این خوب نیست.` | Negation preserved; no stopword removal |
| 9 | `سلام.` | Dot should be displayed at the sentence end in the RTL editor |
| 10 | Persian text copied from browser | Clipboard copy/paste and output copying work |

## 8. Design trade-offs and roadmap

- Keep preprocessing functions separate from UI code to simplify automated testing.
- Add configurable cleaning switches instead of permanently deleting URLs, emoji, or numbers for every NLP task.
- Consider an HTML parser for HTML-heavy sources.
- Version-pin tested dependencies before a formal release.
- Add unit tests and sample datasets without publishing confidential text.
- For Transformer models, feed normalized text into the **model-specific** tokenizer; Hazm word tokens are a separate diagnostic output.
