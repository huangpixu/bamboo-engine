# Generated by Django 2.2.19 on 2021-03-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CallbackData",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(max_length=33, verbose_name="节点 ID")),
                ("version", models.CharField(max_length=33, verbose_name="状态版本")),
                ("data", models.TextField(verbose_name="回调数据")),
            ],
        ),
        migrations.CreateModel(
            name="ContextOutputs",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("pipeline_id", models.CharField(max_length=33, unique=True, verbose_name="流程 ID")),
                ("outputs", models.TextField(verbose_name="输出配置")),
            ],
        ),
        migrations.CreateModel(
            name="Data",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(db_index=True, max_length=33, unique=True, verbose_name="节点 ID")),
                ("inputs", models.TextField(verbose_name="原始输入数据")),
                ("outputs", models.TextField(verbose_name="原始输出数据")),
            ],
        ),
        migrations.CreateModel(
            name="ExecutionData",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(db_index=True, max_length=33, unique=True, verbose_name="节点 ID")),
                ("inputs_serializer", models.CharField(max_length=32, verbose_name="输入序列化器")),
                ("outputs_serializer", models.CharField(max_length=32, verbose_name="输出序列化器")),
                ("inputs", models.TextField(verbose_name="节点执行输入数据")),
                ("outputs", models.TextField(verbose_name="节点执行输出数据")),
            ],
        ),
        migrations.CreateModel(
            name="Node",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(db_index=True, max_length=33, verbose_name="节点 ID")),
                ("detail", models.TextField(verbose_name="节点详情")),
            ],
        ),
        migrations.CreateModel(
            name="Process",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("parent_id", models.BigIntegerField(db_index=True, default=-1, verbose_name="父进程 ID")),
                ("ack_num", models.IntegerField(default=0, verbose_name="收到子进程 ACK 数量")),
                ("need_ack", models.IntegerField(default=-1, verbose_name="需要收到的子进程 ACK 数量")),
                ("asleep", models.BooleanField(default=True, verbose_name="是否处于休眠状态")),
                ("suspended", models.BooleanField(default=False, verbose_name="是否处于暂停状态")),
                ("frozen", models.BooleanField(default=False, verbose_name="是否处于冻结状态")),
                ("dead", models.BooleanField(default=False, verbose_name="是否已经死亡")),
                ("last_heartbeat", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="上次心跳时间")),
                ("destination_id", models.CharField(default="", max_length=33, verbose_name="执行终点 ID")),
                (
                    "current_node_id",
                    models.CharField(db_index=True, default="", max_length=33, verbose_name="当前节点 ID"),
                ),
                ("root_pipeline_id", models.CharField(max_length=33, verbose_name="根流程 ID")),
                (
                    "suspended_by",
                    models.CharField(db_index=True, default="", max_length=33, verbose_name="导致进程暂停的节点 ID"),
                ),
                ("priority", models.IntegerField(verbose_name="优先级")),
                ("queue", models.CharField(default="", max_length=128, verbose_name="所属队列")),
                ("pipeline_stack", models.TextField(default="[]", verbose_name="流程栈")),
            ],
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(max_length=33, unique=True, verbose_name="节点 ID")),
                ("root_id", models.CharField(db_index=True, default="", max_length=33, verbose_name="根节点 ID")),
                ("parent_id", models.CharField(db_index=True, default="", max_length=33, verbose_name="父节点 ID")),
                ("name", models.CharField(max_length=64, verbose_name="状态名")),
                ("version", models.CharField(max_length=33, verbose_name="状态版本")),
                ("loop", models.IntegerField(default=1, verbose_name="循环次数")),
                ("retry", models.IntegerField(default=0, verbose_name="重试次数")),
                ("skip", models.BooleanField(default=False, verbose_name="是否跳过")),
                ("error_ignored", models.BooleanField(default=False, verbose_name="是否出错后自动忽略")),
                ("created_time", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("started_time", models.DateTimeField(null=True, verbose_name="开始时间")),
                ("archived_time", models.DateTimeField(null=True, verbose_name="归档时间")),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("type", models.IntegerField(verbose_name="调度类型")),
                ("process_id", models.BigIntegerField(default=-1, verbose_name="进程 ID")),
                ("node_id", models.CharField(max_length=33, verbose_name="节点 ID")),
                ("finished", models.BooleanField(default=False, verbose_name="是否已完成")),
                ("expired", models.BooleanField(default=False, verbose_name="是否已过期")),
                ("scheduling", models.BooleanField(default=False, verbose_name="是否正在调度")),
                ("version", models.CharField(max_length=33, verbose_name="状态版本")),
                ("schedule_times", models.IntegerField(default=0, verbose_name="被调度次数")),
            ],
            options={
                "unique_together": {("node_id", "version")},
            },
        ),
        migrations.CreateModel(
            name="LogEntry",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(max_length=33, verbose_name="节点 ID")),
                ("loop", models.IntegerField(default=1, verbose_name="循环次数")),
                ("logger_name", models.CharField(max_length=128, verbose_name="logger 名称")),
                ("level_name", models.CharField(max_length=32, verbose_name="日志等级")),
                ("message", models.TextField(null=True, verbose_name="日志内容")),
                ("logged_at", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="输出时间")),
            ],
            options={
                "index_together": {("node_id", "loop")},
            },
        ),
        migrations.CreateModel(
            name="ExecutionHistory",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(max_length=33, verbose_name="节点 ID")),
                ("loop", models.IntegerField(default=1, verbose_name="循环次数")),
                ("retry", models.IntegerField(default=0, verbose_name="重试次数")),
                ("skip", models.BooleanField(default=False, verbose_name="是否跳过")),
                ("version", models.CharField(max_length=33, verbose_name="状态版本")),
                ("started_time", models.DateTimeField(verbose_name="开始时间")),
                ("archived_time", models.DateTimeField(verbose_name="归档时间")),
                ("inputs_serializer", models.CharField(max_length=32, verbose_name="输入序列化器")),
                ("outputs_serializer", models.CharField(max_length=32, verbose_name="输出序列化器")),
                ("inputs", models.TextField(verbose_name="节点执行输入数据")),
                ("outputs", models.TextField(verbose_name="节点执行输出数据")),
            ],
            options={
                "index_together": {("node_id", "loop")},
            },
        ),
        migrations.CreateModel(
            name="ContextValue",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("pipeline_id", models.CharField(max_length=33, verbose_name="流程 ID")),
                ("key", models.CharField(max_length=128, verbose_name="变量 key")),
                ("type", models.IntegerField(verbose_name="变量类型")),
                ("serializer", models.CharField(max_length=32, verbose_name="序列化器")),
                ("code", models.CharField(default="", max_length=128, verbose_name="计算型变量类型唯一标志")),
                ("value", models.TextField(verbose_name="变量值")),
                ("references", models.TextField(verbose_name="所有对其他变量直接或间接的引用")),
            ],
            options={
                "unique_together": {("pipeline_id", "key")},
            },
        ),
    ]
