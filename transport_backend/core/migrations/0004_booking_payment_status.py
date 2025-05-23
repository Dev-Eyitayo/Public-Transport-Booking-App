# Generated by Django 5.1.7 on 2025-04-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_booking_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("successful", "Successful"),
                    ("failed", "Failed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
