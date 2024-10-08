---
description: '翻译说明'
part: 翻译说明
path: /translators
showBookMenu: true
title: '翻译说明'
weight: 5
---

# freebsd 文档翻译计划

freebsd 官方文档的中文文档年久失修，由于 freebsd 官方文档使用的是 asciidoctor (.adoc) 格式文档，并且已经有 po4a 工具进行辅助翻译，所以目前该项目仍然使用该工具进行翻译，并且使用官方网站模板进行静态部署。  

## 翻译流程

po4a 可以将 asciidoctor 文档中的文本块进行提取，生成 po 文件，该文件只包含一对对需要翻译的文档块，屏蔽了格式细节（仍有少量格式出现在翻译块中），那么只需要对 po 文件进行翻译，然后再使用 po4a 工具对源文档进行还原翻译即可。po 文件可以采用翻译引擎的 api 进行自动机器翻译，加快翻译效率，人工只需要进行校对即可。

1. 定期同步  
   上游子模块在`Upstream`，定期对上游文档同步，将原始英文文档复制到website目录下，并且生成待翻译的 po 文件。
2. 自动翻译  
   对上一步生成的 po 文件，使用翻译存储器对 po 文件进行自动翻译，该步骤会将历史翻译过的译文直接进行翻译，并将处理后的 po 文件写入`zh-cn`目录中。
3. 机器翻译  
   使用机器翻译引擎，对待翻译的 po 文件进行翻译，并打上`fuzzy`标签，结果会写入源文件。
4. 人工校验  
   人工对`zh-cn`中的 po 文件进行校验，对带有`fuzzy`标记的文档对进行校对，若涉及到一些链接或不需要翻译的术语，可将`msgstr`中的内容置空，当一个文档对校对完毕时，删除其`fuzzy`标记。并进行PR。
5. 自动构建部署  
   github action会对文档进行自动部署，在目前部署中，会生成`自动翻译`语言选项的内容，该内容会将无校对带有`fuzzy`标记的文本也进行翻译显示。

## 翻译进度

我们首先对 HandBook 进行了翻译，目前进度如下：

|章节|自动翻译|第一轮校对|
|-|-|-|
|introduction|✅|✅|
|preface|✅|✅|
|第一部分|✅|✅|
|parti|✅|✅|
|introduction|✅|✅|
|bsdinstall|✅|✅|
|basics|✅|✅|
|ports|✅|✅|
|x11|✅|✅|
|wayland|✅|✅|
|network|✅|✅|
|第二部分|✅|4/7|
|partii|✅|✅|
|desktop|✅|✅|
|multimedia|✅||
|kernelconfig|✅|✅|
|printing|✅||
|linuxemu|✅|✅|
|wine|✅||
|第三部分|✅|12/16|
|partiii|✅|✅|
|config|✅|✅|
|boot|✅|✅|
|security|✅|✅|
|jails|✅|✅|
|mac|✅|✅|
|audit|✅|✅|
|disks|✅|✅|
|geom|✅||
|zfs|✅|✅|
|filesystems|✅|✅|
|virtualization|✅||
|l10n|✅||
|cutting|✅|✅|
|dtrace|✅|✅|
|usb|✅||
|第四部分|✅|5/7|
|partiv|✅|✅|
|serialcomms|✅|✅|
|ppp-and-slip|✅||
|mail|✅||
|network-servers|✅|✅|
|firewalls|✅|✅|
|advanced-networking|✅|✅|
|第五部分|✅|2/7|
|partv|✅|✅|
|mirrors|✅|✅|
|bibliography|✅||
|eresources|✅||
|pgpkeys|✅||
|glossary|✅||
|colophon|✅||

# 参与

目前仅我一个人对上述进行翻译的文档进行校验，欢迎小伙伴一起进行翻译校验，直接提交PR即可。