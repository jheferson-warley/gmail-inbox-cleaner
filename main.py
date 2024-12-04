
import imaplib
import email
import os
import datetime
from dotenv import load_dotenv


load_dotenv()

# Configurações da conta do Gmail 
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASS")


SERVER = 'imap.gmail.com'

DIAS_EXPIRACAO = 30

def delete_unread_emails(days):
   
    try:
        with imaplib.IMAP4_SSL(SERVER) as mail:
            mail.login(EMAIL_ADDRESS, PASSWORD)
            mail.select('inbox')

            data_limite = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%d-%b-%Y")
            _, data = mail.search(None, f'(BEFORE "{data_limite}" UNSEEN)')
            mail_ids = data[0]
            id_list = mail_ids.split()

            for num in id_list:
                _, data = mail.fetch(num, '(RFC822)')
                email_message = email.message_from_bytes(data[0][1])

                print(f"Excluindo email: {email_message['Subject']}")

                mail.store(num, '+FLAGS', '\\Deleted')

            mail.expunge()
            print("Emails excluídos com sucesso.")

    except Exception as e:
        print(f"Erro ao excluir emails: {e}")


if __name__ == "__main__":
    delete_unread_emails(DIAS_EXPIRACAO)