# Generated by Django 4.0.3 on 2022-05-01 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manageCake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfOrder', models.DateTimeField()),
                ('Price', models.FloatField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageorder.order')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageCake.product')),
            ],
        ),
    ]
