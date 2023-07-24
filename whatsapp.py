import pywhatkit

def send_message():
    mobile = input("Введите номер телефона: ")
    message = input("Введите сообщение: ")
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

send_message()  