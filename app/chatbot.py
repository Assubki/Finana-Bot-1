from app.parsing import parse_amount, format_rupiah

# class FinancialState:
#     def __init__(self):
#         self.income = None
#         self.expense = None
#         self.cicilan = None

#     def reset(self):
#         self.__init__()

# def chatbot(user_message, history, state):
#     try:
#         user_message = user_message.lower()

#         if "income" in user_message and state.income is None:
#             return "💬 Ceritain deh berapa total pemasukan kamu? Contoh: Gaji 5 juta, freelance 2 juta"

#         if "expense" in user_message and state.expense is None:
#             return "💬 Berapa total pengeluaran kamu tiap bulan? Contoh: Makan 2 juta, transport 500 ribu"

#         if "cicilan" in user_message and state.cicilan is None:
#             return "💬 Berapa total cicilan kamu tiap bulan? Contoh: KPR 2 juta, motor 500 ribu"

#         if state.income is None:
#             income = parse_amount(user_message)
#             if income > 0:
#                 state.income = income
#                 return f"👍 Total pemasukan tercatat: {format_rupiah(income)}\n\nKetik 'expense' buat lanjut ke pengeluaran bro!"
#             else:
#                 return "⚠️ Input pemasukan kurang jelas bro. Coba ketik nominalnya ya."

#         if state.expense is None:
#             expense = parse_amount(user_message)
#             if expense > 0:
#                 state.expense = expense
#                 return f"👍 Total pengeluaran tercatat: {format_rupiah(expense)}\n\nKetik 'cicilan' kalau ada cicilan, atau ketik 'ga ada' buat lanjut!"
#             else:
#                 return "⚠️ Input pengeluaran kurang jelas bro. Coba ketik nominalnya ya."

#         if state.cicilan is None:
#             cicilan = parse_amount(user_message)
#             if cicilan > 0:
#                 state.cicilan = cicilan
#                 return f"👍 Total cicilan tercatat: {format_rupiah(cicilan)}\n\nKetik 'analisa' buat cek kondisi keuanganmu bro!"
#             else:
#                 if "ga ada" in user_message or "tidak ada" in user_message or "0" in user_message:
#                     state.cicilan = 0
#                     return "👍 Oke, kamu ga ada cicilan.\n\nKetik 'analisa' buat lanjut!"
#                 return "⚠️ Input cicilan kurang jelas bro. Ketik nominal atau bilang 'ga ada'."

#         if "analisa" in user_message:
#             income = state.income
#             expense = state.expense
#             cicilan = state.cicilan or 0

#             sisa = income - expense
#             kebutuhan = int(income * 0.5)
#             gaya_hidup = int(income * 0.3)
#             tabungan = int(income * 0.2)

#             persentase_expense = (expense / income) * 100
#             rasio_cicilan = (cicilan / income) * 100

#             result = f"""💰 Sisa uang bulanan: {format_rupiah(sisa)}

#                         📊 Rekomendasi Budget 50/30/20:
#                         - Kebutuhan Pokok (50%): {format_rupiah(kebutuhan)}
#                         - Gaya Hidup (30%): {format_rupiah(gaya_hidup)}
#                         - Tabungan/Investasi (20%): {format_rupiah(tabungan)}
#                         """

#             if persentase_expense > 80:
#                 result += f"\n🚨 Warning: Pengeluaranmu sudah {persentase_expense:.1f}% dari pemasukan! Harus lebih hemat bro!"
#             else:
#                 result += f"\n✅ Pengeluaranmu masih aman ({persentase_expense:.1f}%). Good job bro!"

#             if cicilan > 0:
#                 if rasio_cicilan > 30:
#                     result += f"\n🚨 Warning: Cicilanmu {rasio_cicilan:.1f}% dari pemasukan. Idealnya max 30%, atur ulang ya bro."
#                 else:
#                     result += f"\n✅ Cicilanmu {rasio_cicilan:.1f}% dari pemasukan. Aman bro!"

#             if sisa <= 0:
#                 result += "\n\n💬 Note: Sisa uangmu kecil atau minus, perlu atur ulang pengeluaran!. Masih miskin jangan banyak gaya!!"

#             state.reset()
#             return result

#         return "🤖 Aku ga paham bro. Coba ketik 'income', 'expense', 'cicilan', atau 'analisa' ya!"

#     except Exception as e:
#         print(f"Error in chatbot logic: {e}")
#         return "⚠️ Ada kesalahan teknis bro. Coba lagi nanti ya."





