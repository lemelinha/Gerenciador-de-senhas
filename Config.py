from tkinter import ttk
from tkinter import IntVar, StringVar
from Commands import *

class Config:
	def __init__(self, master):
		self.master = master
		self.Commands = Commands(self)


	def setFrames(self):
		self.frameTamanhoSenha = ttk.Frame(self.master)
		self.frameSenhaGerada = ttk.Frame(self.master)
		self.frameBotoes = ttk.Frame(self.frameSenhaGerada)

		self.Senha = StringVar()
		Mostrar_senha = ttk.Label(self.frameSenhaGerada, textvariable=self.Senha)
		Mostrar_senha.pack(side='top', expand=True)

		self.frameTamanhoSenha.pack(side='left', fill='both')
		self.frameSenhaGerada.pack(side='right', fill='both', expand=True)
		self.frameBotoes.pack(side='bottom', fill='both')


	def setInputs(self):
		ttk.Label(self.frameTamanhoSenha, text='Definir tamanho da senha').pack(side='top', expand=True)
		self.TamanhoSenha = IntVar()

		self.entry_TamanhoSenha = ttk.LabeledScale(self.frameTamanhoSenha, from_=12, to=30, variable=self.TamanhoSenha)
		self.entry_TamanhoSenha.pack(expand=True, side='top', pady=5)

		ttk.Label(self.frameSenhaGerada, text='Nome da senha').pack(side='top', expand=True)
		self.Nome_senha = StringVar()
		entry_Nome_senha = ttk.Entry(self.frameSenhaGerada, textvariable=self.Nome_senha)
		entry_Nome_senha.pack(side='top', expand=True)

		botao_gerar_senha = ttk.Button(self.frameTamanhoSenha, text='Gerar senha', command=self.Commands.Gerar)
		botao_gerar_senha.pack(side='bottom', expand=True)

		botao_copiar_senha = ttk.Button(self.frameBotoes, text='Copiar senha', command=self.Commands.Copiar)
		botao_salvar_senha = ttk.Button(self.frameBotoes, text='Salvar senha', command=self.Commands.Salvar)

		botao_copiar_senha.pack(side='top', padx=3, pady=3)
		botao_salvar_senha.pack(side='top', padx=3, pady=3)


		botao_ver_senha = ttk.Button(self.frameBotoes, text='Ver senha', command=self.Commands.Ver_senha)
		self.ver_senha = StringVar()
		self.combobox_senhas = ttk.Combobox(self.frameBotoes, textvariable=self.ver_senha, state='readonly', width=20)
		self.Commands.Update_combobox()

		self.combobox_senhas.pack(side='right', padx=3, pady=3)
		botao_ver_senha.pack(side='right', padx=3, pady=3)

