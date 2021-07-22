from django.forms import forms
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    """
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Digite o seu nome'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder':'Digite o seu email'}))
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea(attrs={'placeholder':'Digite o assunto'})
    """
    if form.is_valid():
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')
        email_submit = EmailMessage(
            "Mensagem do Blog do django",
            f"De {nome} <{email}> Escreveu: \n\n{mensagem}",
            "nao-responder@inbox.mailto.io",
            ['alissonchaves2015@gmail.com'],
            reply_to=[email]


        )
        try:
            email_submit.send()
        
        except:
            send = False
        send = True
    context = {
        'form': form,
        'success': send
    }
    return render(request, 'contact/contact.html', context)