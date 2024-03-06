import django

from datetime import timedelta, datetime
from django.utils.timezone import localdate
from django.template.defaultfilters import slugify

from django.db import models


# Create your models here.


class MailItemModel(models.Model):
    track_number = models.CharField(max_length=13)
    slug = models.SlugField(max_length=13, unique=True, blank=True)
    address = models.ForeignKey('RecipientModel', related_name='address_mails', db_index=True, on_delete=models.PROTECT)
    is_court = models.BooleanField(default=False)
    is_court_subpoena = models.BooleanField(default=False)
    is_police_fine = models.BooleanField(default=False)
    re_entry = models.BooleanField(default=False)
    letter_image_id = models.CharField(max_length=40, blank=True)
    date_of_receipt = models.DateTimeField(auto_now_add=True)
    the_expired_date = models.DateField(auto_now=False, blank=True, null=True)
    expired_date = models.DateTimeField(default=django.utils.timezone.now(), blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_court = self.is_court
        self._is_court_subpoena = self.is_court_subpoena

    def save(self, *args, **kwargs):
        self.slug = slugify(self.track_number)

        if not self._is_court and self.is_court_subpoena:
            # self.expired_date = date_of_receipt + timedelta(days=4)
            self.expired_date = django.utils.timezone.now() + timedelta(days=4)
        else:
            self.expired_date = django.utils.timezone.now() + timedelta(days=30)
        super().save(*args, **kwargs)

    def expired_time(self):
        ex_time = self.expired_date.date() - datetime.today().date()
        return ex_time.days

    # def save(self, *args, **kwargs):
    #     if self.is_court_subpoena and self.expired_date is None:
    #         self.expired_date = datetime.date.  today() + timedelta(days=30)
    #     elif not self.is_court_subpoena and self.expired_date is None:
    #         self.expired_date = datetime.date.today() + timedelta(days=3)
    #     super().save(*args, **kwargs)

    # def return_date_time(self):
    #     now = datetime.date.today()
        # if not self.is_court_subpoena:
        # return now + timedelta(days=30)
        # elif self.is_court_subpoena:
        #     return now + timedelta(days=3)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.track_number)
    #     super(LetterItemModel, self).save(*args, **kwargs)

    def __str__(self):
        return (f'{self.date_of_receipt} | '
                f'{self.track_number} | '
                f'{self.is_court} | '
                f'{self.is_court_subpoena} | '
                f'{self.is_police_fine}')

    class Meta:
        ordering = ['-date_of_receipt']
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
        ('', ''), ('tpo', 'До відділення'),
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
        ('260', '260'), ('262', '262'), ('264', '264'),
        ('266', '266'), ('268', '268'), ('270', '270'),
        ('272', '272'), ('274', '274'), ('276', '276'),
        ('278', '278'), ('280', '280'), ('282', '282'),
        ('284', '284'), ('286', '286'), ('288', '288'),
        ('290', '290'), ('292', '292'), ('294', '294'),
        ('296', '296'), ('298', '298'), ('300', '300'),
        ('302', '302'), ('304', '304'), ('306', '306'),
        ('308', '308'), ('310', '310'), ('312', '312'),
        ('314', '314'), ('316', '316'), ('318', '318'),
        ('320', '320'), ('322', '322'), ('324', '324'),
        ('326', '326'), ('328', '328'), ('330', '330'),
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
    company_name = models.CharField(max_length=100, blank=True)
    # mail_item = models.CharField(MailItemModel, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.street} {self.build}{self.build_letter}/{self.apartment}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'recipient'
        verbose_name_plural = 'Recipients'


# class LetterCardModel(models.Model):
#     letter = models.OneToOneField(LetterItemModel, db_index=True, on_delete=models.SET_NULL, blank=True, null=True)
#     sender = models.ManyToManyField(SenderModel, db_index=True)
#     recipient = models.ManyToManyField(RecipientModel, db_index=True)