def chatbot(user_message, history, state):
    try:
        user_message = user_message.lower()

        # Cek urutan: income ➝ expense ➝ cicilan ➝ analisa
        if state.income is None:
            if "expense" in user_message or "cicilan" in user_message or "analisa" in user_message:
                return "⚠️ Masukin dulu pemasukan kamu bro. Ketik 'income' lalu kasih nominalnya."

            if "income" in user_message:
                return "💬 Ceritain deh berapa total pemasukan kamu? Contoh: Gaji 5 juta, freelance 2 juta"

            income = parse_amount(user_message)
            if income > 0:
                state.income = income
                return f"👍 Total pemasukan tercatat: {format_rupiah(income)}\n\nSekarang ketik 'expense' buat lanjut ke pengeluaran bro!"
            else:
                return "⚠️ Input pemasukan kurang jelas bro. Coba ketik nominalnya ya."

        if state.expense is None:
            if "cicilan" in user_message or "analisa" in user_message:
                return "⚠️ Masukin dulu pengeluaran kamu bro. Ketik 'expense' dulu baru lanjut."

            if "expense" in user_message:
                return "💬 Berapa total pengeluaran kamu tiap bulan? Contoh: Makan 2 juta, transport 500 ribu"

            expense = parse_amount(user_message)
            if expense > 0:
                state.expense = expense
                return f"👍 Total pengeluaran tercatat: {format_rupiah(expense)}\n\nSekarang ketik 'cicilan' kalau ada cicilan, atau 'ga ada'."
            else:
                return "⚠️ Input pengeluaran kurang jelas bro. Coba ketik nominalnya ya."

        if state.cicilan is None:
            if "analisa" in user_message:
                return "⚠️ Masukin dulu cicilan kamu (atau bilang 'ga ada') sebelum analisa bro."

            if "cicilan" in user_message:
                return "💬 Berapa total cicilan kamu tiap bulan? Contoh: KPR 2 juta, motor 500 ribu"

            cicilan = parse_amount(user_message)
            if cicilan > 0:
                state.cicilan = cicilan
                return f"👍 Total cicilan tercatat: {format_rupiah(cicilan)}\n\nKetik 'analisa' buat cek kondisi keuanganmu bro!"
            else:
                if "ga ada" in user_message or "tidak ada" in user_message or "0" in user_message:
                    state.cicilan = 0
                    return "👍 Oke, kamu ga ada cicilan.\n\nKetik 'analisa' buat lanjut!"
                return "⚠️ Input cicilan kurang jelas bro. Ketik nominal atau bilang 'ga ada'."

        if "analisa" in user_message:
            income = state.income
            expense = state.expense
            cicilan = state.cicilan or 0

            sisa = income - expense
            kebutuhan = int(income * 0.5)
            gaya_hidup = int(income * 0.3)
            tabungan = int(income * 0.2)

            persentase_expense = (expense / income) * 100
            rasio_cicilan = (cicilan / income) * 100

            result = f"""💰 Sisa uang bulanan: {format_rupiah(sisa)}

📊 Rekomendasi Budget 50/30/20:
- Kebutuhan Pokok (50%): {format_rupiah(kebutuhan)}
- Gaya Hidup (30%): {format_rupiah(gaya_hidup)}
- Tabungan/Investasi (20%): {format_rupiah(tabungan)}"""

            if persentase_expense > 80:
                result += f"\n🚨 Warning: Pengeluaranmu udah {persentase_expense:.1f}% dari pemasukan! Perlu atur ulang."
            else:
                result += f"\n✅ Pengeluaranmu masih aman ({persentase_expense:.1f}%)"

            if cicilan > 0:
                if rasio_cicilan > 30:
                    result += f"\n🚨 Cicilanmu {rasio_cicilan:.1f}% dari pemasukan. Idealnya di bawah 30% ya bro!"
                else:
                    result += f"\n✅ Cicilan kamu aman ({rasio_cicilan:.1f}%)"

            if sisa <= 0:
                result += "\n💬 Note: Sisa uangmu kecil atau minus. Perlu atur ulang gaya hidup dan cicilan."

            state.reset()
            return result

        return "🤖 Aku ga paham bro. Coba ketik 'income', 'expense', 'cicilan', atau 'analisa' ya!"

    except Exception as e:
        print(f"Error in chatbot logic: {e}")
        return "⚠️ Ada error teknis bro. Coba lagi nanti."
