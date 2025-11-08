import customtkinter as ctk
from tkinter import messagebox

# ================= Funções =================
def atualizar_status(texto):
    historico.insert(ctk.END, texto)
    historico.yview(ctk.END)

def executar_acao(texto, barra, tempo=2000):
    atualizar_status(texto)
    barra.start()
    janela.after(tempo, lambda: finalizar_acao(barra, "✅ Concluído!"))

def finalizar_acao(barra, texto):
    barra.stop()
    atualizar_status(texto)

def limpar_cache():
    executar_acao("🧹 Limpando cache...", barra_cache, 2500)

def otimizar_memoria():
    executar_acao("⚡ Otimizando memória...", barra_memoria, 2500)

def desfragmentar_disco():
    executar_acao("💽 Desfragmentando disco...", barra_disco, 4000)

def liberar_cpu():
    executar_acao("🖥️ Liberando CPU...", barra_cpu, 2000)

def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        janela.destroy()

# ================= Configuração Inicial =================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Otimizador Aoxy")
janela.geometry("800x500")

# ================= Frames =================
frame_menu = ctk.CTkFrame(janela, width=200, corner_radius=0)
frame_menu.pack(side="left", fill="y")

frame_main = ctk.CTkFrame(janela)
frame_main.pack(side="right", expand=True, fill="both", padx=10, pady=10)

# ================= Botões do Menu =================
btn_cache = ctk.CTkButton(frame_menu, text="🧹 Limpar Cache", command=limpar_cache)
btn_cache.pack(pady=20, padx=20, fill="x")

btn_memoria = ctk.CTkButton(frame_menu, text="⚡ Otimizar Memória", command=otimizar_memoria)
btn_memoria.pack(pady=10, padx=20, fill="x")

btn_disco = ctk.CTkButton(frame_menu, text="💽 Desfragmentar Disco", command=desfragmentar_disco)
btn_disco.pack(pady=10, padx=20, fill="x")

btn_cpu = ctk.CTkButton(frame_menu, text="🖥️ Liberar CPU", command=liberar_cpu)
btn_cpu.pack(pady=10, padx=20, fill="x")

btn_sair = ctk.CTkButton(frame_menu, text="❌ Sair", command=sair, fg_color="#a33")
btn_sair.pack(pady=30, padx=20, fill="x")

# ================= Área Principal com Abas =================
abas = ctk.CTkTabview(frame_main)
abas.pack(expand=True, fill="both", padx=10, pady=10)
abas.add("Status")
abas.add("Configurações")
abas.add("Sobre")

# ---------------- Aba Status ----------------
ctk.CTkLabel(abas.tab("Status"), text="📌 Histórico de Ações", font=("Arial", 16, "bold")).pack(anchor="w", pady=(0,10))

historico = ctk.CTkTextbox(abas.tab("Status"), width=400, height=250, corner_radius=10)
historico.pack(pady=10)

# ---------------- Barras de Progresso ----------------
barra_cache = ctk.CTkProgressBar(abas.tab("Status"))
barra_cache.pack(pady=5, fill="x")

barra_memoria = ctk.CTkProgressBar(abas.tab("Status"))
barra_memoria.pack(pady=5, fill="x")

barra_disco = ctk.CTkProgressBar(abas.tab("Status"))
barra_disco.pack(pady=5, fill="x")

barra_cpu = ctk.CTkProgressBar(abas.tab("Status"))
barra_cpu.pack(pady=5, fill="x")

# ---------------- Aba Configurações ----------------
ctk.CTkLabel(abas.tab("Configurações"), text="Configurações do Otimizador", font=("Arial", 16, "bold")).pack(pady=20)
ctk.CTkCheckBox(abas.tab("Configurações"), text="Iniciar com Windows").pack(anchor="w", padx=20, pady=5)
ctk.CTkCheckBox(abas.tab("Configurações"), text="Notificações Ativas").pack(anchor="w", padx=20, pady=5)

# ---------------- Aba Sobre ----------------
ctk.CTkLabel(abas.tab("Sobre"), text="Otimizador Aoxy v1.0", font=("Arial", 16, "bold")).pack(pady=20)
ctk.CTkLabel(abas.tab("Sobre"), text="Desenvolvido com Python e CustomTkinter.\nTodos os recursos são simulados para demonstração.",
             font=("Arial", 12)).pack(pady=10)

# ================= Inicializa =================
atualizar_status("🎉 Bem-vindo ao Otimizador Aoxy!")

janela.mainloop()
