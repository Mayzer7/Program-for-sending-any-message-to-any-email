import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_html_email(recipients_emails: list, subject: str, html_content: str):
    login = 'your_yandex_email'
    password = 'your_app_password'  # Используйте пароль приложения

    # Создание сообщения
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = login
    msg['To'] = ', '.join(recipients_emails)

    # Добавляем HTML-контент
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))

    try:
        # Для SSL используйте порт 465
        with smtplib.SMTP_SSL('smtp.yandex.ru', 465, timeout=10) as s:
            s.login(login, password)
            s.sendmail(msg['From'], recipients_emails, msg.as_string())
            print("Email sent successfully!")
    except Exception as ex:
        print(f"An error occurred: {ex}")

def main():
    # Чтение содержимого файла welcome_email.html
    try:
        with open('welcome_email.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print("Файл welcome_email.html не найден.")
        return
    except Exception as ex:
        print(f"Ошибка при чтении файла: {ex}")
        return

    # Отправка письма
    send_html_email(
        recipients_emails=['send_to_whom?'],
        subject='Добро пожаловать в STORE (topic)',
        html_content=html_content
    )

if __name__ == '__main__':
    main()
