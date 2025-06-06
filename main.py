# import gradio as gr
# from chatbot import chatbot
# from state import FinancialState

# # --- Inisialisasi state ---
# state = FinancialState()

# # --- Launch Gradio ---
# with gr.Blocks(theme=gr.themes.Default()) as demo:
#     gr.Markdown("# 💬 Chatbot Finansial - Bro Edition 🚀")
#     chatbot_ui = gr.ChatInterface(fn=lambda user_msg, history: chatbot(user_msg, history, state))

# demo.launch()



# import gradio as gr
# from app.chatbot import chatbot
# from app.state import FinancialState

# # Inisialisasi state
# state = FinancialState()

# demo = gr.ChatInterface(
#     fn=lambda user_msg, history: chatbot(user_msg, history, state),
#     chatbot=gr.Chatbot(label="💬 Bot Finansial"),
#     textbox=gr.Textbox(
#         placeholder="Contoh: Gaji 5 juta, atau ketik 'income', 'expense', 'analisa'...",
#         label="Input kamu 👇"
#     ),
#     submit_btn="🚀 Kirim",
#     # clear_btn dihapus karena tidak didukung
#     title="📊 Chatbot Finansial - New Edition",
#     description="Bantu kamu kelola keuangan dengan santai, tapi pasti bikin melek literasi 😎",
#     theme=gr.themes.Default(),
#     type="messages"  # Gunakan format OpenAI-style: role+content
# )

# if __name__ == "__main__":
#     demo.launch()



import gradio as gr
from app.chatbot import chatbot
from app.state import FinancialState

# --- Inisialisasi state ---
state = FinancialState()

# --- Fungsi handler utama ---
def handle_chat(user_msg, history):
    response = chatbot(user_msg, history, state)
    return history + [{"role": "user", "content": user_msg}, {"role": "assistant", "content": response}]

# --- UI ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 💬 Bot Finansial\nKelola keuangan lo bro, dengan gaya santai")

    chatbot_ui = gr.Chatbot(
        label="💰 Chat Area",
        height=400,
        show_copy_button=True,
        type="messages"
    )

    with gr.Row():
        user_input = gr.Textbox(placeholder="ketik contoh :'expense' 'income', cicilan ", show_label=False, scale=5)
        send_btn = gr.Button(" Kirim", scale=1)

    with gr.Row():
        clear_btn = gr.Button(" Reset Chat")
        history_dropdown = gr.Dropdown(label="Riwayat Chat (demo only)", choices=[], interactive=False, visible=False)

    def submit_msg(message, history):
        updated_history = handle_chat(message, history)
        return updated_history, ""  # chatbot di-update, textbox dikosongin


    send_btn.click(fn=submit_msg, inputs=[user_input, chatbot_ui], outputs=[chatbot_ui, user_input])
    user_input.submit(fn=submit_msg, inputs=[user_input, chatbot_ui], outputs=[chatbot_ui, user_input])
    clear_btn.click(lambda: [], outputs=chatbot_ui)

# --- Launch app ---
if __name__ == "__main__":
    demo.launch(show_api=False, inbrowser=True)
