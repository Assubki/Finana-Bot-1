import re
def parse_amount(text):
    try:
        text = text.lower().replace(",", ".")
        total = 0
        words = text.split()
        i = 0
        while i < len(words):
            word = words[i]
            if re.match(r'^\d+\.?\d*$', word):
                num = float(word)
                multiplier = 1
                if i + 1 < len(words):
                    next_word = words[i + 1]
                    if next_word in ["juta", "jt"]:
                        multiplier = 1_000_000
                        i += 1
                    elif next_word in ["ribu", "rb", "r"]:
                        multiplier = 1_000
                        i += 1
                    else:
                        if num < 10:
                            multiplier = 1_000_000
                total += int(num * multiplier)
            elif re.match(r'^\d+\.?\d*(jt|juta)$', word):
                num = float(re.findall(r'\d+\.?\d*', word)[0])
                total += int(num * 1_000_000)
            elif re.match(r'^\d+\.?\d*(rb|ribu|r)$', word):
                num = float(re.findall(r'\d+\.?\d*', word)[0])
                total += int(num * 1_000)
            i += 1
        return total
    except Exception as e:
        print(f"Error in parse_amount: {e}")
        return 0

def detect_data(text):
    try:
        text = text.lower()
        data = {"income": 0, "expense": 0, "cicilan": 0}
        parts = re.split(r',|dan|&', text)
        for part in parts:
            if any(word in part for word in ["gaji", "pemasukan", "penghasilan", "income", "masuk"]):
                data["income"] += parse_amount(part)
            elif any(word in part for word in ["pengeluaran", "spending", "biaya", "keluar", "habis", "expense"]):
                data["expense"] += parse_amount(part)
            elif any(word in part for word in ["cicilan", "hutang", "kredit"]):
                data["cicilan"] += parse_amount(part)
        return data
    except Exception as e:
        print(f"Error in detect_data: {e}")
        return {"income": 0, "expense": 0, "cicilan": 0}

def format_rupiah(amount):
    try:
        return f"Rp {amount:,.0f}".replace(",", ".")
    except Exception as e:
        print(f"Error in format_rupiah: {e}")
        return "Rp 0"

# import re

# # Format angka ke rupiah

# def format_rupiah(amount):
#     try:
#         return f"Rp {amount:,.0f}".replace(",", ".")
#     except:
#         return "Rp 0"

# # Parsing jumlah uang + operasi matematika

# def parse_amount(text):
#     try:
#         text = text.lower().replace(",", ".").replace(" ", "")
#         total = 0.0

#         # Ambil angka dan satuan
#         matches = re.findall(r'(\d+(?:\.\d+)?)(juta|jt|ribu|rb|r)?', text)
#         expression = []

#         for num_str, unit in matches:
#             num = float(num_str)
#             if unit in ['juta', 'jt']:
#                 num *= 1_000_000
#             elif unit in ['ribu', 'rb', 'r']:
#                 num *= 1_000
#             expression.append(str(int(num)))

#         # Tangkap operator + -
#         ops = re.findall(r'[+-]', text)
#         full_expr = []
#         for i, num in enumerate(expression):
#             full_expr.append(num)
#             if i < len(ops):
#                 full_expr.append(ops[i])

#         total = eval(''.join(full_expr)) if full_expr else 0
#         return int(total)

#     except Exception as e:
#         print(f"Error in parse_amount: {e}")
#         return 0
