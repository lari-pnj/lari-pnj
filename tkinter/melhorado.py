import tkinter as tk
from tkinter import ttk, messagebox
import time

# ================= Funções de Otimização =================
def atualizar_status(texto, cor="white"):
    historico_status.insert(tk.END, texto)
    historico_status.itemconfig(tk.END, fg=cor)
    historico_status.yview(tk.END)

def executar_acao(texto, cor="white", tempo=2000):
    atualizar_status(texto, cor)
    barra_progresso.start(10)
    janela.after(tempo, lambda: finalizar_acao("✅ Concluído!"))

def limpar_cache():
    executar_acao("🧹 Limpando cache...", cor="lightgreen", tempo=2500)

def otimizar_memoria():
    executar_acao("⚡ Otimizando memória...", cor="lightblue", tempo=2500)

def desfragmentar_disco():
    executar_acao("💽 Desfragmentando disco...", cor="orange", tempo=4000)

def liberar_cpu():
    executar_acao("🖥️ Liberando CPU...", cor="yellow", tempo=2000)

def finalizar_acao(texto):
    barra_progresso.stop()
    atualizar_status(texto, cor="lightgray")

def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        janela.destroy()

# ================= Criando Janela Principal =================
janela = tk.Tk()
janela.title("Otimizador Aoxy")
janela.geometry("800x500")
janela.resizable(False, False)
janela.config(bg="#1b1b2f")

# ================= Fundo com Gradiente =================
canvas_fundo = tk.Canvas(janela, width=800, height=500, highlightthickness=0)
canvas_fundo.place(x=0, y=0)
for i in range(500):
    r = int(27 + (0 * i/500))
    g = int(27 + (0 * i/500))
    b = int(47 + (60 * i/500))
    cor = f'#{r:02x}{g:02x}{b:02x}'
    canvas_fundo.create_line(0, i, 800, i, fill=cor)

# ================= Frame Menu Lateral =================
frame_menu = tk.Frame(janela, bg="#2c2c44", width=200)
frame_menu.place(x=0, y=0, height=500)

# Função para criar botões arredondados
def botao_arredondado(frame, texto, comando, y_pos, cor="#3e3e5e", cor_hover="#57577e"):
    def on_enter(e):
        botao.config(bg=cor_hover)
    def on_leave(e):
        botao.config(bg=cor)
    botao = tk.Button(frame, text=texto, command=comando, font=("Arial", 11, "bold"),
                      bg=cor, fg="white", relief="flat", bd=0, activebackground=cor_hover)
    botao.place(x=20, y=y_pos, width=160, height=40)
    botao.bind("<Enter>", on_enter)
    botao.bind("<Leave>", on_leave)

# Botões do menu
botao_arredondado(frame_menu, "🧹 Limpar Cache", limpar_cache, 50)
botao_arredondado(frame_menu, "⚡ Otimizar Memória", otimizar_memoria, 110)
botao_arredondado(frame_menu, "💽 Desfragmentar Disco", desfragmentar_disco, 170)
botao_arredondado(frame_menu, "🖥️ Liberar CPU", liberar_cpu, 230)
botao_arredondado(frame_menu, "❌ Sair", sair, 290, cor="#a33", cor_hover="#d44")

# ================= Frame Principal com Abas =================
frame_main = tk.Frame(janela, bg="#1b1b2f")
frame_main.place(x=200, y=0, width=600, height=500)

notebook = ttk.Notebook(frame_main)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ---------------- Aba Status ----------------
aba_status = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_status, text="Status")

label_status = tk.Label(aba_status, text="📌 Histórico de Ações", font=("Arial", 14, "bold"),
                        bg="#1b1b2f", fg="white", anchor="w")
label_status.pack(fill="x", padx=10, pady=(10,0))

historico_status = tk.Listbox(aba_status, bg="#2c2c44", fg="white",
                              font=("Arial", 12), height=15, selectbackground="#57577e")
historico_status.pack(fill="both", expand=True, padx=10, pady=10)

# ---------------- Aba Configurações ----------------
aba_config = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_config, text="Configurações")

tk.Label(aba_config, text="Configurações do Otimizador", font=("Arial", 14, "bold"),
         bg="#1b1b2f", fg="white").pack(pady=20)

tk.Checkbutton(aba_config, text="Iniciar com Windows", bg="#1b1b2f", fg="white",
               font=("Arial", 12), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)
tk.Checkbutton(aba_config, text="Notificações Ativas", bg="#1b1b2f", fg="white",
               font=("Arial", 12), selectcolor="#2c2c44").pack(anchor="w", padx=20, pady=5)

# ---------------- Aba Sobre ----------------
aba_sobre = tk.Frame(notebook, bg="#1b1b2f")
notebook.add(aba_sobre, text="Sobre")

tk.Label(aba_sobre, text="Otimizador Aoxy v1.0", font=("Arial", 16, "bold"),
         bg="#1b1b2f", fg="lightblue").pack(pady=20)
tk.Label(aba_sobre, text="Desenvolvido com Python e Tkinter puro.\nTodos os recursos são simulados para demonstração.",
         font=("Arial", 12), bg="#1b1b2f", fg="white").pack(pady=10)

# ================= Barra de Progresso =================
barra_progresso = ttk.Progressbar(frame_main, mode='indeterminate')
barra_progresso.place(x=210, y=460, width=580, height=20)

# ================= Rodapé =================
label_footer = tk.Label(frame_main, text="© 2025 Otimizador Aoxy", font=("Arial", 10),
                        bg="#1b1b2f", fg="gray")
label_footer.place(x=10, y=470)

# Inicializa com mensagem de boas-vindas
atualizar_status("🎉 Bem-vindo ao Otimizador Aoxy!", cor="lightgreen")

# ================= Inicia Aplicativo =================
janela.mainloop()
