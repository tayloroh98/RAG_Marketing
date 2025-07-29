from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("라르트 일일매출 및 광고비.xlsx")
print(result.text_content)