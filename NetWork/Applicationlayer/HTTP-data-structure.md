# HTTP
HTTP是基于TCP的应用层协议。对TCP连接的使用，目前HTTP协议都是客户端发起请求，服务器回送响应。分为两种方式：俗称“短连接”和“长连接”。HTTP1.1规定了默认保持长连接。

## 协议解析
### Request
Get请求：
1. 请求行: 请求类型Get，URL和参数，协议版本。
2. 请求头部。
```
GET /api/article/all/?page=1 HTTP/1.1
Host: dingdingblog.com
Connection: keep-alive
Accept: application/json, text/plain, */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
Referer: http://dingdingblog.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: ……
```

Post请求：
1. 请求行: 请求类型Post，URL, 协议版本。
2. 请求头部。
3. 空行。   
4. 空行之后就是请求数据。
```
POST http://dingdingblog.com/login HTTP/1.1
Host: dingdingblog.com
Connection: keep-alive
Content-Length: 107
Cache-Control: max-age=0
Origin: http://dingdingblog.com
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: http://dingdingblog.com/login
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: ……

_token=Qzg5&email=123&password=123&remember=on
```

### Response
1. 状态行: HTTP协议版本号，状态码，状态消息。
2. 请求头部。
3. 空行。
4. 响应正文，服务器返回给客户端的文本信息。

200响应的例子：     
第一行为状态行，HTTP/1.1表明HTTP版本为1.1版本，状态码为200，状态消息为OK。
```
HTTP/1.1 200 OK
Server: nginx
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/7.3.3
Cache-Control: no-cache, private
Date: Tue, 16 Apr 2019 00:40:01 GMT
Set-Cookie: laravel_session=eyJp……; expires=Tue, 16-Apr-2019 02:40:01 GMT; Max-Age=7200; path=/; httponly
Content-Length: 5603

<!DOCTYPE html>
<html lang="zh-cn">
……
</html>
```

302重定向的例子：
```
HTTP/1.1 302 Found
Server: nginx
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: PHP/7.3.3
Cache-Control: no-cache, private
Date: Tue, 16 Apr 2019 00:43:49 GMT
Location: http://dingdingblog.com/admin/article
Set-Cookie: laravel_session=eyJp……; expires=Tue, 16-Apr-2019 02:43:49 GMT; Max-Age=7200; path=/; httponly

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="refresh" content="0;url=http://dingdingblog.com/admin/article" />

        <title>Redirecting to http://dingdingblog.com/admin/article</title>
    </head>
    <body>
        Redirecting to <a href="http://dingdingblog.com/admin/article">http://dingdingblog.com/admin/article</a>.
    </body>
</html>
```

## Request头部字段解析
1. Accept-Encoding: 浏览器发给服务器,声明浏览器支持的编码类型

2. requestedWith: requestedWith为 null，则为同步请求。requestedWith 为 XMLHttpRequest 则为 Ajax 请求。

3. Referer：    
告诉服务器我是从哪个页面链接过来的，服务器藉此可以获得一些信息用于处理。比如从我主页上链接到一个朋友那里，他的服务器就能够从HTTP Referer中统计出每天有多少用户点击我主页上的链接访问他的网站。     
Referer的正确英语拼法是referrer。由于早期HTTP规范的拼写错误，为了保持向后兼容就将错就错了。

4. Connection: keep-alive     
长连接, 浏览器先发起一个TCP连接去抓取页面。但是抓取页面之后，该TCP连接并不会立即关闭，而是暂时先保持着,这就是“Keep-Alive”。然后浏览器分析HTML之后，发现有很多外部资源，就用刚才那个TCP连接去抓取此页面的外部资源，避免短时间内多次三次握手的开销。

5. Origin：主要是用来说明最初请求是从哪里发起的，origin只用于Post请求。

6. Accept：表示可接受的类型。application/json表示json对象，text/plain表示纯文本形式，\*/\*表示所有类型。

