# Generated by Django 3.1.7 on 2021-04-05 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Seller', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='product_seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productseller'),
        ),
    ]
