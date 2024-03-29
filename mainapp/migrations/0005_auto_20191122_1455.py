# Generated by Django 2.2.7 on 2019-11-22 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20191122_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='china_item',
            old_name='cityGubun',
            new_name='china_cityGubun',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='dtYearMonth',
            new_name='china_dtYearMonth',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='id',
            new_name='china_id',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='marketType',
            new_name='china_marketType',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='sido',
            new_name='china_sido',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='sigungu',
            new_name='china_sigungu',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='useCost',
            new_name='china_useCost',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='useCount',
            new_name='china_useCount',
        ),
        migrations.RenameField(
            model_name='china_item',
            old_name='userCount',
            new_name='china_userCount',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='ageGroup',
            new_name='korea_ageGroup',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='cityGubun',
            new_name='korea_cityGubun',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='dtYearMonth',
            new_name='korea_dtYearMonth',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='gender',
            new_name='korea_gender',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='id',
            new_name='korea_id',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='marketType',
            new_name='korea_marketType',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='sido',
            new_name='korea_sido',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='sigungu',
            new_name='korea_sigungu',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='useCost',
            new_name='korea_useCost',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='useCount',
            new_name='korea_useCount',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='userCount',
            new_name='korea_userCount',
        ),
        migrations.RenameField(
            model_name='korea_item',
            old_name='userType',
            new_name='korea_userType',
        ),
    ]