7. Upgrade-Insecure-Requests: 1     
客户端向服务器端发送信号表示它支持 upgrade-insecure-requests 的升级机制。服务器现在可以重定向到这个站点的安全版本。在响应中可以添加一个首部 Vary: Upgrade-Insecure-Requests，这样的话，响应就不会被缓存服务器提供给不支持升级机制的客户端了。

8. Accept-Encoding: 浏览器发给服务器,声明浏览器支持的编码类型。     
gzip，GNUzip的缩写，它是一个GNU自由软件的文件压缩程序。它最早由Jean-loup Gailly和Mark Adler创建，用于UNⅨ系统的文件压缩。   
deflate是同时使用了LZ77算法与哈夫曼编码（Huffman Coding）的一个无损数据压缩算法

9. Accept-Language: 表示接受的语言和权重。服务器可以从诸多备选项中选择一项进行应用， 并使用Content-Language 应答头通知客户端它的选择。    
zh-CN,zh;q=0.9,en;q=0.8表示中文的权重为0.9，英文的权重0.8，优先使用中文。

10. User-Agent：浏览器版本，系统，应用信息等等。

## Response头部字段解析
1. X-Powered-By: 用于描述你这个网站是用什么语言或者框架开发的，出于安全考虑，一般建议隐藏。隐藏的方法是根据各个web框架而定。

2. Server: 服务器信息，也是建议隐藏。
```
PHP隐藏X-Powered-By
修改 php.ini 文件 设置 expose_php = Off

apache 隐藏 server
修改httpd.conf 设置 

ServerSignature Off

ServerTokens Prod

nginx 隐藏 server
修改nginx.conf  在http里面设置 

server_tokens off;
```

3. Conent-Length：表示实体内容长度，客户端（服务器）可以根据这个值来判断数据是否接收完成。

4. Transfer-Encoding: chunked     
当客户端向服务器请求一个静态页面或者一张图片时，服务器可以很清楚的知道内容大小，然后通过Content-length消息首部字段告诉客户端 需要接收多少数据。但是如果是动态页面，服务器是不可能预先知道内容大小，这时就可以使用```Transfer-Encoding：chunk```模式来传输 数据了。      
即如果要一边产生数据，一边发给客户端，服务器就需要使用```Transfer-Encoding: chunked```这样的方式来代替Content-Length。       
chunk编码将数据分成一块一块的发送。Chunked编码将使用若干个Chunk串连而成，由一个标明长度为0的chunk标示结束。每个Chunk分为头部和正文两部分，头部内容指定正文的字符总数（十六进制的数字）和数量单位（一般不写），正文部分就是指定长度的实际内容，两部分之间用回车换行(CRLF) 隔开。在最后一个长度为0的Chunk中的内容是称为footer的内容，是一些附加的Header信息（通常可以直接忽略）。   
Transfer-Encoding和Content-Length是互斥的，如果同时出现，浏览器以Transfer-Encoding为准。

5. Cache-Control：     
public表明响应可以被任何对象（包括：发送请求的客户端，代理服务器，等等）缓存。      
private表明响应只能被单个用户缓存，不能作为共享缓存（即代理服务器不能缓存它）,可以缓存响应内容。    
POST请求会在首部设置```Cache-Control: max-age=0```     
更详细的看[MDN文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Cache-Control)

