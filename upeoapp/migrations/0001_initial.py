# Generated by Django 4.1.1 on 2022-10-23 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_answers6', to='upeoapp.answers')),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('confirm_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('admission_number', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_answers3', to='upeoapp.answers')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_questions2', to='upeoapp.questions')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_student1', to='upeoapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_student4', to='upeoapp.student'),
        ),
        migrations.AddField(
            model_name='questions',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_questions5', to='upeoapp.topic'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=6, null=True)),
                ('message', models.CharField(max_length=15, null=True)),
                ('origin', models.CharField(max_length=6, null=True)),
                ('title', models.CharField(max_length=15, null=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upeoapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.IntegerField()),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_answers', to='upeoapp.answers')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_questions', to='upeoapp.questions')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_student', to='upeoapp.student')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_Topic', to='upeoapp.topic')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_questions8', to='upeoapp.questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_student9', to='upeoapp.student'),
        ),
        migrations.AddField(
            model_name='answers',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upeo_Topic7', to='upeoapp.topic'),
        ),
    ]
