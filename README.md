# 📬 Gmail Inbox Cleaner

Um script em Python que automatiza a exclusão de e-mails **não lidos** com mais de 30 dias na sua conta do Gmail. Este projeto foi criado para ajudar a manter sua caixa de entrada organizada e eficiente, economizando tempo e reduzindo distrações. 🚀

---

## 🛠️ Funcionalidades

- Conecta-se automaticamente ao servidor IMAP do Gmail.
- Identifica e-mails não lidos com mais de **30 dias**.
- Exclui os e-mails de forma segura e eficiente.
- Utiliza variáveis de ambiente para proteger suas credenciais.

---

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

1. Python 3.7 ou superior instalado.
2. As bibliotecas Python necessárias instaladas (listadas abaixo).
3. Acesso ao seu Gmail configurado para permitir conexões IMAP.

### Configuração IMAP no Gmail
Certifique-se de que o acesso IMAP está habilitado no Gmail:
1. Acesse as **Configurações** do Gmail.
2. Vá até a aba **Encaminhamento e POP/IMAP**.
3. Ative a opção **Acesso IMAP**.

Além disso, você precisará gerar uma **Senha de Aplicativo** para substituir sua senha principal no script, garantindo mais segurança.

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/gmail-inbox-cleaner.git
   cd gmail-inbox-cleaner

---

## 🚀 Como usar
 1. Abra o terminal no diretório do projeto.
 2. Execute o script:
    ```bash
    python main.py
 3. O script conectará à sua conta, identificará e-mails não lidos com mais de 30 dias e os excluirá.

---

## 🛡️ Segurança 

Este projeto utiliza a biblioteca dotenv para gerenciar credenciais de forma segura. Nunca compartilhe suas informações confidenciais ou o arquivo .env publicamente.
  
---

## 📝 Licença

Este projeto é licenciado sob a MIT License.
  
---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 😊
  
---

## 📧 Contato

Se você tiver dúvidas ou sugestões, entre em contato:

Email: jhefersonwarley@gmail.com <br>
LinkedIn: [Jheferson Warley](https://www.linkedin.com/in/jheferson-warley/)
