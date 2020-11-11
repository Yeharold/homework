# Linux作业提交系统使用教程

## 解压homework

- 将homework解压放与用户主目录下

  ```shell
  mv homework-main homework
  ```

- Linux命令行中安装依赖软件

  ```shell
  #python3 版本需大于等于3.6
  sudo pip3 install sanic
  ```

## alias设置与编辑

- 在用户主目录下编辑.bashrc文件

  ```
  cd 
  nano .bashrc
  ```

- 在.bashrc文件中添加如下内容：

  ```
  alias homework="if [ ! -d "~/homework/static" ];then mkdir ~/homework/static;fi;python3 ~/homework/app.py &"
  alias khomework="bash ~/homework/.sdhomework.sh"
  alias class="bash ~/homework/.moveto.sh"
  ```

- 保存退出nano编辑并执行如下：

  ```shell
  source .bashrc
  ```

## 相关使用教程

- 启动服务

  ```shell
  homework
  ```

- 设置定时

  ```shell
  #设置10分钟后自动关闭服务
  khomework 10
  ```

- 回收作业

  ```
  #将提交的作业拷贝到18iot目录中
  class 18iot
  ```

  
