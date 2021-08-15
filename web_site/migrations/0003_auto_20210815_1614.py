# Generated by Django 3.2.6 on 2021-08-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0002_auto_20210814_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='codegist',
            name='difficulty',
            field=models.CharField(choices=[('DIFFICULT', 'Difficult'), ('INTERMEDIATE', 'Intermediate'), ('EASY', 'Easy')], default='EASY', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='codegist',
            name='topic',
            field=models.CharField(default='topic', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='codegist',
            name='coding_platform',
            field=models.CharField(choices=[('HACKERRANK', 'HackerRank'), ('CODECHEF', 'CodeChef'), ('LEETCODE', 'Leetcode'), ('NONE', 'None')], max_length=30),
        ),
        migrations.AlterField(
            model_name='codegist',
            name='language',
            field=models.CharField(choices=[('C', 'C'), ('PYTHON', 'Python'), ('JAVA', 'Java'), ('JAVASCRIPT', 'Javascript'), ('CPP', 'CPP'), ('OTHER', 'other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='codegist',
            name='problem_url',
            field=models.URLField(default='', null=True),
        ),
    ]