# KGQAHLM
本项目主要是根据：[KGQA_HLM](https://github.com/chizhu/KGQA_HLM)重构得到。感谢原作者对项目进行开源。

项目开发笔记可参见我CSDN博客：[知识图谱](https://blog.csdn.net/meiqi0538/category_11901623.html?spm=1001.2014.3001.5482)

## 使用方法

项目需要neo4j数据库作为知识存储设备。可以使用`pip install -e .` 的方式在KGQAHLM目录下执行，即可安装到系统中。

系统的配置文件在KGQAHLM/data/config.ini文件中，实例如下：

```text
[neo4j]
host=http://192.168.56.101
port=7474
user=neo4j
password=root

[sys]
relation_path=data/relation.txt
# static dir
people_images_dir=people_images
people_profile_file_path=data/people_profile_file.json
```

在运行项目之前，需要初始化数据库：`flask init-db`执行即可。

项目运行示例（centos7）：

```shell
export FLASK_APP=serve
flask run --host=0.0.0.0
```

然后根据提示即可访问该系统。

## 联系我

1. 我的github：[https://github.com/Htring](https://github.com/Htring)
2. 我的csdn：[科皮子菊](https://piqiandong.blog.csdn.net/)
3. 我订阅号：AIAS编程有道
   ![AIAS编程有道](https://s2.loli.net/2022/05/05/DS37LjhBQz2xyUJ.png)
4. 知乎：[皮乾东](https://www.zhihu.com/people/piqiandong)
