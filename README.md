# vn.py 
基于python的开源交易平台开发框架

## vn.py框架交流群
QQ群号：262656087

相关问题在这个里面问的答复最快。

## 2015/4/24项目状态##
发布了基于vn.ctp的Demo，在vn.demo/ctpdemo文件夹下，可用于CTP柜台期货公司的手动交易。

## 2015/4/20项目状态##
发布了用于展示如何使用vn.py框架开发的vn.demo，使用了vn.event和vn.lts模块，可以用于华宝证券LTS柜台的手动交易。

demo的简单说明：

- demoApi.py主要包含了程序的底层接口，对vn.lts中的API进行了简化封装
- demoEngine.py主要包含了程序的中间层，负责调用底层接口
- demoUi.py主要包含了用于数据监控和主动函数调用相关的GUI组件
- demoMain.py包含了程序的主函数入口，双击运行
- demoMain.pyw功能和demoMain.py一样，双击时会自动调用pythonw.exe运行（无cmd界面）


接下来将会发布几篇和vn.demo相关的教程在vnpy.org网站上。

## 2015/3/26项目状态##
因为有不少人问CTP的接口，正好我最近的项目也要用到，就把开发CTP封装的工作提前了。

CTP的python封装发布在vn.ctp文件夹下： 
 
1. 封装使用的API是最新支持期货交易所期权的6.3.0版本  
2. md部分已经完全经过了测试  
3. td部分只进行了少量测试，接下来几天会继续，测试仅会覆盖和交易相关的函数（银期转账等等测试大家有需要自己做吧）

## 2015/3/3项目状态 ##
目前完成：  

1. 华宝证券的LTS API的python封装，发布在vn.lts文件夹下  
2. 事件驱动引擎，发布在vn.event文件夹下  

### vn.lts   ###
ltsapi：华宝证券官方的LTS C++ API  
pyscript：用于自动生成重复度较高的封装代码的python脚本  
vnltsmd：行情API的封装源代码和测试脚本  
vnltstd：交易API的封装源代码和测试脚本  

### vn.event ###
eventType：定义事件类型常量  
eventEngine：包含事件驱动引擎实现  

## 下一步计划 ##
1. API封装、编译、使用方面的教程
2. 事件驱动引擎原理、使用方面的教程
3. 基于API和引擎开发的LTS交易客户平台（因为华宝没有提供官方的LTS交易软件，目前的两个实现分别是基于C++的尔易终端和基于.COM封装的盈佳终端）
4. 策略引擎接口

## 联系作者 ##
作者知乎名：用python的trader，想要联系作者可以通过知乎私信。

## 关于Linux下编译运行的说明 ##

知乎：@家俊桑

已初步验证vnpy仅需少量跨平台兼容性修改，再加上华宝的Linux动态链接库文件即可在Linux上编译运行 (仅在Ubuntu x64下测试)

如需在Linux下编译运行，请在bashrc中设置环境变量 LD_LIBRARY_PATH 以及 PYTHON_PATH， 例如：

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/vnpy/vn.lts/vnltsmd/pyltsmd:/root/vnpy/vn.lts/ltsapi:/root/vnpy/vn.lts/ltsl2:/root/vnpy/vn.ctp/ctpapi

export PYTHON_PATH=$PYTHON_PATH:/root/vnpy/vn.lts/vnltsmd/pyltsmd:/root/vnpy/vn.lts/ltsapi:/root/vnpy/vn.lts/ltsl2:/root/vnpy/vn.ctp/ctpapi
```

然后cd至vnpy项目根目录并使用make
vnpy$ make all

ctp及lts api的封装库将以.so的形式被创建，并会被自动拷贝至demo和strategy目录

Linux下代码所需改动主要有
1）使用条件编译移除对stdafx.h的引用

<------------------
```
#include "stdafx.h"
```
------------------>
```
#ifndef __GNU__
#include "stdafx.h"
#endif
```

2) 使用GNU C的strncpy替代MSVC的strcpy_s函数

<------------------

------------------>
```
#ifdef __GNU__
#define strcpy_s(dest, len, src)  strncpy(dest, src, len)
#endif
```

3）demoMain 文件中取消不必要的 windows 函数调用


因为数据和帐号原因，Linux版本并未得到完整测试，权当抛砖引玉

如果在Linux 32位上运行，需要去华宝下载32位的动态链接库
http://www.sfit.com.cn/5_2_DocumentDown.htm

## License ##
MIT

