![Static Badge](https://img.shields.io/badge/Python-v3.9.13-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads)
![Static Badge](https://img.shields.io/badge/Node-v18.17.1-green?link=https%3A%2F%2Fnodejs.org%2Fen%2Fabout%2Fprevious-releases)
![Static Badge](https://img.shields.io/badge/license-Apache2.0-yellow?link=https%3A%2F%2Fgithub.com%2Fhaneball%2Fgs_wiki%2Fblob%2Fmaster%2FLICENSE)


# gs_wiki

#### 介绍

gs_wiki 是一个 Genshin 数据网站，提供角色、武器等信息的查询服务。前端基于 Vite + Vue3 和 Element-Plus 搭建，采用响应式布局，适配了常见的 PC 及移动端的屏幕比例。后端基于 Django 开发。数据库采用 MySQL 存储并使用 Navicat 进行管理。


#### 架构

- 前端: Vite + Vue3 + Element-Plus
- 后端: Django
- 数据库: MySQL + Navicat


#### 功能

- 版本倒计时
- 近期角色生日
- 每日素材
- 角色、武器图鉴
- 历史祈愿计时


#### 目录结构

```
.
│  .gitignore
│  LICENSE
│  README.md
│  
├─client                                        // 客户端文件
│  │  .gitignore
│  │  index.html
│  │  package.json
│  │  README.md
│  │  vite.config.js                            // Vite 配置
│  │  
│  ├─.vscode
│  │      extensions.json
│  │      
│  │          
│  ├─public
│  │      favicon.ico
│  │      vite.svg
│  │      
│  └─src
│      │  App.vue
│      │  main.js
│      │  style.css
│      │  
│      ├─api                                    // API 接口
│      │      index.js
│      │      
│      ├─assets
│      │  │  vue.svg
│      │  │  
│      │  └─scss
│      │          anime.scss                    // 动画
│      │          index.scss                    // 宽度, 字号, 颜色
│      │          layout.scss
│      │          
│      ├─components                             // 组件
│      │  │  CollapseCard.vue                   // 折叠卡片
│      │  │  HeadNavMenu.vue                    // 导航栏
│      │  │  HelloWorld.vue
│      │  │  ItemCell.vue                       // 图鉴单元
│      │  │  NearEvent.vue
│      │  │  PageFooter.vue                     // 页脚
│      │  │  QuerySearch.vue                    // 搜索框
│      │  │  
│      │  ├─char                                // 角色详情页子组件
│      │  │      AttributeTable.vue             // 信息属性页
│      │  │      BackgroundStory.vue            // 背景故事
│      │  │      ConstellationTable.vue         // 命之座页
│      │  │      ProfileTable.vue               // 资料页
│      │  │      TalentAttr.vue                 // 天赋属性
│      │  │      TalentTable.vue                // 天赋页
│      │  │      VoiceOver.vue                  // 语音页
│      │  │      
│      │  ├─custom                              // 自定义组件
│      │  │      BackTopBtn.vue                 // 回到顶部
│      │  │      PickBar.vue                    // 选项
│      │  │      TabRow.vue                     // 单栏
│      │  │      WindowAffix.vue
│      │  │      
│      │  ├─home                                // 主页子组件
│      │  │      CommingBrith.vue               // 生日
│      │  │      TodayMaterial.vue              // 每日素材
│      │  │      VersionCd.vue                  // 版本倒计时
│      │  │      
│      │  └─timer                               // 计时子组件
│      │          TimerProgress.vue
│      │          
│      ├─router                                 // Vue-Router
│      │      index.js
│      │      
│      ├─store                                  // VueX
│      │      index.js
│      │      
│      ├─utils                                  // 工具
│      │      request.js                        // Vue-Axios
│      │      vue.api.js
│      │      
│      └─views                                  // 视图
│              CharArchive.vue                  // 角色图鉴
│              CharDetail.vue                   // 角色详情
│              GachaTimer.vue                   // 祈愿计时
│              HomePage.vue                     // 主页
│              NotFound.vue                     // 404
│              WeaponArchive.vue                // 武器图鉴
│              WeaponDetail.vue                 // 武器详情
│              
└─gs_wiki                                       // 服务端文件
    │  manage.py
    │  requirements.txt                         // Python 项目依赖列表
    │  
    ├─gs_wiki
    │     settings.py
    │     urls.py
    │     wsgi.py
    │     __init__.py
    │     
    ├─gw_app
    │  │  admin.py
    │  │  apps.py
    │  │  models.py
    │  │  tests.py
    │  │  urls.py
    │  │  views.py
    │  │  __init__.py
    │  │  
    │  └─migrations
    │        __init__.py
    |        
    └─static

```