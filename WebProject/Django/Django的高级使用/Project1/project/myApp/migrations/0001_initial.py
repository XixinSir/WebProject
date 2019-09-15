# Generated by Django 2.1.2 on 2019-08-04 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('gname', models.AutoField(primary_key=True, serialize=False)),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
            ],
            options={
                'db_table': 'grades',
                'ordering': ['gname'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sage', models.IntegerField(db_column='age')),
                ('scontend', models.CharField(max_length=20)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Grades')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['id'],
            },
        ),
    ]
