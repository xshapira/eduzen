# Generated by Django 3.0.6 on 2020-05-21 15:47

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields


class Migration(migrations.Migration):

    replaces = [
        ("blog", "0001_initial"),
        ("blog", "0002_dolarpeso"),
        ("blog", "0003_auto_20170701_1458"),
        ("blog", "0004_auto_20170701_1945"),
        ("blog", "0005_auto_20170806_2313"),
        ("blog", "0006_post_image"),
        ("blog", "0007_auto_20171210_1543"),
        ("blog", "0008_auto_20191112_1022"),
        ("blog", "0009_auto_20200216_1243"),
        ("blog", "0010_auto_20200516_1231"),
        ("blog", "0011_delete_custompage"),
        ("blog", "0012_auto_20200521_1246"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("word", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(null=True)),
            ],
            options={"unique_together": {("word", "slug")},},
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Titulo")),
                (
                    "pompadour",
                    models.CharField(blank=True, default="", max_length=800, verbose_name="Resumen para portada"),
                ),
                ("slug", models.SlugField(null=True, unique=True)),
                ("created_date", models.DateField(default=django.utils.timezone.now)),
                ("published_date", models.DateField(blank=True, null=True)),
                ("text", ckeditor_uploader.fields.RichTextUploadingField(verbose_name="Cuerpo de texto")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ("tags", models.ManyToManyField(related_name="posts", to="blog.Tag")),
                ("image", models.ImageField(blank=True, null=True, upload_to="post-img/%Y/%m/%d")),
                (
                    "cropping",
                    image_cropping.fields.ImageRatioField(
                        "image",
                        "260x120",
                        adapt_rotation=False,
                        allow_fullsize=False,
                        free_crop=False,
                        help_text=None,
                        hide_image_field=False,
                        size_warning=False,
                        verbose_name="cropping",
                    ),
                ),
            ],
            options={"ordering": ["-published_date"], "verbose_name": "post", "verbose_name_plural": "posts",},
        ),
    ]