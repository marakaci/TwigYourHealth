# Generated by Django 2.0.2 on 2018-05-26 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deceases', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='deceases',
            field=models.ManyToManyField(through='deceases.PatientDecease', to='deceases.Decease'),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Gender'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctorsphere',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Doctor'),
        ),
        migrations.AddField(
            model_name='doctorsphere',
            name='sphere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deceases.Sphere'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Hospital', verbose_name='hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.City'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('doctor_sphere', 'patient')},
        ),
        migrations.AlterUniqueTogether(
            name='relationships',
            unique_together={('patient', 'doctor')},
        ),
    ]
