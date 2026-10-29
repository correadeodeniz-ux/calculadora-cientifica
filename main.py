# main.py
import customtkinter as ctk
from src import calculos

# Configuração inicial do tema do CustomTkinter
ctk.set_appearance_mode("System")  # Segue o tema do sistema (Claro/Escuro)
ctk.set_default_color_theme("blue")

class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Científica")
        self.geometry("360x520")
        self.resizable(False, False)

        # Variável para armazenar a expressão atual
        self.expressao = ""

        # Visor (Área de exibição dos números e resultados)[cite: 1]
        self.visor = ctk.CTkEntry(self, font=("Arial", 28), justify="right", height=60)
        self.visor.pack(padx=20, pady=20, fill="x")

        # Frame para organizar os botões
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(padx=20, pady=10, fill="both", expand=True)

        # Definição dos botões da calculadora
        botoes = [
            ("C", 0, 0), ("⌫", 0, 1), ("%", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("**", 4, 2), ("√", 4, 3),
            ("=", 5, 0)
        ]

        # Criando e posicionando cada botão na grade (grid)
        for (texto, linha, coluna) in botoes:
            if texto == "=":
                btn = ctk.CTkButton(self.frame_botoes, text=texto, font=("Arial", 20), fg_color="green", hover_color="darkgreen", command=self.calcular)
                btn.grid(row=linha, column=coluna, columnspan=4, padx=5, pady=5, sticky="nsew")
            else:
                btn = ctk.CTkButton(self.frame_botoes, text=texto, font=("Arial", 18), command=lambda t=texto: self.clique_botao(t))
                btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew", ipadx=5, ipady=10)

        # Configurar peso das linhas/colunas do grid para redimensionamento uniforme
        for i in range(6):
            self.frame_botoes.rowconfigure(i, weight=1)
        for j in range(4):
            self.frame_botoes.columnconfigure(j, weight=1)

    def clique_botao(self, valor):
        if valor == "C":
            self.expressao = ""
        elif valor == "⌫":
            self.expressao = self.expressao[:-1]
        else:
            self.expressao += str(valor)
        
        self.atualizar_visor()

    def atualizar_visor(self):
        self.visor.delete(0, "end")
        self.visor.insert(0, self.expressao)

    def calcular(self):
        try:
            # Tratamento especial para raiz quadrada (√)
            if "√" in self.expressao:
                num_str = self.expressao.replace("√", "")
                resultado = calculos.raiz_quadrada(float(num_str))
            else:
                # Usa eval de forma segura para computar as expressões básicas
                resultado = eval(self.expressao)
            
            self.expressao = str(resultado)
            self.atualizar_visor()
        except ZeroDivisionError:
            self.expressao = ""
            self.visor.delete(0, "end")
            self.visor.insert(0, "Erro: Divisão por zero!")
        except Exception:
            self.expressao = ""
            self.visor.delete(0, "end")
            self.visor.insert(0, "Erro de expressão!")

if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()