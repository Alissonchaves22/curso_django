from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Digite o seu nome'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder':'Digite o seu email'}))
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea(attrs={'placeholder':'Digite o assunto'}))