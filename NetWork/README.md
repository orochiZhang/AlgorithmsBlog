# computer-network-note
计算机网络基础笔记
<table>
<tr>
<td>OSI七层网络模型</td>
<td>TCP/IP四层概念模型</td>
<td>网络协议</td>
</tr>
<tr>
<td>应用层（Application）</td>
<td rowspan="3">应用层</td>
<td>
HTTP, TFTP, FTP, NFS, WAIS,SMTP
</td>
</tr>

<tr>
<td>表示层（Presentation）</td>
<td>Telnet, Rlogin, SNMP, Gopher</td>
</tr>

<tr>
<td>会话层（Session）</td>
<td>SMTP, DNS</td>

</tr>

<tr>
<td>传输层（Transport）</td>
<td>传输层</td>
<td>TCP, UDP</td>
</tr>

<tr>
<td>网络层（Network）</td>
<td>网络层</td>
<td>IP, ICMP, ARP, RARP, AKP, UUCP</td>
</tr>


<tr>
<td>数据链路层（Data Link）</td>
<td rowspan="2">数据链路层</td>
<td>FDDI, Ethernet, Arpanet, PDN, SLIP, PPP</td>
</tr>

<tr>
<td>物理层（Physical）</td>
<td>IEEE 802.1A, IEEE 802.2到IEEE 802.11</td>
</tr>
</table>


## 应用层
- [Overview](https://github.com/orochiZhang/computer-network-note/blob/master/Applicationlayer/Overview.md)
- HTTP2
- HTTP
  1. [HTTP协议基础解析](https://github.com/orochiZhang/computer-network-note/blob/master/Applicationlayer/HTTP_data_structure.md)
  2. [HTTP的请求方法和幂等性](https://github.com/orochiZhang/computer-network-note/blob/master/Applicationlayer/HTTP_Method_Idempotent.md)

- [DHCP](https://baike.baidu.com/item/DHCP/218195)
- RIP
- DNS
- [SNMP](https://baike.baidu.com/item/%E7%AE%80%E5%8D%95%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%8D%8F%E8%AE%AE/2986113)
- FTP
- [TFTP](https://baike.baidu.com/item/tftp/455170)

## Socket
- Socket的五种IO模型

## 传输层
- [TCP与UDP](https://github.com/orochiZhang/computer-network-note/blob/master/Transportlayer/TCP_and_UDP.md)
- [TCP](https://github.com/orochiZhang/computer-network-note/blob/master/Transportlayer/TCP.md)
- UDP(UDP组播)

## 网络层
- IP
- [IP地址分类，子网划分，CIDR构造超网](https://github.com/orochiZhang/computer-network-note/blob/master/Networklayer/IP_address.md)
- ARP
- [ICMP/IGMP](https://github.com/orochiZhang/computer-network-note/blob/master/Networklayer/ICMP_and_IGMP.md)

- [外部网关协议/内部网关协议](https://github.com/orochiZhang/computer-network-note/blob/master/Networklayer/IGP_and_EGP.md)
  1. [外部网关协议BGP](https://github.com/orochiZhang/computer-network-note/blob/master/Networklayer/BGP.md)
  2. [内部网关协议RIP/OSPF](https://github.com/orochiZhang/computer-network-note/blob/master/Networklayer/RIP_and_OSPF.md)

## 数据链路层/计算机网络硬件
IEEE802系列标准把数据链路层分成LLC（Logical Link Control，逻辑链路控制）和MAC（Media Access Control，介质访问控制）两个子层。   
LLC子层实现数据链路层与硬件无关的功能，比如流量控制、差错恢复等。   
MAC子层提供LLC和物理层之间的接口。    

- [路由器与交换机](https://github.com/orochiZhang/computer-network-note/blob/master/DataLinkLayer/Router_and_Switch.md)

## 参考书籍
- 《计算机网络自顶向下方法》
- 《图解网络硬件》
- 《图解TCP/IP》
