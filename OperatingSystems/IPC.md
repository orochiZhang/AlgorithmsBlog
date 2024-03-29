# 进程间通信
Interprocess communication，简称IPC 

## 管道（Pipe）有名管道（named pipe）
管道可用于具有亲缘关系进程（父子进程）间的通信，用于连接一个读进程和一个写进程以实现它们之间通信的一个共享文件，又名pipe文件。   
有名管道克服了管道没有名字的限制，因此，除具有管道所具有的功能外，有名管道还允许无亲缘关系进程间的通信。

管道和套接字的区别：管道是半双工，套接字是全双工。

## 信号（Signal）
信号是比较复杂的通信方式，用于通知接受进程有某种事件发生，除了用于进程间通信外，进程还可以发送信号给进程本身；linux除了支持Unix早期信号语义函数sigal外，还支持语义符合Posix.1标准的信号函数sigaction（实际上，该函数是基于BSD的，BSD为了实现可靠信号机制，又能够统一对外接口，用sigaction函数重新实现了signal函数）。

## 消息（Message）队列
消息队列是消息的链接表，包括Posix消息队列system V消息队列。有足够权限的进程可以向队列中添加消息，被赋予读权限的进程则可以读走队列中的消息。消息队列克服了信号承载信息量少，管道只能承载无格式字节流以及缓冲区大小受限等缺点。

## 共享内存
使得多个进程可以访问同一块内存空间，是最快的可用IPC形式。是针对其他通信机制运行效率较低而设计的。往往与其它通信机制，如信号量结合使用，来达到进程间的同步及互斥。  

## 内存映射（mapped memory）
内存映射允许任何多个进程间通信，每一个使用该机制的进程通过把一个共享的文件映射到自己的进程地址空间来实现它。

## 信号量（semaphore）
主要作为进程间以及同一进程不同线程之间的同步手段。 

## 套接字（Socket）
更为一般的进程间通信机制，可用于不同机器之间的进程间通信。起初是由Unix系统的BSD分支开发出来的，但现在一般可以移植到其它类Unix系统上：Linux和System V的变种都支持套接字。


## 参考文献
- [Unix系统中，哪些可以用于进程间的通信](https://zhidao.baidu.com/question/436350547665271564.html)
