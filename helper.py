from faker import Faker
fake = Faker()

def login_generator():
    generated_login = fake.user_name()
    return generated_login

def mail_generator():
    generated_mail = fake.email(domain="maeil.com")
    return generated_mail
