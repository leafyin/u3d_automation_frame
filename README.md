## ui 测试工程

### 主要工程文件
* Basic
  * BaseTest 抽象基础方法类
  * AndroidInfo 安卓手机基础设备信息类
* AirTest 
  * airtest测试库封装测试步骤、独立case，基于图像识别，基于BaseTest实现
  * 当前提供的独立case
    * 新手引导
    * 英雄升级
    * 装备升级
    * 羁绊升级
    * 持续新增case中...
  * 测试步骤见源文件
* PocoTest
  * poco测试库封装的测试步骤、独立case，基于ui空间定位，需要安装包接入pocosdk，基于BaseTest实现
  * 功能基本同等于Airtest
* Entry 
  * 测试工程的入口文件，提供菜单选择