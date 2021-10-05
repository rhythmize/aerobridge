# Generated by Django 3.2.7 on 2021-10-05 13:17

from django.db import migrations, models
import django.db.models.deletion
import registry.models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0062_auto_20211005_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='role_type',
            field=models.IntegerField(choices=[(0, 'Other'), (1, 'Responsible')], default=0, help_text='A contact may or may not be legally responsible officer within a company, specify if the contact is responsisble (legally) for operations in the company'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='acronym',
            field=models.CharField(default='NA', help_text='If you use a acronym for this manufacturer, you can assign it here', max_length=10),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='address',
            field=models.ForeignKey(blank=True, help_text='Assign a address to this manufacturers', null=True, on_delete=django.db.models.deletion.CASCADE, to='registry.address'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='common_name',
            field=models.CharField(default='NA', help_text='Common name for the manufacturer e.g. Skydio', max_length=140),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(default='NA', help_text='The three-letter ISO 3166-1 country code where the manufacturer is located', max_length=3),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='full_name',
            field=models.CharField(default='NA', help_text='Full legal name of the manufacturing entity', max_length=140),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='address',
            field=models.ForeignKey(help_text='Assign a address to this Pilot', on_delete=django.db.models.deletion.CASCADE, to='registry.address'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='is_active',
            field=models.BooleanField(default=0, help_text='Is this pilot active? If he is not working for the company or has moved on'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='operator',
            field=models.ForeignKey(help_text='Assign this pilot to a operator', on_delete=django.db.models.deletion.CASCADE, to='registry.operator'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='person',
            field=models.OneToOneField(help_text='Assign this pilot to a person object', on_delete=django.db.models.deletion.CASCADE, to='registry.person'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='photo',
            field=models.URLField(blank=True, null=True, validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='photo_small',
            field=models.URLField(blank=True, null=True, validators=[registry.models.validate_url]),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='tests',
            field=models.ManyToManyField(help_text='Specify the tests if any the pilot has taken', through='registry.TestValidity', to='registry.Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='taken_at',
            field=models.IntegerField(choices=[(0, 'Online Test'), (1, 'In Authorized Test Center'), (2, 'Other')], default=0, help_text='Specify where this test was taken'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.IntegerField(choices=[(0, 'Remote pilot online theoretical competency'), (1, 'Certificate of remote pilot competency'), (2, 'Other')], default=0, help_text='Specify the type of test'),
        ),
    ]
