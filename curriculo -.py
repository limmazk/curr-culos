import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import re


def gerar_curriculo():
    
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    experiencia = text_experiencia.get("1.0", tk.END).strip()
    educacao = text_educacao.get("1.0", tk.END).strip()
    habilidades = text_habilidades.get("1.0", tk.END).strip()

    
    if not nome or not email or not telefone:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha nome, email e telefone.")
        return

    
    if not email.endswith("@gmail.com"):
        messagebox.showwarning("Email Inválido", "O email deve ser do tipo @gmail.com.")
        return

    
    if not telefone.isdigit():
        messagebox.showwarning("Telefone Inválido", "O telefone deve conter apenas números.")
        return

    # criar pdf
    pdf_nome = f"{nome}_curriculo.pdf"
    c = canvas.Canvas(pdf_nome, pagesize=A4)
    largura, altura = A4

    #titulo (estilo)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1 * inch, altura - 1 * inch, nome)

    # subtitulo falando do contato
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.darkgray)
    c.drawString(1 * inch, altura - 1.5 * inch, f"Email: {email} | Telefone: {telefone}")

    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.black)
    c.drawString(1 * inch, altura - 2.5 * inch, "Experiência Profissional")
    c.setFont("Helvetica", 12)
    text = c.beginText(1 * inch, altura - 3 * inch)
    text.setLeading(14)
    text.textLines(experiencia)
    c.drawText(text)

    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, altura - 4.5 * inch, "Educação")
    c.setFont("Helvetica", 12)
    text = c.beginText(1 * inch, altura - 5 * inch)
    text.setLeading(14)
    text.textLines(educacao)
    c.drawText(text)

   
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, altura - 6.5 * inch, "Habilidades")
    c.setFont("Helvetica", 12)
    text = c.beginText(1 * inch, altura - 7 * inch)
    text.setLeading(14)
    text.textLines(habilidades)
    c.drawText(text)

    #salvar pdf
    c.showPage()
    c.save()
    
    messagebox.showinfo("Sucesso", f"Currículo gerado com sucesso: {pdf_nome}")


app = tk.Tk()
app.title("Gerador de Currículos")
app.geometry("800x800")
app.configure(background='light gray')


label_titulo = tk.Label(app, text="Gerador de Currículo", font=("Helvetica", 16,))
label_titulo.pack(pady=10)


label_nome = tk.Label(app, text="Nome Completo:")
label_nome.pack()
entry_nome = tk.Entry(app, width=40)
entry_nome.pack(pady=5)


label_email = tk.Label(app, text="Email:")
label_email.pack()
entry_email = tk.Entry(app, width=40)
entry_email.pack(pady=5)


label_telefone = tk.Label(app, text="Telefone:")
label_telefone.pack()
entry_telefone = tk.Entry(app, width=40)
entry_telefone.pack(pady=5)


label_experiencia = tk.Label(app, text="Experiência Profissional:")
label_experiencia.pack()
text_experiencia = tk.Text(app, height=5, width=55)
text_experiencia.pack(pady=5)


label_educacao = tk.Label(app, text="Educação:")
label_educacao.pack()
text_educacao = tk.Text(app, height=5, width=55)
text_educacao.pack(pady=5)


label_habilidades = tk.Label(app, text="Habilidades:")
label_habilidades.pack()
text_habilidades = tk.Text(app, height=5, width=55)
text_habilidades.pack(pady=5)


btn_gerar = tk.Button(app, text="Gerar Currículo", command=gerar_curriculo)
btn_gerar.pack(pady=20)


app.mainloop()
