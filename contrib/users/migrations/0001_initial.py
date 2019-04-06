# Generated by Django 2.1.7 on 2019-04-06 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('cla_name', models.CharField(help_text='班级名称', max_length=128)),
                ('cla_code', models.IntegerField(help_text='班级代码', null=True)),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('edu_begin_time', models.DateField(help_text='开始时间')),
                ('edu_finish_time', models.DateField(help_text='结束时间')),
                ('edu_school_name', models.CharField(help_text='学校名称', max_length=128, null=True)),
                ('edu_study_major', models.CharField(help_text='专业方向', max_length=128, null=True)),
                ('edu_study_field', models.CharField(help_text='研究领域', max_length=128, null=True)),
            ],
            options={
                'verbose_name': '学历',
                'verbose_name_plural': '学历',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('stu_number', models.IntegerField(default='20190101', help_text='学号', unique=True)),
                ('stu_avatar', models.ImageField(help_text='学生照片', null=True, upload_to='')),
                ('stu_gender', models.CharField(choices=[('G1', '男'), ('G2', '女')], help_text='性别', max_length=64, null=True)),
                ('stu_card_type', models.CharField(default='身份证', help_text='身份证件类型', max_length=128)),
                ('stu_cardID', models.CharField(default='12345', help_text='身份证号', max_length=128, null=True, unique=True)),
                ('stu_candidate_number', models.CharField(help_text='考生号', max_length=128, null=True)),
                ('stu_birth_day', models.DateField(help_text='出生日期')),
                ('stu_nation', models.CharField(default='汉', help_text='民族', max_length=64)),
                ('stu_source', models.CharField(help_text='生源地', max_length=128, null=True)),
                ('stu_is_village', models.BooleanField(default=False, help_text='是否农村学生')),
                ('stu_political', models.CharField(choices=[('P1', '党员'), ('P2', '团员'), ('P3', '群众'), ('P4', '民主党派')], help_text='政治面貌', max_length=64, null=True)),
                ('stu_type', models.CharField(choices=[('S1', '硕士'), ('S2', '博士'), ('S3', '本硕连读'), ('S4', '硕博连读'), ('S5', '直博')], default='S1', help_text='学生类型', max_length=128)),
                ('stu_learn_type', models.CharField(choices=[('S1', '全日制'), ('S2', '非全日制')], default='S1', help_text='学习形式', max_length=64)),
                ('stu_learn_status', models.CharField(choices=[('D1', '博士'), ('D2', '硕士'), ('D3', '本科')], default='D2', help_text='学习阶段', max_length=64)),
                ('stu_grade', models.CharField(default='1', help_text='年级', max_length=64)),
                ('stu_system', models.IntegerField(default=3, help_text='学制')),
                ('stu_entrance_time', models.CharField(default='2019-09', help_text='入学日期', max_length=32)),
                ('stu_graduation_time', models.CharField(default='2021-07', help_text='毕业日期', max_length=32)),
                ('stu_cultivating_mode', models.CharField(choices=[('C1', '专硕'), ('C2', '学硕')], default='C1', help_text='培养方式', max_length=128)),
                ('stu_enrollment_category', models.CharField(choices=[('E1', '定向'), ('E2', '非定向')], default='E1', help_text='录取类别', max_length=64)),
                ('stu_nationality', models.CharField(default='中国', help_text='国籍', max_length=128)),
                ('stu_special_program', models.CharField(choices=[('S1', '无'), ('S2', '少数民族高层次骨干计划'), ('S3', '强军计划'), ('S4', '对口支援西部地区高校定向培养计划'), ('S5', '援藏计划'), ('S6', '农村学校教育硕士师资培养计划'), ('S7', '高校辅导员攻读思想政治教育专业硕士学位计划'), ('S8', '高校思想政治理论课教师攻读博士学位计划'), ('S9', '其他')], default='S1', help_text='专项计划', max_length=128)),
                ('stu_is_regular_income', models.BooleanField(default=False, help_text='是否有固定收入')),
                ('stu_is_tuition_fees', models.BooleanField(default=False, help_text='是否欠缴学费')),
                ('stu_is_archives', models.BooleanField(default=False, help_text='档案是否转到学校')),
                ('stu_is_superb', models.BooleanField(default=False, help_text='是否优秀毕业生')),
                ('stu_telephone', models.IntegerField(help_text='电话号码', null=True)),
                ('stu_status', models.CharField(choices=[('S1', '在校'), ('S2', '离校'), ('S3', '留校')], default='S1', help_text='在学状态', max_length=64)),
                ('stu_class', models.CharField(help_text='所属班级', max_length=128, null=True)),
                ('academy', models.ForeignKey(help_text='所属学院', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stu_academy', to='academy.Academy')),
                ('major', models.ForeignKey(help_text='学科专业', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stu_major', to='academy.Major')),
                ('research', models.ForeignKey(help_text='科研方向', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stu_research', to='academy.Research')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'ordering': ['stu_number'],
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('tut_number', models.IntegerField(help_text='导师工号', unique=True)),
                ('tut_gender', models.CharField(choices=[('G1', '男'), ('G2', '女')], help_text='性别', max_length=64)),
                ('tut_title', models.CharField(choices=[('T1', '讲师'), ('T2', '副教授'), ('T3', '教授'), ('T4', '副研究员'), ('T5', '研究员'), ('T6', '助教')], help_text='职称', max_length=64)),
                ('tut_cardID', models.CharField(help_text='身份证号', max_length=128, null=True, unique=True)),
                ('tut_birth_day', models.DateField(help_text='出生日期')),
                ('tut_entry_day', models.DateField(help_text='入职日期')),
                ('tut_political', models.CharField(choices=[('P1', '党员'), ('P2', '团员'), ('P3', '群众'), ('P4', '民主党派')], help_text='政治面貌', max_length=64)),
                ('tut_telephone', models.IntegerField(help_text='电话号码', null=True)),
                ('tut_degree', models.CharField(choices=[('D1', '博士'), ('D2', '硕士'), ('D3', '本科')], help_text='学位', max_length=64)),
                ('academy', models.ForeignKey(help_text='所属学院', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='academy', to='academy.Academy')),
                ('education', models.ForeignKey(help_text='学历', null=True, on_delete=True, related_name='education', to='users.Education')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '导师',
                'verbose_name_plural': '导师',
                'ordering': ['tut_number'],
            },
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(help_text='指导老师', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stu_tutor', to='users.Tutor'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stu_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
