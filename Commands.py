from pyperclip import copy
from tkinter.messagebox import showerror, showinfo
from tkinter import Toplevel, StringVar, Entry
from tkinter.ttk import Frame, Label, Button
from string import printable
from random import choice

caracteres = list(printable)
caracteres = caracteres[:94]
caracteres.pop(68)
caracteres.pop(63)

class Commands:
	def __init__(self, config):
		self.Config = config
		self.senhas_salvas = dict()
		self.janela_ver_senha = False

	def Gerar(self):
		senha = ''
		for c in range(0, self.Config.TamanhoSenha.get()):
			senha = ''.join([senha, choice(caracteres)])
		self.Config.Senha.set(senha)

	def Copiar(self):
		copy(self.Config.Senha.get())
		self.Config.combobox_senhas.set(self.senhas_salvas['Selecione uma senha'])

	def Salvar(self):
		if self.Config.Nome_senha.get().strip() == '':
			showerror('Erro', 'Preenche um nome para a senha')
			return
		elif self.Config.Senha.get() == '':
			showerror('Erro', 'Nenhuma senha gerada')
			return
		else:
			try:
				with open('senhas.txt', 'a') as arquivo:
					arquivo.writelines(f'{self.Config.Nome_senha.get()}\n{self.Config.Senha.get()}\n')

			except FileExistsError:
				with open('senhas.txt', 'x'):
					print()

			else:
				showinfo('Senha salva', 'Sua senha foi salva!')
				self.Update_combobox()
				return

	def Ver_senha(self):
		if self.Config.ver_senha.get() != '' and self.Config.ver_senha.get() in self.senhas_salvas:
			if not self.janela_ver_senha or not self.janela_ver_senha.winfo_exists():
				self.janela_ver_senha = Toplevel(self.Config.master)
				self.janela_ver_senha.geometry('280x90')
				self.janela_ver_senha.title(self.Config.ver_senha.get())

				self.frame_nome = Frame(self.janela_ver_senha)
				self.frame_senha = Frame(self.janela_ver_senha)
				self.frame_botoes = Frame(self.janela_ver_senha)

				Label(self.frame_nome, text='Nome:').pack(side='left', padx=3, pady=3)
				Label(self.frame_senha, text='Senha:').pack(side='left', padx=3, pady=3)

				self.frame_nome.pack(side='top', fill='x')
				self.frame_senha.pack(side='top', fill='x')
				self.frame_botoes.pack(side='bottom', fill='x')

				self.config_janela_ver_senha()

				self.janela_ver_senha.mainloop()
		else:
			showerror('Erro', 'Selecione uma senha válida')

	def config_janela_ver_senha(self):
		self.mostrar_nome = Label(self.frame_nome, textvariable=self.Config.ver_senha)
		self.mostrar_senha = Label(self.frame_senha, text=self.senhas_salvas[self.Config.ver_senha.get()])

		self.mostrar_nome.pack(side='left', padx=3, pady=3)
		self.mostrar_senha.pack(side='left', padx=3, pady=3)

		self.botao_editar = Button(self.frame_botoes, text='Editar', command=self.editar)
		self.botao_copiar = Button(self.frame_botoes, text='Copiar senha', command=lambda: copy(self.senhas_salvas[self.Config.ver_senha.get()]))
		self.botao_editar.pack(side='left', padx=3, pady=3)
		self.botao_copiar.pack(side='left', padx=3, pady=3)

	def editar(self):
		self.mostrar_nome.destroy()
		self.mostrar_senha.destroy()
		self.botao_editar.destroy()
		self.botao_copiar.destroy()

		self.novo_nome = StringVar(value=self.Config.ver_senha.get())
		self.entry_nome = Entry(self.frame_nome, textvariable=self.novo_nome, width=50)
		self.nova_senha = StringVar(value=self.senhas_salvas[self.Config.ver_senha.get()])
		self.entry_senha = Entry(self.frame_senha, textvariable=self.nova_senha, width=50)

		self.entry_nome.pack(side='left', padx=3, pady=3, fill='x')
		self.entry_senha.pack(side='left', padx=3, pady=3, fill='x')

		self.botao_salvar = Button(self.frame_botoes, text='Salvar alterações', command=self.Salvar_alteracao)
		self.botao_excluir = Button(self.frame_botoes, text='Excluir senha', command=self.excluir_senha)
		self.botao_cancelar = Button(self.frame_botoes, text='Cancelar', command=self.cancelar)

		self.botao_salvar.pack(side='left', padx=3, pady=3)
		self.botao_excluir.pack(side='left', padx=3, pady=3)
		self.botao_cancelar.pack(side='right', padx=3, pady=3)

	def Salvar_alteracao(self):
		if self.novo_nome.get() != self.Config.ver_senha.get() or self.nova_senha.get() != self.senhas_salvas[self.Config.ver_senha.get()]:
			with open('senhas.txt', 'r') as arquivo:
				senhas = arquivo.readlines()
			senhas[senhas.index(f'{self.Config.ver_senha.get()}\n')] = f'{self.novo_nome.get()}\n'
			senhas[senhas.index(f'{self.senhas_salvas[self.Config.ver_senha.get()]}\n')] = f'{self.nova_senha.get()}\n'
			with open('senhas.txt', 'w') as arquivo:
				arquivo.writelines(senhas)
			self.senhas_salvas.pop(self.Config.ver_senha.get())
			self.Config.ver_senha.set(value=self.novo_nome.get())
			self.Update_combobox()
			showinfo('Senha', 'Alterações feitas com sucesso')
		self.cancelar()

	def excluir_senha(self):
		with open('senhas.txt', 'r') as arquivo:
			senhas = arquivo.readlines()
		senhas.remove(f'{self.Config.ver_senha.get()}\n')
		senhas.remove(f'{self.senhas_salvas[self.Config.ver_senha.get()]}\n')
		with open('senhas.txt', 'w') as arquivo:
			arquivo.writelines(senhas)
		self.senhas_salvas.pop(self.Config.ver_senha.get())
		self.Update_combobox()
		showinfo('Senha', 'Senha deletada com sucesso')
		self.janela_ver_senha.destroy()

	def cancelar(self):
		self.entry_nome.destroy()
		self.entry_senha.destroy()
		self.botao_salvar.destroy()
		self.botao_excluir.destroy()
		self.botao_cancelar.destroy()

		self.config_janela_ver_senha()

	def Update_combobox(self):
		with open('senhas.txt', 'r') as arquivo:
			senhas = arquivo.readlines()
		for c in range(len(senhas)):
			if c % 2 == 0:
				self.senhas_salvas[senhas[c][:len(senhas[c])-1]] = senhas[c+1][:len(senhas[c+1])-1]
		self.Config.combobox_senhas['values'] = [n for n in self.senhas_salvas.keys()]
