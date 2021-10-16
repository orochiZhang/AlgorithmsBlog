## 标准HTTP协议支持的请求方法
1. **GET** 是最常见的请求，通常是发送一个请求来取得服务器上的某一资源。服务器通过一组HTTP头和响应数据（如HTML文本，或者图片或者视频等）返回给客户端。
2. **POST** 向服务器提交数据。这个方法用途广泛，几乎目前所有的提交操作都是靠这个完成。
3. **PUT** 这个方法比较少见。HTML表单也不支持这个。本质上来讲， PUT和POST极为相似，都是向服务器发送数据，但它们之间有一个重要区别，PUT通常指定了资源，如果资源不存在则创建，存在则是更新资源。而POST则没有指定资源，POST的数据存放由服务器逻辑决定。
4. **DELETE** 表示删除某一个资源。
5. **HEAD** 和GET本质是一样的，区别在于HEAD不含有呈现数据，而仅仅是HTTP头信息。有的人可能觉得这个方法没什么用，其实不是这样的。想象一个业务情景：欲判断某个资源是否存在，我们通常使用GET，但这里用HEAD则意义更加明确。
6. **OPTIONS**  用于获取目的资源所支持的通信选项。在 CORS 中，可以使用OPTIONS方法发起一个预检请求，以检测实际请求是否可以被服务器所接受。服务器所返回的 Access-Control-Allow-Methods 首部字段将所有允许的请求方法告知客户端。该首部字段与 Allow 类似，但只能用于涉及到 CORS 的场景中。
7. **TRACE**  回显服务器收到的请求，主要用于测试或诊断。
8. **PATCH**  用于对资源进行部分修改，不同于 PUT 方法，而与 POST 方法类似，PATCH  方法是非幂等的，这就意味着连续多个的相同请求会产生不同的效果。该操作成功返回 204 状态码。
9. **CONNECT**，CONNECT方法可以开启一个客户端与所请求资源之间的双向沟通的通道。它可以用来创建隧道（tunnel）。    
例如，CONNECT 可以用来访问采用了 SSL (HTTPS)  协议的站点。客户端要求代理服务器将 TCP 连接作为通往目的主机隧道。之后该服务器会代替客户端与目的主机建立连接。连接建立好之后，代理服务器会面向客户端发送或接收 TCP 消息流。

## RESTful与4种HTTP请求
GET，POST，PUT，DELETE可以跟数据库的CRUD增删改查操作对应起来：

CRUD | HTTP请求
---|---
Create | POST
Retrieve | GET  
Update | PUT  
Delete | DELETE  

这样就实现了HTTP和数据库操作，日常CRUD业务的完美统一，这也是REST的精髓之一。GET与DELETE对应的操作是很明确的，但论及与Create和Update对应的HTTP方法时要取决于幂等性。

## HTTP的幂等性
HTTP协议本身是一种面向资源的应用层协议，但对HTTP协议的使用实际上存在着两种不同的方式：一种是RESTful的，它把HTTP当成应用层协议，比较忠实地遵守了HTTP协议的各种规定；另一种是SOA的，它并没有完全把HTTP当成应用层协议，而是把HTTP协议作为了传输层协议，然后在HTTP之上建立了自己的应用层协议。

本文所讨论的HTTP幂等性主要针对RESTful风格的。不过，幂等性并不属于特定的协议，它是分布式系统的一种特性。所以，不论是SOA还是RESTful的Web API设计都应该考虑幂等性。下面将介绍HTTP GET、DELETE、PUT、POST四种主要方法的语义和幂等性。

GET方法用于获取资源，不应有副作用，所以是幂等的。比如：``GET http://dingdingblog.com/article/1`` ，不会改变资源的状态，不论调用一次还是N次都没有副作用。请注意，这里强调的是一次和N次具有相同的副作用，而不是每次GET的结果相同。``GET http://dingdingblog.com/`` 这个HTTP请求可能会每次得到不同的结果，但它本身并没有产生任何副作用，所以GET是满足幂等性的。

DELETE方法用于删除资源，有副作用，但它应该满足幂等性。比如：``DELETE http://dingdingblog.com/article/4231`` ，调用一次和N次对系统产生的副作用是相同的，即删掉id为4231的帖子。因此，调用者可以多次调用或刷新页面而不必担心引起错误。所以DELETE是满足幂等性的。

比较容易混淆的是POST和PUT。POST和PUT的区别容易被简单地误认为“POST表示创建资源，PUT表示更新资源”。而实际上，二者均可用于创建资源，更为本质的差别是在幂等性方面。

[RFC2616](https://www.ietf.org/rfc/rfc2616)中对POST和PUT是这样定义的：
>The POST method is used to request that the origin server accept the entity enclosed in the request as a new subordinate of the resource identified by the Request-URI in the Request-Line ...... If a resource has been created on the origin server, the response SHOULD be 201 (Created) and contain an entity which describes the status of the request and refers to the new resource, and a Location header.
>
>The PUT method requests that the enclosed entity be stored under the supplied Request-URI. If the Request-URI refers to an already existing resource, the enclosed entity SHOULD be considered as a modified version of the one residing on the origin server. If the Request-URI does not point to an existing resource, and that URI is capable of being defined as a new resource by the requesting user agent, the origin server can create the resource with that URI.

POST所对应的URI并非创建的资源本身，而是资源的接收者。比如：``POST http://dingdingblog.com/article/`` 的语义是在``http://dingdingblog.com/article/`` 下创建一篇帖子，HTTP响应中应包含帖子的创建状态以及帖子的URI。两次相同的POST请求会在服务器端创建两份资源，它们具有不同的URI；所以，POST方法不具备幂等性。

PUT所对应的URI是要创建或更新的资源本身。比如``PUT http://dingdingblog.com/article/4231`` 的语义是创建或更新ID为4231的帖子。对同一URI进行多次PUT的副作用和一次PUT是相同的。因此，PUT方法具有幂等性。

## 参考文章
[理解HTTP幂等性](http://www.cnblogs.com/weidagang2046/archive/2011/06/04/2063696.html)  
[http的请求方法](http://blog.csdn.net/u010529455/article/details/42918639)   
[http协议中:GET/POST/PUT/DELETE/INPUT/TRACE/OPTIONS/ HEAD方法](http://blog.csdn.net/truong/article/details/19936541)
