## TCP的Retransmission Timeout(RTO)
为了防止数据报丢失,当TCP发送一个报文时,就启动重传计时器,有2种情况:
1. 若在计时器超时之前收到了特定报文的确认,则撤消这个计时器;
2. 特定数据报在计时器超时前没有收到确认,则重传该数据报,并把计时器复位

### TCP的RTO计算

**RTT**: 发送一个数据包到收到对应的ACK，所花费的时间     
**RTO**: 重传超时时间，即从数据发送时刻算起，超过这个时间便执行重传     
**SRTT**: 平滑RTT    
**RTTVAR**：平滑RTT和真实RTT的差距

RTO根据RTT不断的进行调整，防止重传时间太短导致发出太多包，防止重传时间太长使得应用层反应缓慢

第一次RTO计算方法, 假设RTT = R
```
1. SRTT = R

2. RTTVAR = R/2

3. RTO = SRTT + max(G, K*RTTVAR) , K = 4
```
后续的RTO计算,假设当前的RTT为R，RTTVAR'，SRTT'是上一次的RTTVAR，SRTT。
```
计算平滑RTT和真实RTT的差距
RTTVAR = (1 - beta)*RTTVAR' + beta*|SRTT' - R|   

计算平滑RTT
SRTT = (1 - alpha)*SRTT' + alpha*R 

RTO = SRTT + max(G, K*RTTVAR)

alpha = 1/8  beta = 1/4
```

【问题】
假定TCP在开始建立连接时，发送方设定超时重传时间是RTO=6s。    
1. 当发送方接到对方的连接确认报文段时，测量出RTT样本值为1.5s。试计算现在的RTO值。   
2. 当发送方发送数据报文段并接收到确认时，测量出RTT样本值为2.5s。试计算现在的RTO值。

【答案】 
```
根据RFC6298

RTT(1) = 1.5

SRTT(1) = RTT(1) = 1.5

RTTVAR(1) = 1.5/2 = 0.75

RTO = 1.5 + 4*0.75 = 4.5s 所以现在RTO的值为4.5s

接着计算第二步 RTT (2) = 2.5

RTTVAR(2) = 3/4 * 0.75 + 1/4 * |1.5 - 2.5| = 13/16

SRTT(2) = 7/8 *1.5 + 1/8*2.5 = 1.625

RTO = 1.625 + 4 * 13/16 = 4.875

```

## TCP拥塞控制     
TCP就是通过这种小速率探测网络拥堵情况，指数增加发送速度。  
检测到丢包，发送速率减半，直到不再检测到丢包。    
线性增长发送速率，检测到丢包，再指数减小发送速率。    
     
TCP流控算法的关键，是基于丢包，有否丢包是唯一的判断依据，是加油门还是踩刹车。

但TCP由于对网络了解的很片面，无法分辨丢包是什么原因造成的：
1. 网络真的拥堵而丢包
2. 线路质量差CRC校验失败丢、或信号干扰丢
3. IP包乱序而引起的误判

只有情况1是需要踩刹车的，而情况2、3并不需要。
![image](https://raw.githubusercontent.com/orochiZhang/computer-network-note/master/Pictures/congestion-avoidance.png)

## TCP自动重传请求
自动重传请求（Automatic Repeat-reQuest，ARQ）是OSI模型中数据链路层的错误纠正协议之一。它包括停止等待ARQ协议和连续ARQ协议，错误侦测（Error Detection）、正面确认（Positive Acknowledgment）、逾时重传（Retransmission after Timeout）与负面确认继以重传（Negative Acknowledgment and Retransmission）等机制。

传统自动重传请求分成为三种，即停等式(stop-and-wait）ARQ，回退n帧（go-back-n）ARQ，以及选择性重传（selective repeat）ARQ。后两种协议是滑动窗口技术与请求重发技术的结合，由于窗口尺寸开到足够大时，帧在线路上可以连续地流动，因此又称其为连续ARQ协议。三者的区别在于对于出错的数据报文的处理机制不同。三种ARQ协议中，复杂性递增，效率也递增。除了传统的ARQ，还有混合ARQ（Hybrid-ARQ）。
### 停等式ARQ
在停等式ARQ中，数据报文发送完成之后，发送方等待接收方的状态报告，如果状态报告报文发送成功，发送后续的数据报文，否则重传该报文。

停等式ARQ，发送窗口和接收窗口大小均为1，发送方每发送一帧之后就必须停下来等待接收方的确认返回，仅当接收方确认正确接收后再继续发送下一帧。该方法所需要的缓冲存储空间最小，缺点是信道效率很低。
### 回退n帧的ARQ
发信侧不用等待收信侧的应答，持续的发送多个帧，假如发现已发送的帧中有错误发生，那么从那个发生错误的帧开始及其之后所有的帧全部再重新发送。

特点：（GDN）复杂度低，但是不必要的帧会再重发，所以大幅度范围内使用的话效率是不高的

例：如果序列号有K bits，那么这个ARQ的协议大小为：2^k-1。
### 选择性重传ARQ
发信侧不用等待收信侧的应答，持续的发送多个帧，假如发现已发送的帧中有错误发生，那么发信侧将只重新发送那个发生错误的帧。

特点：相对于GDN 复杂度高，但是不需要发送没必要的帧，所以效率高。

例：如果序列号有K bits，那么这个ARQ的协议大小为：2^(k-1)。
### 混合ARQ
在混合ARQ中，数据报文传送到接收方之后，即使出错也不会被丢弃。接收方指示发送方重传出错报文的部分或者全部信息，将再次收到的报文信息与上次收到的报文信息进行合并，以恢复报文信息。

## 三次握手和四次挥手
**【问题1】为什么连接的时候是三次握手，关闭的时候却是四次握手？**    
答：因为当Server端收到Client端的SYN连接请求报文后，可以直接发送SYN+ACK报文。其中ACK报文是用来应答的，SYN报文是用来同步的。但是关闭连接时，当Server端收到FIN报文时，很可能并不会立即关闭SOCKET，所以只能先回复一个ACK报文，告诉Client端，"你发的FIN报文我收到了"。只有等到我Server端所有的报文都发送完了，我才能发送FIN报文，因此不能一起发送。故需要四步握手。

**【问题2】为什么TIME_WAIT状态需要经过2MSL(最大报文段生存时间)才能返回到CLOSE状态？**      
答：虽然按道理，四个报文都发送完毕，我们可以直接进入CLOSE状态了，但是我们必须假象网络是不可靠的，有可以最后一个ACK丢失。所以TIME_WAIT状态就是用来重发可能丢失的ACK报文。


![image](https://raw.githubusercontent.com/orochiZhang/computer-network-note/master/Pictures/tcp-sequence.png)

## 参考文献
- [TCP-IP详解: RTT和RTO的计算方法](https://blog.csdn.net/wdscq1234/article/details/52505191)
- [浅析TCP字节流与UDP数据报的区别](https://blog.csdn.net/donghustone/article/details/49657803)
