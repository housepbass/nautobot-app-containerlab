# Generated by Django 3.2.25 on 2024-07-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0108_jobbutton_enabled'),
        ('containerlab', '0002_alter_topology_dynamic_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topology',
            name='dynamic_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='containerlab_topologies', to='extras.dynamicgroup'),
        ),
    ]
