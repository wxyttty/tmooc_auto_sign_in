# tmooc_auto_sign_in

#### 介绍
selenium 自动登录 tmooc 并签到

基于[tmooc_auto_sign_in: selenium 自动登录 tmooc 并签到 (gitee.com)](https://gitee.com/mincho/tmooc_auto_sign_in?_from=gitee_search) 修改.

### 安装
#### 安装python环境
注意：在安装时，请选择设置python和pip环境变量

#### 安装chrome&&Chromedriver

##### windows

下载地址：http://npm.taobao.org/mirrors/chromedriver/ <br>
下载与chrome浏览器版本最接近的那个版本 <br>
将解压后的可执行文件拷贝到Python安装目录的Scripts目录中 <br>
windows查看python安装目录(cmd命令行)：where python

##### UbuntuLinux

```bash
sudo apt install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
sudo apt-get install xvfb
```

下载地址：http://npm.taobao.org/mirrors/chromedriver/ <br>
下载与chrome浏览器版本最接近的那个版本

```bash
unzip chromedriver_linux64.zip
chmod +x chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```



#### 安装selenium

`pip install selenium`

#### 使用方法
将main.py中的第4步和第5步的账号和密码修改成自己的 <br>

可修改第8步更改日志文件的位置及名字

Windows创建txt写入python 绝对路径\main.py。保存后改后缀为bat通过任务计划程序定时签到.

Linux可crontab -e 在最后加一行

```
45 7 * * * python 绝对路径\main_headless.py >> 绝对路径\tts.log
```

即每天7:45运行.

#### 无头运行Chrome

将main_headless.py中的第4步和第5步的账号和密码修改成自己的<br>

```bash
pip3 install selenium

pip3 install pyvirtualdisplay
```

---Linux root用户将main_headless.py中options.add_argument('--no-sandbox')的注释删去

## 感谢

@[super敏 (mincho) - Gitee.com](https://gitee.com/mincho)

## 另一种方法

[1771346368/TMOOCAUTOCHECKIN (github.com)](https://github.com/1771346368/TMOOCAUTOCHECKIN)

如果报和ssl加密有关的错误请把src/start.js内的链接中的http改为https,

Windows创建任务计划程序定时打开浏览器访问https://tmooc.cn即可.

