# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class DCategory(models.Model):
    category_id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    category_name = models.CharField(max_length=20)
    book_counts = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    category_pid = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_category'


class DOrderiterm(models.Model):
    shop_id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    shop_num = models.DecimalField(max_digits=20, decimal_places=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'd_orderiterm'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TAddress(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    name = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    addr_mobile = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=255, blank=True, null=True)
    book_author = models.CharField(max_length=255, blank=True, null=True)
    book_publish = models.CharField(max_length=255, blank=True, null=True)
    publish_time = models.CharField(max_length=255, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=255, blank=True, null=True)
    word_count = models.CharField(max_length=64, blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=64, blank=True, null=True)
    book_category = models.IntegerField(blank=True, null=True)
    book_wrapper = models.CharField(max_length=255, blank=True, null=True)
    book_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    book_dprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    editor_recommendation = models.CharField(max_length=2000, blank=True, null=True)
    content_introduction = models.CharField(max_length=2000, blank=True, null=True)
    author_introduction = models.CharField(max_length=2000, blank=True, null=True)
    menu = models.CharField(max_length=2000, blank=True, null=True)
    media_review = models.CharField(max_length=2000, blank=True, null=True)
    digest_image_path = models.CharField(max_length=2000, blank=True, null=True)
    product_image_path = models.CharField(max_length=2000, blank=True, null=True)
    series_name = models.CharField(max_length=128, blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.CharField(max_length=64, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    customer_socre = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    book_status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    sales = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    book_size = models.CharField(max_length=255, blank=True, null=True)
    book_pager = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TOrder(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TShoppingCart(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    book_id = models.CharField(max_length=20, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_shopping_cart'


class TUser(models.Model):
    user_id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
