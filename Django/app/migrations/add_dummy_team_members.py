from django.db import migrations

def add_dummy_team_members(apps, schema_editor):
    TeamMember = apps.get_model('app', 'TeamMember')
    # Adding dummy data with unique email addresses
    TeamMember.objects.create(first_name="John", last_name="Doe", phone="123-456-7890", email="dummy1@example.com", role="admin")
    TeamMember.objects.create(first_name="Jane", last_name="Smith", phone="123-456-7891", email="dummy2@example.com", role="regular")
    TeamMember.objects.create(first_name="Alice", last_name="Johnson", phone="123-456-7892", email="dummy3@example.com", role="regular")
    TeamMember.objects.create(first_name="Bob", last_name="Brown", phone="123-456-7893", email="dummy4@example.com", role="admin")

def remove_dummy_team_members(apps, schema_editor):
    TeamMember = apps.get_model('app', 'TeamMember')
    # Deleting dummy data by unique email addresses
    TeamMember.objects.filter(email__in=[
        "dummy1@example.com",
        "dummy2@example.com",
        "dummy3@example.com",
        "dummy4@example.com",
    ]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_dummy_team_members, remove_dummy_team_members),
    ]