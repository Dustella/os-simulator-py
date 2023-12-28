# 操作系统课程设计 - 田青老师 - Python 实现

## 题目要求

![20231229062845](https://img-cdn.dustella.net/markdown/20231229062845.png)

## 必须看的吐槽

### 如果你是田青学生

**请你尽量不要参考这份代码**

**请你尽量不要参考这份代码**

**请你尽量不要参考这份代码**

**这是我这两周接的 9 个课设里唯二搞砸的题目，另一个是同一个老师的同一个题目！**

另外一个搞砸的其实就是这个项目用 Java 重写了一遍，仓库在 https://github.com/Dustella/os-simulator-java

**如果你是田青学生，请你认真阅读下面一段**

    本次我们最大的错误在于，我们以为需要实现一个并发运行的，让所有特性同时运行的一个完整操作系统模拟器。但是做完之后参考别人的系统，我发现，我们被要求的更多是一些零散实验的结合，而非所有特性同时运行的模拟器。

    也因此，最后我们花了非常大的力气设计了指令集、进程模型和 OS 架构，甚至设计了简易的 shell 语言用于执行进程任务来模拟系统的具体操作、用可视化界面展现发生了什么事情，但是这些部分却都不是必要的：虽然对于完整运行的 OS 他们必不可少，但是我们最终只需要分别独立地模拟这些算法即可，没有必要并发运行在同一个过程上。作为代价，我们未能在期限前实现死锁处理、进程同步、页面置换的内容。

总结： 田青让你塞这么多功能，就是想让你把过去实验都复制黏贴到同一个文件夹，添加一个主菜单去选择运行哪一个，**而*不是*独立手搓一个完整的模拟器，并发地运行他要求的所有特性。** 如果你真的这么做了，你会很困惑在什么时机去执行死锁避免，银行家算法要求的资源是什么，也不知道进程同步在纯运行时怎么实现，更不知道在通一个系统里如何展示你的管理器正常运行。

### 如果你是田青本人

这个课设题目真的是烂透了！！！！你是真的什么都想要啊！！！！

我建议不要分组，就一个人手搓一个平时实验课 1.5 倍工作量到 2 倍工作量的小实验，比方说手搓个进程调度器，或者可视化一下换页和紧凑，或者做而且只做一个银行家、一个哲学家。

让 4-5 个人做平时实验课 5-6 倍工作量和巨大难度的课设不会有很好的结果。**结果就是大部分学生不会尝试独立写你的课设，要么复制黏贴开源项目或往期实验，要么像这群可怜人一样找我代做**。但如果这是你期望的，那我不做评价。

### 如果你不是田青学生，且受困于 OS 课设

如果你最终的目标就是做一个 General 的 OS 模拟器，而且确实希望有一个指令集、调度系统和设备管理器，那我有自信，这个项目的架构依然是一个相当不错的参考。

但是，我更推荐大部分人去参考这一个 Variant，是我给另一个女孩子做的，仓库位置在 https://github.com/Dustella/schedular-simulator-py

它就是从本项目改出来的，相比较之下，虽然去除了管程、设备、文件、线程这些外置的管理器，也不考虑进程同步或者死锁，但是它提供了你们更需要的东西：

- 稳定无 bug 的调度器，能够所有进程运行结束

- 动态优先级/多级反馈调度算法，有两个就绪队列

- 重写了内存管理器，指令更加合理，支持缺页中断

- 真正实现了 LRU 换页算法，可以在 GUI 的内存区域正确染色

**由于这个课设很成功很成功**，我真的不能说我的翻车不是题目的问题。

非常幸运的是，除了田青之外的大部分老师的课设题目都和那个女孩子的课设题目比较像。

### 文档

这份课设有写对应的课程报告，需要的人给我发邮件索取