# Generated by Django 4.0 on 2022-01-08 12:08

from django.db import migrations, models
import django.db.models.deletion
import users.ulitis


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(default='profiles/DEFAULT.png', upload_to=users.ulitis.upload_image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userInfo', to='auth.user')),
            ],
        ),
    ]
