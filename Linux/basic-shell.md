## 第一个shell

```
echo 'hello，world'
```

shell脚本的命名一般“xxx.sh”，不使用后缀名也是允许，不过不推荐这样命名。

#### 脚本的执行

设脚本文件名为``hello.sh``

1.使用shell来执行
```
bash hello.sh
```

2.授予脚本可执行权
```
chmod +x hello.sh
```
使用chmod为脚本添加x权限，然后通过./hello.sh方法执行

## 读取参数
在shell脚本里面，$0表示为脚本名称，$1，$2，$3表示的是在执行脚本时按顺序输入的参数，而$*则表示所有输入的参数（不包括$0）。
```
echo "Script name: \"$0\""

if [ -n $1 ];then
    echo "first parameter: $1"
fi
if [ -n $2 ];then
    echo "second parameter: $2"
fi
if [ -n $3 ];then
    echo "third parameter: $3"
fi
echo "all parameter : "$*""
```
执行
```
$bash parameter.sh 1 2 3

Script name: "parameter.sh"

first parameter: 1

second parameter: 2

third parameter: 3

all parameter : 1 2 3
```

## 函数
Shell函数的定义格式 函数名 或者function+函数名

最后的hello和helloWorld表示调用函数，脚本语言要调用一个函数时，被调用的函数必须先被声明，否则调用失败。

```
hello()
{
    echo "hello"
}
function helloWorld()
{
    echo "hello world"
}

hello
helloWorld
```

## 数组
为了处理方便，通常把具有相同类型的若干变量以有序的形式组织起来。这些按顺序排序且具有
同类数据元素特征的集合称为数组（array）
shell的数组定义很简单

```
array[a]=36
declare -a province[b]=Gangdong
city[c]=zhanjiang

#输出
echo ${array[a]}
echo "my hometown is ${province[b]} ${city[c]}"
```
上面的例子输出   
36   
my hometown is Gangdong zhanjiang

### 二维数组
在shell里，虽然bash对数组元素个数没有限制，但是只支持一维数组，不过可以使用一些技巧模拟出多维数组。
```
array1="A B C"
array2="D E F"
array3="G H I"
for i in array1 array2 array3
do
    eval value=\$$i
    for j in $value
    do
        echo -e $value
        continue 2
    done
done
```

## shell脚本中的变量
在Linux操作系统下的变量通常分为环境变量和局部变量两类，系统变量一般是系统所有的变量，局部变量通常是用户自定义的变量，另外，系统中还有一种称为特殊变量的标量，这类变量通常以只读的形式存在。

### 局部变量
简单地说，局部变量（也称本地变量）就是存在生命周期的变量，被定义的局部变量只是在局部的进程中可见，也就是说只针对某段程序块有效，当进程退出时就会随之消失。

```
hello="hello world"
echo -e "variate hello is $hello"

echo -n "please input var "
read var
echo -e "variate var is $var"
```
输出
```
$ bash variate.sh

variate hello is hello world

please input var 66666666

variate var is 66666666
```
shell的变量赋值的时候不需要$，但是输出的时候需要$

shell的变量进行算术相加的时候需要带上let，不带let是字符串拼接

shell的变量不声明默认值的话，在算术相加的时候为0，在字符串拼接的时候为空。
```
i=0
i+=2
echo $i
let i+=2
echo $i
```
输出：  
```
02   
4
```

### 环境变量
为了保证系统的正常运行，Linux系统需要定义一些永久的变量，这些变量不会因为程序结束或者系统重启而消失。主要用于存储会话和工作环境的信息，例如jdk的路径，你可以通过env命令来查看。

### 特殊变量
特殊变量指某些特定值，比较常见的特殊变量是$*和$1，$2，$*表示的是当前所指的所有参数，$1,$2表示的是所输入的参数的第1，第2个参数。

```
echo "Script name: \"$0\""

if [ -n $1 ];then
    echo "first parameter: $1"
fi
if [ -n $2 ];then
    echo "second parameter: $2"
fi
if [ -n $3 ];then
    echo "third parameter: $3"
fi
echo "all parameter : "$*""
```

输出：  
```
$bash parameter.sh 1 2 3   

Script name: "parameter.sh"   
first parameter: 1  
second parameter: 2   
third parameter: 3   
all parameter : 1 2 3  
```

## 循环
### 传统风格for循环
```
for i in $(seq 1 5)
do
    echo $i
done
```
输出：1 2 3 4 5

### c语言风格for循环
```
for((i=5;i<10;i++))
do
    echo "$i"
done
```
输出：5 6 7 8 9

### 数字段形式for循环
```
for i in {1..10}
do
    echo $i
done
```
输出：1 2 3 4 5 6 7 8 9 10

## 详细列出
适用于字符且项数不多
```
for number in 1 2 3 4 5
do
    echo $number
done
```
输出：1 2 3 4 5

### while循环
```
while(( i <= 100 ))
do
    let sum+=i
    let i+=2
done
echo "sum=$sum"
```
输出：sum=2530

**while的[]语法注意两边必须有空格**
```
i=1
while [ $i -le 5 ]
do
    echo $i
    let i++
done
```
输出：1 2 3 4 5

**break 命令不执行当前循环体内break下面的语句从当前循环退出**
```
i=0
while [ $i -le 5 ]
do
    if [ $i -eq 3 ];then
        break
    fi
    echo $i
    let i++
done
```
输出：0 1 2

**continue 命令是程序在本循体内忽略下面的语句,从循环头开始执行**
```
i=0
while [ $i -le 5 ]
do
    if [ $i -eq 3 ];then
        let i++
        continue
    fi
    echo $i
    let i++
done
```
输出：0 1 2 4 5

## until循环
```
i=1
until [[ "$i" -gt 5 ]]    #当i大于5，结束循环
do
    let square=i*i
    echo "$i * $i = $square"
    let i++
done
```
输出：
```
1 * 1 = 1

2 * 2 = 4

3 * 3 = 9

4 * 4 = 16

5 * 5 = 25
```

## 条件判断
整数条件表达式，大于，小于，shell里没有> 和< ,会被当作尖括号，只有-ge,-gt,-le,lt
```
if [ 1 -ne 1 ];then
...
fi
```
这是指当1不等于1时执行then后的语句

语句 | 意义 | 英文
---|---|---
-eq|等于|equal
-ne|不等于|not equal
-le|小于等于|less and equal
-ge|大于等于|greater and equal
-lt|小于|less than
-gt|大于|greater than

-eq  -ne  -lt  -nt只能用于整数，不适用于字符串，字符串等于用赋值号=   
=放在别的地方是赋值,放在if [ ] 里就是字符串等于,shell里面没有==的,那是c语言的等于

= 作为判断等于时，其两边都必须加空格，否则失效。

= 做赋值号时正好相反，两边不能有空格

### 文件相关
语句 | 意义
---|---
if [ -f  file ] | 如果文件存在
if [ -d ...   ] | 如果目录存在
if [ -s file  ] | 如果文件存在且非空 
if [ -r file  ] | 如果文件存在且可读
if [ -w file  ] | 如果文件存在且可写
if [ -x file  ] | 如果文件存在且可执行

### 字符串判断

shell 中利用 -n 来判定字符串非空，利用 -z 来判定字符串非空。
