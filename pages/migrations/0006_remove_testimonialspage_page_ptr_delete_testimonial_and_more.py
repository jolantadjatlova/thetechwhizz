from django.db import migrations, connection


def drop_testimonials_cascade(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS pages_testimonial CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS pages_testimonialspage CASCADE;")


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_privacypolicypage'),
    ]

    operations = [
        migrations.RunPython(drop_testimonials_cascade, migrations.RunPython.noop),
    ]