6. Content-Type：   
text/html; charset=UTF-8表示服务器返回html文档，字符集为 UTF-8。   
application/json表示服务器返回json对象。    
POST请求也会带上这个首部，用于描述它发来什么类型的内容。    
更多类型请参考[List of MIME types](http://www.iana.org/assignments/media-types/media-types.xhtml)

7. Location: 302重定向的目标地址。

8. Date: 表示服务端响应这个请求的时间。

9. Set-Cookie:  

属性 | 说明
---|---
NAME=VALUE | 赋予 Cookie 的名称和其值（必须项）
expires=DATE|指定浏览器可发送Cookie的有效期（若不指定则默认为浏览器关闭为止）
path=PATH | 将服务器上的文件目录作为Cookie的适用对象（若不指定则默认为文档所在的文件目录）
domain=域名 | 作为 Cookie 适用对象的域名（若不指定则默认为创建 Cookie 的服务器的域名）
Secure | 仅在 HTTPS 安全通信时才会发送 Cookie
HttpOnly|加以限制，使 Cookie 不能被 JavaScript 脚本访问。主要目的是为防止跨站脚本攻击对 Cookie 的信息窃取。

10. Vary: Accept-Encoding    
详细请看:
- [HTTP 协议中 Vary 的一些研究](https://www.cnblogs.com/dhsz/p/7016283.html)
- [标头“Vary:Accept-Encoding”指定方法及其重要性分析](http://www.webkaka.com/blog/archives/how-to-set-Vary-Accept-Encoding-header.html)

### Last-Modified
在浏览器第一次请求某一个URL时，服务器端的返回状态会是200，内容是客户端请求的资源，同时有一个Last-Modified的属性标记此文件在服务器端最后被修改的时间。   
Last-Modified格式类似这样：
```
Last-Modified : Fri , 12 May 2006 18:53:33 GMT
```
客户端第二次请求此URL时，根据HTTP协议的规定，浏览器会向服务器传送If-Modified-Since报头，询问该时间之后文件是否有被修改过：
```
If-Modified-Since : Fri , 12 May 2006 18:53:33 GMT
```
如果服务器端的资源没有变化，则自动返回 HTTP 304（Not Changed.）状态码，内容为空，这样就节省了传输数据量。当服务器端代码发生改变或者重启服务器时，则重新发出资源，返回和第一次请求时类似。从而保证不向客户端重复发出资源，也保证当服务器有变化时，客户端能够得到最新的资源。

## 浅析application/x-www-form-urlencoded和multipart/form-data的区别
我们知道在通过POST方式向服务器发送AJAX请求时最好要通过设置请求头来指定为application/x-www-form-urlencoded编码类型。知道通过表单上传文件时必须指定编码类型为"multipart/form-data"。那么为什么要这么设置呢？

在<Form>语法中，EncType表明提交数据的格式。
1. application/x-www-form-urlencoded：窗体数据被编码为名称/值对。这是标准的编码格式。
2. multipart/form-data：窗体数据被编码为一条消息，页上的每个控件对应消息中的一个部分。
3. text/plain：窗体数据以纯文本形式进行编码，其中不含任何控件或格式字符。

<Form>的enctype属性为编码方式，常用有两种： 
1. application/x-www-form-urlencoded 
2. multipart/form-data   

默认为application/x-www-form-urlencoded 。

当action为get时候，浏览器用x-www-form-urlencoded的编码方式把form数据转换成一个字串（name1=value1&name2=value2...），然后把这个字串append到url后面，用?分割，加载这个新的url。

当action为post时候，浏览器把form数据封装到http body中，然后发送到server。

如果没有 type=file 的控件，用默认的 application/x-www-form-urlencoded 就可以了。

但是如果有 type=file 的话，就要用到 multipart/form-data 了。浏览器会把整个表单以控件为单位分割，并为每个部分加上Content-Disposition(form-data或者file)、Content-Type(默认为text/plain)、name(控件name)等信息，并加上分割符(boundary)。

## 参考文档
- [MDN文档](https://developer.mozilla.org/en-US/)
- [为 Cookie 服务的首部字段（七）](https://www.jianshu.com/p/6ff91f376598)
- [百度百科-Last-Modified](https://baike.baidu.com/item/Last-Modified/15647072)
- [脚本之家-浅析application/x-www-form-urlencoded和multipart/form-data的区别](http://www.jb51.net/article/51377.htm)
- [HTTP协议头部与Keep-Alive模式详解](https://www.byvoid.com/zhs/blog/http-keep-alive-header)
- [浅谈http中的Cache-Control](https://blog.csdn.net/u012375924/article/details/82806617)
- [HTTP协议常用头部实例详解（Request、Response）](https://blog.csdn.net/selinda001/article/details/79338766)
