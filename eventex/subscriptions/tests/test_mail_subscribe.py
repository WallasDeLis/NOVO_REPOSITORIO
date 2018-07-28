from django.core import mail
from django.test import TestCase


class SubscribePostvalid(TestCase):
    def setUp(self):
        data = dict(name='De Lis', cpf='12345678901',
                    email='delis.wallas@armazemparaiba.com.br', phone='86-99908-6341')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'delis.wallas@armazemparaiba.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'De Lis',
            '12345678901',
            'delis.wallas@armazemparaiba.com.br',
            '86-99908-6341'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
