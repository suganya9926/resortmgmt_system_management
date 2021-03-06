# Generated by Django 4.0.4 on 2022-05-17 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0003_remove_payments_amount_remove_services_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlebedroom',
            name='details',
        ),
        migrations.AddField(
            model_name='eclecticfood',
            name='amount',
            field=models.IntegerField(default=6000),
        ),
        migrations.AddField(
            model_name='payments',
            name='amount',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='roomservices',
            name='amount',
            field=models.IntegerField(default=4000),
        ),
        migrations.AddField(
            model_name='services',
            name='amount',
            field=models.IntegerField(default=6000),
        ),
        migrations.AddField(
            model_name='services',
            name='carparking',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.carparking'),
        ),
        migrations.AddField(
            model_name='services',
            name='doublebedroom',
            field=models.ForeignKey(default=8000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.doublebedroom'),
        ),
        migrations.AddField(
            model_name='services',
            name='eclecticfood',
            field=models.ForeignKey(default=6000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.eclecticfood'),
        ),
        migrations.AddField(
            model_name='services',
            name='roomservices',
            field=models.ForeignKey(default=4000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.roomservices'),
        ),
        migrations.AddField(
            model_name='services',
            name='singlebedroom',
            field=models.ForeignKey(default=6000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.singlebedroom'),
        ),
        migrations.AddField(
            model_name='services',
            name='vipbedroom',
            field=models.ForeignKey(default=10000, on_delete=django.db.models.deletion.CASCADE, to='resortapp.vipbedroom'),
        ),
        migrations.AddField(
            model_name='singlebedroom',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='singlebedroom',
            name='idproof',
            field=models.CharField(choices=[('Aadhaar Card', 'Aadhaar Card'), ('Passport', 'Passport'), ('Driving Licence', 'Driving Licence'), ('Voter ID', 'Voter ID'), ('Pan Card', 'Pan Card')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='singlebedroom',
            name='mobilenumber',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='singlebedroom',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carparking',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.singlebedroom'),
        ),
        migrations.AlterField(
            model_name='doublebedroom',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.singlebedroom'),
        ),
        migrations.AlterField(
            model_name='roomservices',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.singlebedroom'),
        ),
        migrations.AlterField(
            model_name='vipbedroom',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resortapp.singlebedroom'),
        ),
    ]
