"""HTML formatting utilities."""
import re
import pandas as pd


def dataframe(df: pd.DataFrame, index: bool = True) -> str:
    """Return raw html table without formatting."""

    html_tbl = re.sub(
        r'<tr.*>',
        '<tr>',
        df.to_html(index=index).replace('border="1" ', ''),
    )
    return html_tbl


def hyperlink(text: str, url: str) -> str:
    """Return anchor tag for hyperlink."""
    return f'<a href="{url}">{text}</a>'
