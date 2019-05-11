# Generated by Django 2.1.7 on 2019-05-09 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('aca_avatar', models.ImageField(default='default.png', null=True, upload_to='academies', verbose_name='学院图标')),
                ('aca_nickname', models.CharField(max_length=128, null=True, verbose_name='学院简称')),
                ('aca_cname', models.CharField(max_length=128, null=True, verbose_name='学院名称(中)')),
                ('aca_ename', models.CharField(max_length=128, null=True, verbose_name='学院名称(英)')),
                ('aca_code', models.IntegerField(null=True, verbose_name='学院代码')),
                ('aca_phone', models.CharField(max_length=128, null=True, verbose_name='学院电话')),
                ('aca_fax', models.CharField(max_length=128, null=True, verbose_name='学院传真')),
                ('aca_href', models.URLField(max_length=256, null=True, verbose_name='学院网址')),
                ('aca_brief', models.TextField(verbose_name='学院简介')),
                ('aca_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aca_user', to=settings.AUTH_USER_MODEL, verbose_name='学院负责人')),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
                'db_table': 'academy',
                'permissions': [('can_insert_academy', '新增学院'), ('can_delete_academy', '删除学院'), ('can_update_academy', '修改学院'), ('can_search_academy', '查询学院')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('cla_name', models.CharField(max_length=128, null=True, verbose_name='班级名称')),
                ('cla_code', models.IntegerField(null=True, verbose_name='班级代码')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
                'db_table': 'classes',
                'permissions': [('can_insert_class', '新增班级'), ('can_delete_class', '删除班级'), ('can_update_class', '修改班级'), ('can_search_class', '查询班级')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('maj_name', models.CharField(max_length=128, null=True, verbose_name='学科名称')),
                ('maj_code', models.IntegerField(null=True, verbose_name='学科编号')),
                ('maj_type', models.CharField(choices=[('C1', '专业硕士学位'), ('C2', '学科硕士学位')], max_length=128, verbose_name='学科类型')),
                ('maj_first', models.BooleanField(verbose_name='是否一级学科')),
                ('maj_second', models.BooleanField(verbose_name='是否二级学科')),
                ('maj_first_uuid', models.UUIDField(null=True, verbose_name='所属一级学科')),
                ('maj_setup_time', models.DateField(verbose_name='获批时间')),
                ('maj_degree', models.CharField(choices=[('D1', '哲学'), ('D2', '经济学'), ('D3', '法学'), ('D4', '教育学'), ('D5', '文学'), ('D6', '历史学'), ('D7', '理学'), ('D8', '工学'), ('D9', '农学'), ('D10', '医学'), ('D11', '军事学'), ('D12', '管理学'), ('D13', '艺术学')], max_length=128, verbose_name='学位类型')),
            ],
            options={
                'verbose_name': '学科专业',
                'verbose_name_plural': '学科专业',
                'db_table': 'major',
                'permissions': [('can_insert_major', '新增学科专业'), ('can_delete_major', '删除学科专业'), ('can_update_major', '修改学科专业'), ('can_search_major', '查询学科专业')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Reform',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('time', models.IntegerField(verbose_name='年份')),
                ('ref_type', models.CharField(choices=[('RT1', '研究生教改项目立项'), ('RT2', '研究生教改论文发表'), ('RT3', '研究生课程教材出版'), ('RT4', '研究生教育相关获奖'), ('RT5', '精品/在线课程建设'), ('RT6', '研究生实践基地建设'), ('RT7', '研究生国际交流项目')], max_length=128, verbose_name='教改成果类型')),
                ('ref_name', models.TextField(verbose_name='教改项目名称')),
                ('academy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_academy', to='学院管理.Academy', verbose_name='学院名称')),
            ],
            options={
                'verbose_name': '教育改革成果',
                'verbose_name_plural': '教育改革成果',
                'db_table': 'reform',
                'permissions': [('can_insert_reform', '新增教改成果'), ('can_delete_reform', '删除教改成果'), ('can_update_reform', '修改教改成果'), ('can_search_reform', '查询教改成果')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ReformResults',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('time', models.IntegerField(verbose_name='年份')),
                ('project_count', models.IntegerField(default=0, verbose_name='研究生教育相关教改项目立项数量')),
                ('paper_count', models.IntegerField(default=0, verbose_name='发表研究生教育相关教改论文数量')),
                ('textbook_count', models.IntegerField(default=0, verbose_name='出版研究生教材数量')),
                ('award_count', models.IntegerField(default=0, verbose_name='研究生教育相关获奖数量')),
                ('course_count', models.IntegerField(default=0, verbose_name='精品/在线课程建设数量')),
                ('base_count', models.IntegerField(default=0, verbose_name='实践基地建设数量')),
                ('exchange_project_count', models.IntegerField(default=0, verbose_name='研究生国际交流数量')),
                ('academy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rr_academy', to='学院管理.Academy', verbose_name='学院名称')),
            ],
            options={
                'verbose_name': '教育改革成果统计',
                'verbose_name_plural': '教育改革成果统计',
                'db_table': 'reform_result',
                'permissions': [('can_insert_reform_result', '新增教改统计'), ('can_delete_reform_result', '删除教改统计'), ('can_update_reform_result', '修改教改统计'), ('can_search_reform_result', '查询教改统计')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='唯一标识ID')),
                ('res_name', models.CharField(max_length=128, null=True, verbose_name='研究方向')),
            ],
            options={
                'verbose_name': '研究方向',
                'verbose_name_plural': '研究方向',
                'db_table': 'research',
                'permissions': [('can_insert_research', '新增研究方向'), ('can_delete_research', '删除研究方向'), ('can_update_research', '修改研究方向'), ('can_search_research', '查询研究方向')],
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='major',
            name='research',
            field=models.ManyToManyField(related_name='research', to='学院管理.Research', verbose_name='科研方向'),
        ),
        migrations.AddField(
            model_name='class',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cla_major', to='学院管理.Major', verbose_name='专业名称'),
        ),
        migrations.AddField(
            model_name='academy',
            name='majors',
            field=models.ManyToManyField(related_name='majors', to='学院管理.Major'),
        ),
    ]
