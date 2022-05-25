# Generated by Django 3.2.12 on 2022-05-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220513_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.person'),
        ),
    ]
