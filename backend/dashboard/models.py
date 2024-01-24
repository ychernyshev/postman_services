from django.db import models


# Create your models here.
class LetterItemModel(models.Model):
    track_number = models.CharField(max_length=13)
    address = models.OneToOneField('RecipientModel', db_index=True, on_delete=models.PROTECT)
    is_court = models.BooleanField(default=False)
    is_court_subpoena = models.BooleanField(default=False)
    is_police_subpoena = models.BooleanField(default=False)
    date_of_receipt = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.date_of_receipt} | '
                f'{self.track_number} | '
                f'{self.is_court} | '
                f'{self.is_court_subpoena} | '
                f'{self.is_police_subpoena}')

    class Meta:
        verbose_name = 'letter'
        verbose_name_plural = 'Letters'


# class SenderModel(models.Model):
#     sender_name = models.CharField(max_length=45)
#
#     def __str__(self):
#         return self.sender_name
#
#     class Meta:
#         verbose_name = 'sender'
#         verbose_name_plural = 'Senders'


class RecipientModel(models.Model):
    # recipient_name = models.CharField(max_length=45)

    STREET = [
        ('STR', 'Стрийська'),
        ('MKL', 'Мікльоша'),
        ('SOK', 'Сокільницька'),
    ]

    street = models.CharField(choices=STREET, max_length=3, default='STR')

    BUILD = [
        ('', ''),
        ('3', '3'), ('5', '5'), ('7', '7'), ('9', '9'),
        ('11', '11'), ('13', '13'), ('15', '15'),
        ('17', '17'), ('20', '20'), ('25', '25'),
        ('27', '27'), ('73', '73'), ('75', '75'),
        ('77', '77'), ('81', '81'), ('85', '85'),
        ('87', '87'), ('89', '89'), ('91', '91'),
        ('93', '93'), ('99', '99'), ('101', '101'),
        ('103', '103'), ('105', '105'), ('107', '107'),
        ('111', '111'), ('115', '115'), ('117', '117'),
        ('123', '123'), ('127', '127'), ('133', '133'),
    ]
    build = models.CharField(choices=BUILD, max_length=3, default='', blank=True)

    BUILD_LETTER = [
        ('', ''),
        ('A', 'А'),
        ('B', 'Б'),
        ('V', 'В'),
        ('G1', 'Г'),
        ('D', 'Д'),
        ('E1', 'Е'),
        ('E2', 'Є'),
        ('G2', 'Ж'),
    ]
    build_letter = models.CharField(choices=BUILD_LETTER, max_length=2, default='', blank=True, null=True)
    apartment = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return f'{self.street} {self.build}{self.build_letter}/{self.apartment}'

    class Meta:
        verbose_name = 'recipient'
        verbose_name_plural = 'Recipients'


# class LetterCardModel(models.Model):
#     letter = models.OneToOneField(LetterItemModel, db_index=True, on_delete=models.SET_NULL, blank=True, null=True)
#     sender = models.ManyToManyField(SenderModel, db_index=True)
#     recipient = models.ManyToManyField(RecipientModel, db_index=True)
