# frontend

基于 [Vue.js](https://cn.vuejs.org/) 开发项目。<br>
Vue 是一套构建用户界面的渐进式框架，是一个 JavaScript 框架，用于在 HTML 页面上实现用户界面。


## 开发

``` bash环境
# 安装依赖
npm install

# 以 watch 模式编译前端文件
npm run dev

# 编译生产环境代码，代码自动被压缩
npm run build
```

## 代码分析
整个目录结构：<br>
![](https://github.com/chenzy01/shiyanlou/blob/master/Radis_Monitoring_Tool/rmon/rmon/frontend/frontend%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)
<br>
1、通过Webpack编译，发布到路径：../rmon/rmon/static/js/app.js 文件中。<br>
2、package.json:包含了关于整个项目的各种信息，比如项目名称，可执行命令，以及整个项目的依赖软件包。<br>
3、webpack.config.js ：执行 webpack 命令时从这个文件中读取相应的配置信息。<br>
4、.babelrc ：将 ES6 语法的源代码转译为浏览器能够识别的语法，通过 Babel 工具完成。<br>
5、main.js ： frontend 项目的入口文件。<br>
6、App.vue ：一个 Vue 组件，当浏览器加载 frontend 项目的代码后绘制的第一个组件就是 App.vue，是 Server.vue 和 Metric.vue 的父组件。<br>
7、Server.vue ：实现了 Redis 服务器列表的管理，包括，添加，更新，删除服务器等操作。<br>
8、Metric.vue ：实现了 Redis 监控图表的绘制。<br>

