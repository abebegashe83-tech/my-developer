from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    EMAIL_TO='abebegashe83@gmail.com',
)
class ContactMessageAPITests(TestCase):
    def test_valid_message_is_accepted(self):
        response = self.client.post(
            reverse('contact-message'),
            {
                'name': 'Abebe',
                'email': 'abebe@example.com',
                'message': 'I would like to discuss a project.',
            },
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['abebegashe83@gmail.com'])
        self.assertEqual(mail.outbox[0].reply_to, ['abebe@example.com'])
        self.assertIn('Email: abebe@example.com', mail.outbox[0].body)

    def test_missing_fields_are_rejected(self):
        response = self.client.post(
            reverse('contact-message'),
            {'name': 'Abebe'},
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_email_send_failure_does_not_break_submission(self):
        with self.settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'):
            response = self.client.post(
                reverse('contact-message'),
                {
                    'name': 'Abebe',
                    'email': 'abebe@example.com',
                    'message': 'I would like to discuss a project.',
                },
                content_type='application/json',
            )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'success')
        self.assertIn('saved successfully', response.json()['message'].lower())
        self.assertIn('smtp', response.json()['message'].lower())
