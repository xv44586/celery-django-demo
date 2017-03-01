author = XuMingming
django中使用celery来做定时任务

启动worker：celery -A proj worker -l info
启动celery－beat：celery -A proj beat -l info

worker用来从中间人那取出任务来处理
beat是一个调度器，按照 CELERY_BEAT_SCHEDULE 都设置定时将任务推到中间人处。

 broker 与 result_backend 都选用的redis