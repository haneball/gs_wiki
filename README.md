# gs_wiki

#### 介绍

gs_wiki 是一个 Genshin 数据网站，提供角色、武器等信息的查询服务。前端基于 Vue.js 和 Element-UI 搭建，使用 axios 请求后端获得数据。后端基于 Django 开发，用于接收前端请求，查询数据库并返回 json 数据。数据库采用 MySQL 存储，并辅以 Navicat 进行管理。


#### 架构

- 前端: Vue.js2 + Element-UI
- 后端: Django
- 数据库: MySQL


#### 安装

1. 在项目根目录 /gs_wiki 下，创建虚拟环境

```
python -m vnev proj_env  # proj_env 为虚拟环境文件名, 可自定义
```

2. 进入虚拟环境

```
proj_env/bin/activate  # Linux 下使用
proj_env\Scripts\Acticate  # Windows 下使用
```

3.  安装 Django 依赖

```
pip install -r requirments.txt
```

4. 在 /gs_wiki/gs_wiki，即 settings.py 文件所在目录下，创建 .env 文件，写入 Django 的环境配置

```
DEBUG=False
SECRET_KEY='your secret key'
ALLOWED_HOSTS=localhost
TEMPLATES_DIRS='client/dist'
STATICFILES_DIRS='client/dist/static'
DATABASE_NAME='your database name'
DATABASE_USER='your database user'
DATABASE_PASSWORD='your database password'
DATABASE_HOST='your database host'
DATABASE_PORT='your database port'
```

5.  在 /gs_wiki/client 下，安装 Vue.js 依赖

```
npm install
```

6. 打包 Vue.js 项目文件

```
npm run build
```

7.  在项目根目录 /gs_wiki 下，迁移数据库

```
python manage.py makemigrations
python manage.py migrate
```


#### 运行
在虚拟环境下，输入以下指令即可运行项目(本地)，默认运行在 localhost:8000

```
python manage.py runserver
```


#### 使用说明

1.  建议使用 3.7.0 以上版本的 Python 及 16.16.0 以上版本的 Node.JS
2.  运行项目前，务必建立并连接 MySQL 数据库


#### 更新日志
| 时间 | 内容 | 备注 |
|----|----|----|
|   2022/11/18 |使用 bilibili 视频 iframe，以对话框 dialog 的形式添加角色演示。    |  无  |

