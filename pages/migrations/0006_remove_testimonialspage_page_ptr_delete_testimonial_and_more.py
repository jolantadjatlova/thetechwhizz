from django.db import migrations


def drop_testimonials(apps, schema_editor):
    db = schema_editor.connection.vendor
    with schema_editor.connection.cursor() as cursor:
        if db == 'postgresql':
            cursor.execute("DROP TABLE IF EXISTS pages_testimonial CASCADE;")
            cursor.execute("DROP TABLE IF EXISTS pages_testimonialspage CASCADE;")
        else:
            try:
                cursor.execute("DROP TABLE IF EXISTS pages_testimonial;")
            except Exception:
                pass
            try:
                cursor.execute("DROP TABLE IF EXISTS pages_testimonialspage;")
            except Exception:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_privacypolicypage'),
    ]

    operations = [
        migrations.RunPython(drop_testimonials, migrations.RunPython.noop),
    ]