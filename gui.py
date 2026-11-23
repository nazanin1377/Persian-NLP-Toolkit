
import sys
import re
import html
import unicodedata

from hazm import Normalizer, word_tokenize, sent_tokenize

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QPlainTextEdit,
    QTabWidget,
    QMessageBox,
    QFrame
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QTextOption


# Persian NLP Engine
normalizer = Normalizer()


def clean_text(text):
    """Clean unwanted elements from text."""

    # Decode HTML entities
    text = html.unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]*>", " ", text)

    # Remove URLs
    text = re.sub(
        r"https?://[^\s]+|www\.[^\s]+",
        " ",
        text,
        flags=re.IGNORECASE
    )

    # Remove control characters, keep newlines/tabs
    text = "".join(
        ch for ch in text
        if unicodedata.category(ch) != "Cc"
        or ch in "\n\t"
    )

    # Remove invisible formatting characters
    # Preserve Persian ZWNJ
    text = "".join(
        ch for ch in text
        if unicodedata.category(ch) != "Cf"
        or ch == "\u200c"
    )

    # Normalize whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def normalize_text(text):
    """Normalize Persian text."""

    replacements = {
        "ي": "ی",
        "ى": "ی",
        "ك": "ک",
        "ة": "ه"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Hazm normalization
    text = normalizer.normalize(text)

    # Fix half-space spacing
    text = re.sub(r" *\u200c *", "\u200c", text)

    # Remove spaces before punctuation
    text = re.sub(r" +([،؛؟!.,:])", r"\1", text)

    return text.strip()


def create_rtl_editor(read_only=False):
    """Create a text editor with RTL support."""

    editor = QPlainTextEdit()

    editor.setFont(QFont("Tahoma", 12))

    editor.setLayoutDirection(
        Qt.LayoutDirection.RightToLeft
    )

    # Force paragraph direction to RTL
    options = editor.document().defaultTextOption()

    options.setTextDirection(
        Qt.LayoutDirection.RightToLeft
    )

    options.setAlignment(
        Qt.AlignmentFlag.AlignRight
    )

    options.setWrapMode(
        QTextOption.WrapMode.WordWrap
    )

    editor.document().setDefaultTextOption(options)

    editor.setReadOnly(read_only)

    # Qt provides Copy/Paste and context menu
    editor.setContextMenuPolicy(
        Qt.ContextMenuPolicy.DefaultContextMenu
    )

    return editor


class PersianNLPApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Persian Text Preprocessing - NLP"
        )

        self.resize(1000, 760)
        self.setMinimumSize(750, 550)

        self.output_boxes = []

        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):

        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel(
            "پردازش و نرمال‌سازی متن فارسی"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setObjectName("title")

        layout.addWidget(title)

        subtitle = QLabel(
            "Persian Text Cleaning & Normalization"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(subtitle)

        # Input label
        input_label = QLabel("متن فارسی را وارد کنید:")

        input_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(input_label)

        # Input editor
        self.input_box = create_rtl_editor()

        self.input_box.setPlaceholderText(
            "متن فارسی خود را اینجا بنویسید یا Paste کنید..."
        )

        layout.addWidget(self.input_box, 2)

        # Buttons
        button_layout = QHBoxLayout()

        self.process_button = QPushButton(
            "پردازش متن"
        )

        self.process_button.clicked.connect(
            self.process_text
        )

        self.clear_button = QPushButton(
            "پاک کردن"
        )

        self.clear_button.clicked.connect(
            self.clear_all
        )

        self.copy_button = QPushButton(
            "کپی متن ورودی"
        )

        self.copy_button.clicked.connect(
            lambda: self.copy_text(self.input_box)
        )

        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.process_button)

        layout.addLayout(button_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(
            QFrame.Shape.HLine
        )

        layout.addWidget(separator)

        result_label = QLabel("نتایج پردازش:")

        result_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(result_label)

        # Tabs
        self.tabs = QTabWidget()

        tab_names = [
            "Cleaning",
            "Normalization",
            "Words",
            "Sentences"
        ]

        for name in tab_names:

            tab = QWidget()
            tab_layout = QVBoxLayout(tab)

            output = create_rtl_editor(
                read_only=True
            )

            tab_layout.addWidget(output)

            copy_output = QPushButton(
                "کپی خروجی"
            )

            copy_output.clicked.connect(
                lambda checked=False, w=output:
                self.copy_text(w)
            )

            tab_layout.addWidget(copy_output)

            self.tabs.addTab(tab, name)
            self.output_boxes.append(output)

        layout.addWidget(self.tabs, 3)

        # Status bar
        self.status_label = QLabel(
            "آماده دریافت متن"
        )

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(self.status_label)

    def process_text(self):

        raw = self.input_box.toPlainText()

        if not raw.strip():
            QMessageBox.warning(
                self,
                "هشدار",
                "لطفاً یک متن فارسی وارد کنید."
            )
            return

        try:
            cleaned = clean_text(raw)

            normalized = normalize_text(cleaned)

            words = word_tokenize(normalized)

            sentences = sent_tokenize(normalized)

            results = [
                cleaned,
                normalized,
                "\n".join(words),
                "\n\n".join(sentences)
            ]

            for editor, value in zip(
                self.output_boxes, results
            ):
                editor.setPlainText(value)

            # Display normalized output
            self.tabs.setCurrentIndex(1)

            self.status_label.setText(
                f"پردازش موفق | "
                f"{len(words)} توکن | "
                f"{len(sentences)} جمله"
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "خطا",
                str(error)
            )

    def copy_text(self, editor):

        cursor = editor.textCursor()

        if cursor.hasSelection():
            value = cursor.selectedText()
            value = value.replace("\u2029", "\n")
        else:
            value = editor.toPlainText()

        QApplication.clipboard().setText(value)

        self.status_label.setText(
            "متن در Clipboard کپی شد."
        )

    def clear_all(self):

        self.input_box.clear()

        for editor in self.output_boxes:
            editor.clear()

        self.status_label.setText(
            "آماده دریافت متن"
        )

    def apply_styles(self):

        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
                color: #202938;
                font-family: Tahoma;
                font-size: 12px;
            }

            QLabel#title {
                font-size: 21px;
                font-weight: bold;
                color: #183153;
            }

            QPlainTextEdit {
                background-color: white;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                padding: 12px;
                selection-background-color: #bcd7ff;
            }

            QPlainTextEdit:focus {
                border: 2px solid #2563eb;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton:pressed {
                background-color: #1e40af;
            }

            QTabWidget::pane {
                border: 1px solid #cbd5e1;
                background: white;
                border-radius: 6px;
            }

            QTabBar::tab {
                background: #e2e8f0;
                padding: 10px 18px;
                margin-right: 3px;
            }

            QTabBar::tab:selected {
                background: #2563eb;
                color: white;
            }
        """)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = PersianNLPApp()
    window.show()

    sys.exit(app.exec())
