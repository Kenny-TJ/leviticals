from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='devotional',
            name='life_nugget',
            field=models.TextField(help_text='The main devotional body'),
        ),
        migrations.AlterField(
            model_name='devotional',
            name='prayer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='devotional',
            name='scripture_text',
            field=models.TextField(help_text='The full scripture passage'),
        ),
        migrations.AlterField(
            model_name='missionstory',
            name='body',
            field=models.TextField(),
        ),
    ]
