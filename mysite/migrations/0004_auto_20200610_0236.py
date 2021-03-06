# Generated by Django 3.0.7 on 2020-06-09 21:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_present'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('mac', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='present',
        ),
    ]
