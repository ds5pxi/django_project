
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QnA',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
