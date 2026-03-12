# 代码随想录学习笔记(Python版本)

## 前言__补充内容

### 时间复杂度与空间复杂度详解__计算&表示

#### 算法效率

- 时间效率,即**时间复杂度**,衡量一个算法的<u>**运行速度**</u>	目前更加关注时间复杂度
- 空间效率,即**空间复杂度**,衡量一个算法**所需要的==额外==空间**

#### 大O的渐进表示法规则

时间复杂度和空间复杂度一般都用大O的渐进表示法来表示:

- 所有常数都用常数1表示
- 只保留最高阶项
- 如果最高阶项目存在且不是1,这去除这个项的系数,得到的结果就是大O阶

#### 时间复杂度

> 算法的时间复杂度是一个函数,定量描述了该算法的运行时间.一个算法所花费的时间与其中语句的执行次数成正比,算法中的<u>**基本操作的执行次数,为算法的时间复杂度**</u>

举例说明:

```c
//计算Func1的时间复杂度
void Func1(int N)
{
	int count = 0;
	for (int i = 0; i < 2 * N; i++)
	{
		for (int j = 0; j < 2 * N; j++)
		{
			count++;
		}
	}
	for (int k = 0; k < 2 * N; k++)
	{
		count++;
	}
}

//Func1函数执行了一个嵌套的for循环,(2N)*(2N),又执行了一个单独的for循环,2N,那么时间复杂度就是4N^2+2N,用渐进表示法,时间复杂度表示为O(N^2)
```

```c
//计算Func2的时间复杂度
void Func2(int N)
{
	int count = 0;
	for (int k = 0; k < 100; k++)
	{
		++count;
	}
	printf("%d\n", count);
}

//Func2函数内部执行了一个for循环(共100次),Func2函数内语句的执行次数不会随着传入的变量N的改变而改变,即执行的次数为常数次,时间复杂度表示为O(1)

//注:在刷题时看到题目要求时间复杂度为O(1)，并不是要求函数内部不能含有循环，而是要求循环的次数为常数次
```

```c
//计算二分查找函数的时间复杂度

//int* a表示定义了一个指向int类型数据的指针变量,变量名为a,int*表示该指针只能指向int类型的内存空间		a是指针变量本身,不存储具体数值,而是一个内存地址
//int* a用来接收外部传入的int类型数组的首地址,通过这个指针可以访问数组中的所有元素
//a不是数组,是一个保存了数组首地址的指针变量,a[mid]等价于*(a+mid),通过指针偏移访问数组元素
int BinarySearch(int* a, int N, int x)
{
    //断言,用于调试阶段的参数合法性检查,assert()判断若为真则程序正常执行
	//assert(a)是为了防止传入空指针NULL
    assert(a);
	int begin = 0;
	int end = N - 1;
	while (begin <= end)//左右索引,左闭右闭区间
	{
		//定义整型变量mid,用于存储当前查找空间的中间位置索引
        int mid = begin + ((end - begin) >> 1);//右移1位,x>>1等价于x/2,整除运算
		if (x > a[mid])
			begin = mid + 1;
		else if (x < a[mid])
			end = mid - 1;
		else
			return mid;
	}
	return -1;
}

//用二分查找法查找数据时,查一次可以筛去一半的数据,经过一次次筛选最后待查数据只剩下一个,此时查找的次数就是while循环执行的次数.	举例来讲:第1️⃣次while,剩下N/2个元素;第2️⃣次while,剩下N/4个元素…… 那么当剩下一个元素时,有N/2^x=1,即2^x=N,那么取对数有x=logN(底数为2,打不出来),那么时间复杂度为O(logN)

//在表示时间和空间复杂度时,log表示以2为底的对数
```

```c
//计算斐波那契函数的时间复杂度
int Fibonacci1(int N)
{
	if (N == 0||N == 1)
		return 1;
	else
		return Fibonacci1(N - 1) + Fibonacci1(N - 2);
}

```

使用递归法求斐波那契数,需要知道前两个斐波那契数并相加得出.那么当我们要知道第N个斐波那契数时,递归的次数如下图:

![img](https://i-blog.csdnimg.cn/blog_migrate/02b8aec0d532f0c048840abcdf9771c9.png)

右下角的递归函数会提前结束,因此图中三角形一定有一块是无数据的,不过当N趋于无穷时,缺失数据的一小块可以忽略不计,因此总计调用斐波那契函数的次数为:
$$
2^0 + 2^1 + \dots + 2^{N-1}
$$
利用等比数列求和公式得到最后结果为$2^N-1$
保留最高阶项后,用大O的渐进表示法表示斐波那契函数的时间复杂度为O($2^N$)

用F(6)为例,把**递归次数图**拆成**逐层调用结构**,斐波那契递归的终止条件是`F(0)=0`、`F(1)=1`,遇到这两个值时不会再拆分出下一层调用,整一个递归的公式为`F(n)=F(n-1)+F(n-2)`

```plain
（0层）          F(6)                  → 1次（初始调用）
                 ↓ （拆为F(5)+F(4)）
（1层）    F(5)      F(4)              → 2次
           ↓         ↓ （各拆为两个子函数）
（2层） F(4)  F(3)  F(3)  F(2)        → 4次
        ↓     ↓     ↓     ↓ （F(2)继续拆分，不终止）
（3层）F(3) F(2) F(2) F(1) F(2) F(1) F(1) F(0)  → 8次（本层满额，无空缺）
       ↓    ↓    ↓  （终止）    ↓（终止）（终止）（终止）
（4层）F(2) F(1) F(1) F(0) F(1) F(0) F(1) F(0)  → 16次（前半部分拆分，后半部分多为终止值）
      ↓    （终止）（终止）（终止）（终止）（终止）（终止）（终止）
（5层）F(1) F(0)                       → 32次（本应满额，实际只剩2次，其余均为终止值
     （终止）（终止）
```

普通递归函数有**无记忆性**,不会保存之前计算过的子问题结果,每次调用都要重复计算
**无数据块**部分用一个例子距离如下图便可知

![694a59021812a73fd3c1c351fcbc3939](../Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/wxid_ifah8k667t3r22_d520/temp/RWTemp/2026-01/9e20f478899dc29eb19741386f9343c8/694a59021812a73fd3c1c351fcbc3939.png)

**递归算法的时间复杂度 = 递归的次数 x 每次递归函数中的次数**
递归的次数:整个过程中,函数被调用的总次数
每次递归函数中的次数:指每调用一次斐波那契函数,里面执行的基本操作有多少,比如在这里(普通递归的斐波那契函数里),只是作“判断终止条件+调用两个子函数”,这些操作都是常数次(可以看作一次)

#### 空间复杂度

> 空间复杂度是对一个算法在运行过程中临时占用存储空间大小的量度.空间复杂度不是程序占用了多少字节的空间,而是**<u>*计算变量的个数*</u>**,用大O渐进表示法

```c
//计算冒泡排序函数的空间复杂度
//对整型数组升序排列,通过相邻元素的两两比较与交换,将当前未排序区间中的最大元素逐步冒泡到其最终应在的位置(数组末尾方向),并通过交换标志位减少不必要的排序轮次,提升效率
void BubbleSort(int* a, int N)
{
	assert(a);//检查指针a是否非空
	for (int i = 0; i < N; i++)//i表示已经完成排序的元素个数
	{
		int exchange = 0;//exchange是优化用的交换标志位.初始化为0,表示当前排序轮次尚未发生任何元素交换,用于判断数组是否已经提前有序,避免无效的排序轮次
		//内层循环遍历当前未排序区间,通过相邻元素比较交换,将未排序区间的最大元素冒泡到末尾
        //N-1避免数组越界,因为要访问a[j + 1],j最大值只能为N-2,否则将超出数组下标范围
        //-i,减去已完成排序的元素个数i,这些元素位于数组末尾,无需遍历比较,减少无效操作
        for (int j = 0; j < N - 1 - i; j++)
		{
			if (a[j]>a[j + 1])
			{
				//借助临时变量tmp完成交换,不能直接a[j] = a[j+1]; a[j+1] = a[j],否则会覆盖丢失原始数据,tmp作为中转保存a[j]的原始值
                int tmp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = tmp;
				exchange = 1;//交换发生后标志位置为1,表示当前轮次发生了元素交换,数组尚未完全有序
			}
		}
        //当某一轮内层循环执行完毕后,exchange仍为0则说明这一轮遍历未排序区间时没有发生任何一次元素交换,那么整个数组已经处于有序状态
		if (exchange == 0)
			break;//直接break跳出外层循坏,无需执行后续的排序轮次
	}
}

//这段代码中声明的额外变量仅有:i、exchange、j、tmp,这些变量的个数是固定常数，不随输入数据规模N（数组元素个数）的变化而变化...冒泡排序函数中使用了常数个额外空间（即常数个变量），所以用大O的渐进表示法表示冒泡排序函数的空间复杂度为O(1) 
```

```c
//计算阶乘递归函数的空间复杂度
long long Factorial(size_t N)
{
	//三元运算符表达式
    return N < 2 ? N : Factorial(N - 1)*N;
}

//上面的return ……语句可以等价于下面的if——else逻辑,包含递归的终止和递推
if (N < 2) {
    return N;
} else {
    return Factorial(N - 1) * N;
}

//空间复杂度衡量算法运行过程中额外占用的存储空间,对于递归算法,除了局部变量占用的空间还必须记入 程序调用栈的栈帧空间 (这是递归的额外开销)
//程序调用栈的工作机制:每次调用函数时,系统会在栈上创建一个栈帧,用于保存该函数的局部变量、返回地址、参数等信息,函数执行完毕(返回结果)后,对应的栈帧会被释放
//递归调用的深度等于栈帧的数量,本例中当N=5时,递归调用流程是Factorial(5) → Factorial(4) → Factorial(3) → Factorial(2) → Factorial(1)，未到达终止条件前，栈上同时存在5个栈帧，递归深度为N（更准确地说，递归深度与N成正比）
//单个栈帧空间:本例函数内部没有声明额外的大规模变量,只包含参数N和返回值相关信息,单个栈帧占用的存储空间是常数级O(1)
//总额外空间:栈帧数量为O(N)，单个栈帧空间为O(1)，因此总额外存储空间随N的增大而线性增长。
```

---

## 数组 

### 数组理论基础

**数组**是存放在**连续内存空间**上的**相同类型数据**的**<u>集合</u>**

数组可以通过下标索引的方式获取到下标对应的数据

<img src="https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%84.png" alt="算法通关数组" style="display: block; margin: 0 auto; width: 600px;">

上图是一个字符数组的例子,有两点需要注意:

- 数组下标是从0开始的;
- 数组内存空间的地址是连续的

**数组在内存空间的地址是连续的**,所以在**删除或者增添元素**的时候,难免要**移动其他元素的地址**

例如删除下标为3的元素,需要对下标为3的元素后面的所有元素都做移动操作

<img src="https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%841.png" alt="算法通关数组" style="display: block; margin: 0 auto; width: 600px;">

数组的元素是不能删的,**只能覆盖**

> 数组在内存里是连续、固定长度的存储空间,一旦创建则所占内存大小就固定了
>
> 数组的内存空间是固定的,没法真的移除某块内存里的元素,所谓“删除”指的是用后面的元素覆盖掉这个位置的内容
>
> 因此,数组的元素是不能删的,只能采用覆盖+移动元素位置这种“假删除”

![20240606105522](https://file1.kamacoder.com/i/algo/20240606105522.png)

**C++中二维数组在内存的空间地址是连续分布的**,不过不同语言的内存管理是不一样的

```c++
void test_arr() {
    int array[2][3] = {
		{0, 1, 2},
		{3, 4, 5}
    };
    cout << &array[0][0] << " " << &array[0][1] << " " << &array[0][2] << endl;
    cout << &array[1][0] << " " << &array[1][1] << " " << &array[1][2] << endl;
}

int main() {
    test_arr();
}

//测试结果
0x7ffee4065820 0x7ffee4065824 0x7ffee4065828
0x7ffee406582c 0x7ffee4065830 0x7ffee4065834
```

地址是16进制的,因此可以看出来二维数组地址是连续一条线的
`` 0x7ffee4065820 `与 `0x7ffee4065824 `差了一个4，就是4个字节，因为这是一个int型的数组，所以两个相邻数组元素地址差4个字节

### 二分查找

[力扣原题](https://leetcode.cn/problems/binary-search/description/)

```plain
#题目

给定一个含n个元素的有序（升序）整型数组nums和一个目标值target，写一个函数搜索nums中的target，如果目标值存在返回下标，否则返回-1。

#提示:
假设 nums 中的所有元素是不重复的
```

#### 思路

题目的前提是数组为有序的升序数组,同时强调数组中无重复元素.➡️**“二分法“**

二分法查找涉及很多**边界条件**,主要是对**区间的定义**,区间的定义就是**==不变量==**.要在二分查找中保持不变量,就要在`while` 循环中的每一次边界的处理都要坚持**根据区间的定义来操作**,即**循环不变量规则**

二分法的区间定义一般为	**左闭右闭**即[left, right]，或者**左闭右开**即[left, right)

**/通过一次次更新边界来缩小查找范围/**

#### 二分法NO.1

定义target在一个左闭右闭的区间内,也就是**[left,right]**

既然是左闭右闭的区间,那么有两点很重要:

- `while(left <= right)`要使用 <= ,因为`left == right`是有意义的
- `if(nums[middle] > target)`时,说明数组的中间位置值都大于目标值了,那么需要更新**右边界(即`right`)**,此时`right`应该赋值为`middle-1`(因为右闭,`middle`值已经大于target了就没必要继续包含它)

此外,对于`middle`取值做一个解释:`middle = (left + right)/2`只保留整数部分.其中`left = 0,right = nums.size()-1`.right的值应该根据左闭右闭or左闭右开作动态调整,这里的是左闭右闭的取值

- 假设数组中有奇数个元素,那么`middle`刚好是中间那个数字
- 假设数组中有偶数个元素,那么`middle`是中间两个数字中的左边那个

例如在数组：1,2,3,4,7,9,10中查找元素2，如图所示：

![20210311153055723](https://file1.kamacoder.com/i/algo/20210311153055723.jpg)

#### 二分法NO.2

当定义target在一个左闭右开的区间,即[left,right),二分法的边界处理方式截然不同:

- `while (left < right)`，这里使用 < ,因为`left == right`在区间[left, right)是没有意义的
- `if (nums[middle] > target)`时,right应该更新为`middle`，因为当前nums[middle]大于target，说明target在左区间，而寻找区间是左闭右开区间，所以right更新为middle，即下一个查询区间不会去比较nums[middle]

在数组：1,2,3,4,7,9,10中查找元素2，如图所示：（**注意和方法一的区别**）

![20210311153123632](https://file1.kamacoder.com/i/algo/20210311153123632.jpg)

二分法的重点在于对于区间的定义,在循环中要始终坚持**根据查找区间的定义来做边界处理**

区间的定义就是不变量,在循环中坚持根据查找区间的定义来做边界处理

```python
#二分法Python代码

#方法一
class Solution:
    def search(self,nums:List[int],target:int)-->int:
		left,right = 0,len(nums) - 1	#定义target在左闭右闭区间
        
        while left <= right:
			middle = left + (right - left) //2	#整除
            
            if nums[middle] > target:
                right = middle -1	#target在左区间,所以[left,middle-1]
            elif nums[middle] < target:
                left = middle + 1	#target在右区间,所以[middle+1,right]
            else:	
                return middle	#target值与middle值相等,返回下标值middle
        return -1	#没有在数组中找到与target相等的值,但在循环结束后才能返回-1
    
    
#方法二
class Solution:
    def search(self,nums:List[int],target:int)-->int:
		left,right = 0,len(nums)	#定义target在左闭右开区间,反正右边是开区间,直接取len(nums)即可
        
        while left < right:		#定义左闭右开区间
			middle = left + (right - left) //2	#整除
            
            if nums[middle] > target:
                right = middle	#target在左区间,所以[left,middle)
            elif nums[middle] < target:
                left = middle + 1	#target在右区间,所以[middle+1,right)
            else:	
                return middle	#target值与middle值相等,返回下标值middle
        return -1	#没有在数组中找到与target相等的值,但在循环结束后才能返回-1
```

### 移除元素

[力扣原题](https://leetcode.cn/problems/remove-element/description/)

```plain
#题目

给你一个数组nums和一个值val，你需要 **原地** 移除所有数值等于val的元素，并返回移除后数组的新长度

不要使用额外的数组空间，你必须仅使用O(1)额外空间并 **原地修改** 输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
```

**数组的元素在内存地址中是==连续==的,不能单独删除数组中的某个元素,只能*<u>移动+覆盖</u>***

#### 暴力解法

暴力解法是两层for循环,第一个for循环**遍历数组元素**,第二个for循环**更新数组**

![27.移除元素-暴力解法](https://file1.kamacoder.com/i/algo/27.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0-%E6%9A%B4%E5%8A%9B%E8%A7%A3%E6%B3%95.gif)

暴力解法的时间复杂度是O(n^2^),空间复杂度是O(1)

```python
#暴力解法,两层for循环
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,l = 0,len(nums)
        while i<l:
            if nums[i] == val:# 找到等于目标值的节点
                for j in range(i+1,l):# 移除该元素，并将后面元素向前平移,py的range左闭右开
                    nums[j - 1] = nums[j]
                l -= 1#数组的有效长度-1,通过平移覆盖了一个目标值val,末尾多出一个重复的无效元素
                i -= 1#当前索引i处的元素被后面的元素覆盖了,新的nums[i]是原来的nums[i+1],这个元素还没判断过是否等于val,所以需要i-=1
            i += 1#用于下次while循环中去重新判断索引i的新元素
        return l#l用于记录有效元素的长度,即移除val后的数组有效元素个数
#以上例说明,初始数组[0,1,2,3,3,0,4,2],val=2,当i=2时,原来的nums[2]被替换为nums[3]=3,更新为[0,1,3,3,0,4,2,2],l=7(数组有效长度),如果if语句中不减1,则下一次while中,i=3,直接跳过了nums[2]=3这个数没有被判断是否为val;如果if语句外的i不自增的话,循环就没法继续了
```

#### 双指针法

双指针法(快慢指针法):通过一个**快指针**和**慢指针**在一个**for循环**下完成两个for循环的工作

定义快慢指针

- 快指针`fastIndex`：寻找新数组的元素 ，新数组就是不含有目标元素的数组
- 慢指针`slowIndex`：指向**更新**新数组下标的位置

![img](https://file1.kamacoder.com/i/algo/27.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0-%E5%8F%8C%E6%8C%87%E9%92%88%E6%B3%95.gif)

**双指针法**在数组和链表的操作中是非常常见的,很多考察数组、链表和字符串的面试题都使用了**双指针法**

双指针法的时间复杂度是O(n),空间复杂度是O(1)

```python
#双指针法

##快慢指针法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:# 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1#把slow放在if语句内,就是为了在fast指针找到val时,停止更新新的数组下标,if语句外的fast则继续下一个值的检索匹配
			fast += 1
		return slow
    
##相向双指针法	注意边界控制条件left<=right
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right  = 0, n - 1#左指针找需要被移除的目标值,右指针找可以用来替换的非目标值
        #利用右指针的好元素覆盖左指针的坏元素,将所有非目标元素保留在数组的前半部分
        while left <= right:#左右指针还未交叉则继续处理数组元素
            #left <= right用于防止指针(数组索引)越界(比如右指针已经左移,这左指针不能超过右指针),举例说明:nums = [2,2,2]，val = 3,那么因为所有元素都不为val值,所以left会一直加1,从0→1→2→3→4...,当left=3时,访问nums[3]会超出数组索引范围(数组最大索引是2),直接报错
            #left一直自增直到while语句的条件不成立为止,左指针跳过所有非目标值,停留在val上
            while left <= right and nums[left] != val:
                left += 1
            #right一直自减直到while语句的条件不成立为止,右指针跳过所有目标值,停留在非目标值上
            while left <= right and nums[right] == val:
                right -= 1
            #替换操作:用好元素覆盖坏元素
            if left < right:#这里left是找到的第一个val值的下标索引,right则是找到的第一个非val值的下标索引,完成替换更新后需要跳过更新后的下标索引(已经更新过了,再次查找时不能再从这里开始查)
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left
```

### 有序数组的平方

[力扣原题](https://leetcode.cn/problems/squares-of-a-sorted-array/)

```plain
#题目

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序
```

#### 暴力排序

最简单的想法就是对每个数平方后排序

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list = [i*i for i in nums]#列表生成式
        list.sort()#升序排列
        return list
    
#也可以直接一行搞定	return sorted(x*x for x in nums)
```

这个时间复杂度是 O(n + nlogn)，列表生成式需要遍历`nums`中的每一个元素,遍历次数n;列表内置的`sort()`方法的时间复杂度为O( nlogn);当n足够大时,高阶复杂度会主导整体性能,低阶复杂度O(n)可以被忽略,因此总时间复杂度为O( nlogn)

#### 双指针法

数组是有序的,只是负数平方之后可成为最大数

数组平方的最大值就在**==数组的两端(绝对值最大)==**➡️可以考虑**双指针法**,i指向起点,j指向终点

定义一个新数组`result`,和A数组一样的大小,让k指向`result`数组终止位置

如果`A[i] * A[i] < A[j] * A[j]` 那么`result[k--] = A[j] * A[j];` 。

如果`A[i] * A[i] >= A[j] * A[j]` 那么`result[k--] = A[i] * A[i];` 。

如动画所示：

![img](https://file1.kamacoder.com/i/algo/977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.gif)

```python
#双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        #提前创建一个长度与nums相同的固定长度列表
        #float(‘inf’)表示无穷大,这里用作初始化值,只是为了填充列表的初始空间,后续会被所有平方值完全覆盖,也可以用res = [0] * len(nums),float('inf')只是一种常见的占位符写法
        res = [float('inf')] * len(nums)
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: #左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res
#疑问:如果刚好是(-5)^2和5^2怎么办?
#解答:无影响,假设把最右边的数平方后当作最大值存储,那么右指针左移一位,左指针保留原位,下一次循环比较时,最左边的数平方后一定为最大值(之一),接下来按序操作即可
    
#双指针法 加 反转列表
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #根据list的先进排序在先原则
        #将nums的平方按从大到小的顺序添加进新的list
        #最后反转list
        new_list = []
        left, right = 0 , len(nums) -1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                new_list.append(nums[right] ** 2)
                right -= 1
            else:
                new_list.append(nums[left] ** 2)
                left += 1
        return new_list[::-1]

#双指针法优化版本
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        整体思想：有序数组的绝对值最大值永远在两头，比较两头，平方大的插到新数组的最后
        优   化：1. 优化所有元素为非正或非负的情况
                2. 头尾平方的大小比较直接将头尾相加与0进行比较即可
                3. 新的平方排序数组的插入索引可以用倒序插入实现（针对for循环，while循环不适用）
        """
 
        # 特殊情况, 元素都非负（优化1）
        if nums[0] >= 0:
            return [num ** 2 for num in nums]  # 按顺序平方即可
        # 最后一个非正，全负有序的
        if nums[-1] <= 0:
            return [x ** 2 for x in nums[::-1]]  # 倒序平方后的数组
        
        # 一般情况, 有正有负
        i = 0  # 原数组头索引
        j = len(nums) - 1  # 原数组尾部索引
        new_nums = [0] * len(nums)  # 新建一个等长数组用于保存排序后的结果
        # end_index = len(nums) - 1  # 新的排序数组(是新数组)尾插索引, 每次需要减一（优化3优化了）

        # (优化3，倒序，不用单独创建变量)
        #range(start,end,step),左闭右开原则
        for end_index in range(len(nums)-1, -1, -1): 
            # if nums[i] ** 2 >= nums[j] ** 2:
            if nums[i] + nums[j] <= 0:  # (优化2),说明nums[i]绝对值更大
                new_nums[end_index] = nums[i] ** 2
                i += 1
                # end_index -= 1  (优化3)
            else:
                new_nums[end_index] = nums[j] ** 2
                j -= 1
                # end_index -= 1  (优化3)
        return new_nums
```

时间复杂度为O(n)，相对于暴力排序的解法O(n + nlog n)提升了不少

### 长度最小的子数组

[力扣原题](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

```plain
#原题
给定一个含有n个正整数的数组和一个正整数s，找出该数组中满足其和≥s的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回0。
```

#### 滑动窗口

滑动窗口,就是**不断调节子序列的起始位置和终止位置**,从而得出理想的结果

本题可以用暴力解法,**第一个for循环滑动窗口的起始位置**,**第二个for循环为滑动窗口的终止位置**,用两个for循环能完成一个不断搜索区间的过程

滑动窗口用一个for循环就能实现暴力解法的流程,如果只用一个for循环来表示滑动窗口的起始位置,无法遍历剩下的终止位置,所以要**用for循环来表示滑动窗口的终止位置**

滑动窗口的起始位置如何移动,举例说明:

![209.长度最小的子数组](https://file1.kamacoder.com/i/algo/209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.gif)

可以看出来滑动窗口也是双指针法的一种!

在本题中实现滑动窗口,需要确定如下三点:

- **窗口**:满足窗口内所有元素的和大于等于s的长度最小的连续子数组
- **窗口的起始位置移动规则**:如果当前窗口的值大于等于s了,则窗口要向前移动
- **窗口的结束位置移动规则**:窗口的结束位置就是遍历数组的指针,即for循环里的索引

解题关键在于**窗口起始位置如何移动**:

![leetcode_209](https://file1.kamacoder.com/i/algo/20210312160441942.png)

**滑动窗口的精妙之处在于根据当前子序列和大小的情况，不断调节子序列的起始位置。从而将O(n^2)暴力解法降为O(n)**

```python
#暴力解法
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        length_list = []
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                if current_sum >= target:
                    sun_len = j-i+1
                    length_list.append(sun_len)
                    break
        return min(length_list) if length_list else 0

#学习人家的代码:
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        min_len = float('inf')
        
        for i in range(l):
            cur_sum = 0
            for j in range(i, l):
                cur_sum += nums[j]
                if cur_sum >= s:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return min_len if min_len != float('inf') else 0
```

```python
#滑动窗口法
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            #只要目前和小于目标值,则一直不进入内层循环,right加了很多次,left不变,一直保持为0(没进入while语句,left值不变)
            #内层while:对每个right持续收缩left到当前right结尾的最短子数组
            while cur_sum >= s: # 当前累加值大于目标值,确保左边界收缩到最小
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1#执行完一遍后再去比较现在的目前和与s大小关系,如果还是大于等于,则要再执行一遍while语句块,直到退出条件(目标就是去寻找最小的窗口长度)
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
```

时间复杂度O(n),空间复杂度O(1),每个元素在滑动窗后进来操作一次，出去操作一次，每个元素都是被操作两次，所以时间复杂度是 2 × n 也就是O(n)

> 时间复杂度的详解:
>
> 滑动窗口:两个`while`中的`left`和`right`都是单向移动且从不回头,**数组中的每个元素，只会被`right`指针访问一次，也只会被`left`指针访问一次**,没有任何元素被重复处理
>
> 暴力解法:两层`for`循环中的内层指针会重复回头,重新遍历
> 暴力解法的外层`i`从左往右走，内层`j`每次都要从`i`开始重新遍历（从左往右走到数组末尾），相当于前面已经处理过的元素，会被后续的`i`对应的`j`再次遍历，存在大量重复访问
>
> 以nums=[2,3,1,2,4,3]为例子,滑动窗口的执行次数为12次,暴力解法为6+5+4+3+2+1=21次,对应数学公式n(n+1)/2

### 螺旋矩阵II

[力扣原题](https://leetcode.cn/problems/spiral-matrix-ii/description/)

```plain
#题目

给定一个正整数n,生成一个包含1到n^2的所有元素,且元素按顺时针顺序螺旋排列的正方形矩阵
```

#### 思路

坚持遵守**循环不变量**的原则

模拟顺时针画矩阵的过程:

- 上行从左到右
- 右列从上到下
- 下行从右到左
- 左列从下到上

由外向内一圈圈画下去,但能发现这里有许多**边界条件**,在一个循环中如此多的边界条件,如果不按照固定规则来遍历,那就回陷入到循环陷阱中

这里一圈下来需要画四条边,在画每一条边时都要坚持一致的**左闭右开**or**左开右闭**的原则,这样子一圈才能按照统一的规则画下来

> 用左闭右开的原则画一圈作为示例:

![img](https://file1.kamacoder.com/i/algo/20220922102236.png)

每一种颜色代表了一条边,在每一个拐角处,都让给新的一条边来画==(即坚持**左闭右开**的原则)==

```python
#版本1

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]	#初始化一个nxn的全0矩阵,作为最终填充螺旋数字的容器
        startx, starty = 0, 0               # 起始点
        loop, mid = n // 2, n // 2          # 迭代次数、n为奇数时，矩阵的中心点
        count = 1                           # 计数

        #offset为偏移量,控制当前层的边界范围,循坏表示对应填充为第一层至第loop层循环
        for offset in range(1, loop + 1) :      # 每循环一层偏移量加1，偏移量从1开始
            #始终保持为左闭右开的循环不变量准则
            #上行从左至右,列数变化,行数保持不变,变量为列值
            for i in range(starty, n - offset) :    
                nums[startx][i] = count
                count += 1
            #右列从上至下,列数已经指向当前循环下的最后一列n-offset,行数值为递增变量
            for i in range(startx, n - offset) : 
                nums[i][n - offset] = count
                count += 1
            #下行从右至左,行数已经指向当前循环下的最后一行n-offset,列数值为递减变量
            for i in range(n - offset, starty, -1) :
                nums[n - offset][i] = count
                count += 1
            #左列从下至上,列数已经指向当前循环下的起始列,行数值为递减变量
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1                
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count 
        return nums
    
    
#版本2:定义四个边界

class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []
        
        # 初始化 n x n 矩阵
        matrix = [[0]*n for _ in range(n)]

        # 初始化边界和起始值
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1

        #while循环的条件判断只在进入循环体之前执行一次,只要进入了while循环体就会按照顺序完整执行完当前迭代的所有for循环和对应的自增操作
        while top <= bottom and left <= right:
            # 从左到右填充上边界
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 从上到下填充右边界
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 从右到左填充下边界

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # 从下到上填充左边界

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix
```

- 时间复杂度O(n^2^):模拟遍历二维矩阵的时间
- 空间复杂度O(1)

### 区间和

[原题链接](https://kamacoder.com/problempage.php?pid=1070)

```plain
#题目

给定一个整数数组 Array，请计算该数组在每个 指定区间内 元素的总和。
第一行输入为整数数组Array的长度n,接下来n行中,每行一个整数,表示数组的元素.随后的输入为需要计算总和的区间,直至文件结束
输出每个指定区间内元素的总和

#示例
IN
5
1
2
3
4
5
0 1
1 3

OUTPUT
3
9
```

下面先给出最常规的解法
给一个区间,把这个区间的和都累加一遍

```c++
#include <iostream>		 // 引入输入输出流头文件，支持cin（输入）、cout（输出）操作
#include <vector>		// 引入vector容器头文件，用于存储动态数组
using namespace std;	// 使用std命名空间，避免每次写std::cin/std::cout等前缀
int main() {
    int n, a, b;	// 定义3个整型变量：n（数组长度）、a/b（区间端点）
    cin >> n;		// 从控制台读取n的值
    vector<int> vec(n);		// 创建一个长度为n的int类型vector，初始值默认全为0
    // 循环n次，读取n个整数并依次存入vec的0~n-1索引位置
    for (int i = 0; i < n; i++) cin >> vec[i];
    // 循环读取a和b：只要输入的是两个有效整数，就进入循环体；输入无效则终止循环
    while (cin >> a >> b) {
        int sum = 0;
        // 遍历索引a到b（包含），累加对应元素到sum
        for (int i = a; i <= b; i++) sum += vec[i];
        cout << sum << endl;	// 输出累加和并换行
    }
    // 注：C++11后main函数可省略return 0，编译器会自动补全，代表程序正常结束
}

//读取一个整数n,接着读取n个整数存入长度为n的vector容器
//循环读取两个整数a,b(表示数组的区间端点),计算并输出容器中索引从a到b的所有元素的累加和
//知道输入流结束,程序停止循环并结束
```

当查询次数非常大时,比如查询m次,每一次查询的范围都是从0到n-1,则该算法的时间复杂度是O(n*m)

可以通过引入**==前缀和==**的方法来解决

前缀和:**重复利用计算过的子数组之和**,从而降低区间查询需要累加计算的次数

**前缀和**在涉及**计算区间和的问题**时非常有用

举个例子
统计vec[i]这个数组上的区间和,可以先做累加,即p[i]表示下标从0到i的vec[i]累加之和

![img](https://file1.kamacoder.com/i/algo/20240627110604.png)

如果我们想统计vec数组上下标2到下标5之间的累加和,那么就可以用p[5]-p[1]来解决

```plain
p[1] = vec[0] + vec[1];
p[5] = vec[0] + vec[1] + vec[2] + vec[3] + vec[4] + vec[5];
p[5] - p[1] = vec[2] + vec[3] + vec[4] + vec[5];
```

![img](https://file1.kamacoder.com/i/algo/20240627111319.png)

`p[5]-p[1]`就是红色部分的区间和

p数组是之前就计算好的累加和,所以后面每次求区间和的之后只需要O(1)的操作

> 在使用前缀和求解的时候要特别注意求解区间

```python
#读取终端输入的数组长度n、数组元素以及多组区间查询(每组包含a和b),通过构建前缀和数组快速计算每个区间[a,b]的元素累加和,最终批量输出所有查询结果
#核心优化逻辑是前缀和将区间和查询的时间复杂度从 O (n) 降为 O (1)

import sys	#导入系统模块,提供了与系统交互的接口,这里用于读取标准输入(终端输入)
input = sys.stdin.read	#stdin.read()方法读取终端输入,把函数本身赋值给input,后续调用input()等价于调用sys.stdin.read(),一次性读取终端所有输入内容,直到收到EOF信号（macOS/Linux 按 Ctrl+D，Windows 按 Ctrl+Z）

def main():
    #input()调用赋值后的input变量,一次性读取终端所有输入并返回一个字符串
    #.split()将读取到的字符串按任意空白字符(空格、换行、制表符)分割成字符串列表
    #data用于存储分割后的字符串列表,后续会将其转为整数解析
    data = input().split()
    #定义索引变量,用于遍历data列表,初始指向第一个元素(数组长度)
    index = 0
    #将data的第0个元素从字符串转换为整数,作为数组的长度
    n = int(data[index])
    #索引后移1位,准备读取数组元素
    index += 1
    #初始化空列表,用于存储目标数组的元素
    vec = []
    for i in range(n):
        vec.append(int(data[index + i]))
    #索引后移n位,指向数组元素后的第一个位置(即查询区间的起始位置)
    index += n

    #构建前缀后数组p
    p = [0] * n#初始化长度为n的前缀和数组
    presum = 0#定义累加变量,用于逐步计算前缀
    for i in range(n):
        presum += vec[i]
        p[i] = presum

    #处理多组区间查询并计算和
    results = []
    while index < len(data):#只要索引未遍历完data（还有查询区间），就持续处理
        a = int(data[index])#读取当前索引的元素作为区间左端点 a
        b = int(data[index + 1])#读取下一个索引的元素作为区间右端点 b
        index += 2#索引后移2为,准备读取下一组查询(每组查询占2个元素)

        if a == 0:
            sum_value = p[b]
        else:
            sum_value = p[b] - p[a - 1]

        results.append(sum_value)

    #批量输出所有查询结果,遍历results列表,逐个输出每个查询的区间和(每行一个结果)
    for result in results:
        print(result)

#定义标准程序入口
if __name__ == "__main__":
    main()
```

### 开发商购买土地

[原题链接](https://kamacoder.com/problempage.php?pid=1044)

```plain
#题目

在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。
现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。
然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。
为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。
注意：区块不可再分。

输入描述
第一行输入两个正整数，代表 n 和 m。
接下来的 n 行，每行输出 m 个正整数。

输出描述
请输出一个整数，代表两个子区域内土地总价值之间的最小差距。

例如,输入3 3 1 2 3 2 1 3 1 2 3,输出0
如果将区域按照如下方式划分：
1 2 | 3 2 1 | 3 1 2 | 3
两个子区域内土地总价值之间的最小差距可以达到 0。
```

#### 思路

暴力求解:一个for枚举分割线,嵌套两个for去累加区间里的和

如果本题要求任何两个行/列之间的数值总和,可以在上题`区间和`的基础上求解

依然是**前缀和**的思路,先统计好前n行的和q[n],如果要求矩阵a行到b行之间的总和,用q[b]-q[a-1]即可	使用前缀和要注意区间左右边的开闭情况

```python
#前缀和

import sys
input = sys.stdin.read
    
def main():
    data = input().split()#变成字符串列表

    #提取前两位作为n和m,表示输入应为nxm的矩阵
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1#指向第三个元素,表示接下来开始构造nxm矩阵
    
    sum = 0
    vec = []#创建空列表,用于存储矩阵元素
    for i in range(n):
        row = []#行空列表
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            sum += num#矩阵元素求和
        vec.append(row)#每一个i的for循环遍历完j的for循环后添加这一行元素,构造矩阵

    # 统计横向
    horizontal = [0] * n
    for i in range(n):
        for j in range(m):
            horizontal[i] += vec[i][j]

    # 统计纵向
    vertical = [0] * m
    for j in range(m):
        for i in range(n):
            vertical[j] += vec[i][j]

    result = float('inf')
    horizontalCut = 0
    for i in range(n):
        horizontalCut += horizontal[i]
        result = min(result, abs(sum - 2 * horizontalCut))#关键处理

    verticalCut = 0
    for j in range(m):
        verticalCut += vertical[j]
        result = min(result, abs(sum - 2 * verticalCut))

    print(result)

if __name__ == "__main__":
    main()

```

本题还可以在暴力求解下优化,即可放弃前缀和,在行向遍历的时候遇到行末尾就统计一下(列也如此)

```python
#优化暴力

import sys
input = sys.stdin.read

def main():
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    sum = 0
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            sum += num
        vec.append(row)

    result = float('inf')
    
    count = 0
    # 行切分
    for i in range(n):
        
        for j in range(m):
            count += vec[i][j]
            # 遍历到行末尾时候开始统计
            if j == m - 1:
                result = min(result, abs(sum - 2 * count))

    count = 0
    # 列切分
    for j in range(m):
        
        for i in range(n):
            count += vec[i][j]
            # 遍历到列末尾时候开始统计
            if i == n - 1:
                result = min(result, abs(sum - 2 * count))

    print(result)

if __name__ == "__main__":
    main()

```

优化暴力和前缀和解法的时间复杂度均为O(n^2^)

### 数组__总结

#### 数组理论基础

**数组是存放在连续内存空间上的相同类型数据的集合**

数组可以方便的通过下标索引的方式获取到下标对应的数据

![img](https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%84.png)

上图是一个字符数组的例子,需要注意:

- **数组下标都是从0开始的**
- **数组内存空间的地址是连续的**

因此,在删除或增添元素的时候,难免要移动其他元素的地址

![img](https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%841.png)

**数组的元素是不能删的,只能覆盖**

二维数组在C++中内存的空间地址是连续的,在Java中不是连续的,但是是多条连续的地址空间组成的

![img](https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%842.png)

![img](https://file1.kamacoder.com/i/algo/%E7%AE%97%E6%B3%95%E9%80%9A%E5%85%B3%E6%95%B0%E7%BB%843.png)

#### 数组经典题目回顾

##### 二分法

**循环不变量原则**,左闭右闭or左闭右开,要在循环中坚持对区间的定义

##### 双指针法

又名快慢指针法:**通过一个快指针和慢指针在一个for循环下完成两个for循坏的工作**

数组的元素不能删除,因为:

- 数组在内存中是连续的地址空间,不能释放单一元素;如果要释放就是全释放(程序运行结束,回收内存栈空间)
- C++中vector和array的区别,vector的底层实现是array,封装后使用更友好

> 补充一下:
>
> array,静态数组
> 长度在编译时就必须确定,运行时无法修改,存储在栈内存(访问速度极快但空间有限),类似于Python中手动固定长度的列表[0]*5;用于存储固定数量的产量(比如一周7天的温度)
>
> vector,动态数组
> 动态可扩展的数组,长度在运行时可以自由调整(增删元素),存储在堆内存(堆内存空间大但访问速度略慢),类似于Python中的list;用于存储数量不确定的数据(比如用户输入的任意个数的数字、动态加载的列表)

```c++
//array

#include <iostream>
// 必须包含array头文件才能使用array容器
#include <array>
using namespace std;

int main() {
    // ========== 1. 定义array ==========
    // 格式：array<数据类型, 固定长度> 变量名;
    // 类比Python：scores = [0]*3（长度固定为3，不能append/删除）
    array<int, 3> scores;  // 定义一个长度为3、存储int类型的array
    
    // ========== 2. 初始化/赋值 ==========
    // 方式1：逐个赋值（类似Python的scores[0]=90）
    scores[0] = 90;  // 第0个元素赋值90
    scores[1] = 85;  // 第1个元素赋值85
    scores[2] = 95;  // 第2个元素赋值95
    // 注意：array长度固定为3，无法访问scores[3]，否则会越界报错（类似Python列表越界）
    
    // 方式2：定义时直接初始化（推荐）
    array<int, 3> ages = {18, 20, 22};  // 初始化3个元素
    
    // ========== 3. 访问元素 ==========
    cout << "array的第0个元素：" << scores[0] << endl;  // 输出90
    // 更安全的访问方式：at()（越界时会抛异常，而[]直接崩溃）
    cout << "array的第1个元素：" << scores.at(1) << endl;  // 输出85
    
    // ========== 4. 获取长度 ==========
    // size()返回固定长度（编译时确定，无法修改）
    cout << "array的长度：" << scores.size() << endl;  // 输出3
    
    // ========== 5. 遍历array ==========
    // 类比Python的for score in scores:
    cout << "遍历array：";
    for (int i = 0; i < scores.size(); i++) {
        cout << scores[i] << " ";  // 输出90 85 95
    }
    cout << endl;
    
    // ❌ 错误尝试：array无法动态扩容，没有push_back方法（和Python list的append不同）
    // scores.push_back(100);  // 编译报错！array没有这个方法
    
    return 0;
}

//vector

#include <iostream>
// 必须包含vector头文件
#include <vector>
using namespace std;

int main() {
    // ========== 1. 定义vector ==========
    // 格式：vector<数据类型> 变量名;
    // 类比Python：nums = []（空列表，长度动态）
    vector<int> nums;  // 定义一个空的、存储int类型的vector
    
    // ========== 2. 动态添加元素（核心！类比Python的append） ==========
    nums.push_back(10);  // 尾部添加元素10 → nums = [10]
    nums.push_back(20);  // 尾部添加元素20 → nums = [10,20]
    nums.push_back(30);  // 尾部添加元素30 → nums = [10,20,30]
    
    // ========== 3. 访问元素 ==========
    cout << "vector的第0个元素：" << nums[0] << endl;  // 输出10
    cout << "vector的第2个元素：" << nums.at(2) << endl;  // 输出30（安全访问）
    
    // ========== 4. 获取长度（动态变化） ==========
    cout << "vector当前长度：" << nums.size() << endl;  // 输出3
    
    // ========== 5. 动态删除元素（类比Python的pop） ==========
    nums.pop_back();  // 删除尾部元素 → nums = [10,20]
    cout << "删除后vector长度：" << nums.size() << endl;  // 输出2
    
    // ========== 6. 遍历vector ==========
    cout << "遍历vector：";
    // 方式1：下标遍历（类比Python for i in range(len(nums))）
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";  // 输出10 20
    }
    cout << endl;
    
    // 方式2：范围遍历（类比Python的for num in nums）
    cout << "范围遍历vector：";
    for (int num : nums) {
        cout << num << " ";  // 输出10 20
    }
    cout << endl;
    
    // ========== 7. 清空vector ==========
    nums.clear();  // 清空所有元素 → nums = []
    cout << "清空后vector长度：" << nums.size() << endl;  // 输出0
    
    return 0;
}
```

##### 滑动窗口

滑动窗口:移动窗口的起始位置,达到动态更新窗口大小,从而得出长度最小的复合条件的长度

滑动窗口的精髓:**根据当前子序列和大小的情况,不断调节子序列的起始位置**

##### 模拟行为(螺旋矩阵)

**循环不变量**,模拟类的题目不涉及到算法,只是单纯的模拟

##### 前缀和

**前缀和**在涉及**计算区间和的问题**时非常有用,**重复利用计算过的子数组之和**,从而降低区间查询需要累加计算的次数

##### 思维导图

![img](https://file1.kamacoder.com/i/algo/%E6%95%B0%E7%BB%84%E6%80%BB%E7%BB%93.png)

---

## 链表

### 链表理论基础

**链表**:一种通过**指针**串联在一起的**线性结构**,是一种**逻辑上线性、物理上非连续**的存储结构。核心是由一个个独立的`节点（Node）`组成，每一个节点由**数据域和指针域**组成，**数据域**用来存储实际的业务数据（比如数字、字符串）；**指针域**用来存储下一个节点的地址(指针域存放指向下一个节点的指针),最后一个节点的指针域指向`空指针（null）`

链表的入口节点称为链表的头节点(head)

> 对比数组与单链表
>
> |    特性     |     数组（Python 列表）      |                  单链表                  |
> | :---------: | :--------------------------: | :--------------------------------------: |
> |  内存存储   |      **连续的内存空间**      | **分散的内存空间**，**节点间靠指针连接** |
> |  访问元素   |      随机访问（O (1)）       |          只能从头遍历（O (n)）           |
> | 插入 / 删除 | 中间操作 O (n)（需移动元素） |       找到位置后 O (1)（仅改指针）       |
> |    容量     |    自动扩容（有额外开销）    |            动态扩容（无开销）            |
> |  空间开销   |           仅存数据           |          额外存指针（略占空间）          |
>
> 列表`list`的本质是动态数组，所有元素在内存中是连续存储的，每个元素都有固定的内存地址
> 当执行`pop(0)`（删除索引0的元素）时，因为数组要求内存连续，那么后面所有的元素都要向前移动一个位置来填补第一个位置的空缺，移动操作的次数等于列表的长度n，所以时间复杂度为O（n）；当执行`pop()`（删除最后一个元素）时，前面的元素无需移动，直接释放最后一个位置即可，O（1）
> 
>`deque`这样的双向链表，用`popleft()`删除第一个元素时，只是修改了指针的指向，剪断了第一个元素和第二个元素的连接，无需移动任何元素，极其省时间
> 
>数组（列表）动“元素位置”，链表动“节点之间的**连接关系**”，不移动任何元素

![链表1](https://file1.kamacoder.com/i/algo/20200806194529815.png)

#### 链表的类型

##### 单链表

单链表就是上图这样的形式

##### 双链表

单链表中的**指针域**只能指向节点的下一个节点

**双链表**:每一个节点有两个指针域,一个指向下一个节点（next）,一个指向上一个节点（prev），可实现队列

**双链表**既可以向前查询又可以向后查询

![链表2](https://file1.kamacoder.com/i/algo/20200806194559317.png)

##### 循环链表

循环链表的首尾相连,可以用来解决约瑟夫环问题

![链表4](https://file1.kamacoder.com/i/algo/20200806194629603.png)



> 约瑟夫环介绍
> 有 `n` 个人围成一个圈，从第一个人开始报数，报到第 `m` 个数的人出列，接着从下一个人开始继续报数。如此循环，直到圈中只剩下最后一个人;目标：找到最后一个人的位置（或模拟整个淘汰过程）
>
> 用循环链表解决的思路:
>
> 1. **构建循环列表**:把每个人看作链表的一个节点,将链表首尾相连形成一个环
> 2. **模拟报数淘汰**:从链表头开始遍历,每数到第`m`个节点就将其从环中删除
> 3. **循环执行**:重复步骤2,直到链表中只剩下一个节点
>
> Python代码实现
>
> ```python
> class ListNode:#定义一个ListNode类,用来表示链表的单个节点(对应环中的一个人)
>     """定义链表节点类"""
>     def __init__(self, val):#类的构造方法,创建节点时必须传入val(节点值)
>         self.val = val  #给节点绑定值属性,用于存储人的编号
>         self.next = None  #给节点绑定指针属性,初始值None,表示一开始不指向任何其他节点,指针用来指向下一个节点的指针
> 
> def solve_josephus(n, m):
>     """
>     用循环链表解决约瑟夫环问题
>     :param n: 总人数
>     :param m: 报数的步长
>     :return: 最后存活者的编号
>     """
>     # 1. 构建循环链表
>     if n == 0:
>         return -1#表示无效输入,避免后续代码报错
>     # 创建头节点
>     head = ListNode(1)#创建第一个节点,作为链表的“头节点”
>     current = head#定义current指针,初始指向头节点,用于遍历后续节点
>     # 生成剩余的 n-1 个节点
>     for i in range(2, n+1):#循环生成第2到n号节点
>         current.next = ListNode(i)#给当前节点的next指针绑定新节点
>         current = current.next#将current指针移动到新创建的节点上
>     # 让链表首尾相连，形成环
>     current.next = head#循环结束后的current指向最后一个节点n,把它绑定到头节点,使链表形成环
> 
>     # 2. 模拟淘汰过程
>     # 从环的头部开始
>     # 定义prev指针(“前一个节点”指针),初始指向最后一个节点n.要删除一个节点必须修改它前一个节点的next指针,所以需要prev辅助
>     prev = current
>     current = head#将current指针重新指向头节点,准备开始模拟报数淘汰
>     # 当环中不止一个节点时继续循环
>     while current.next != current:#循环终止条件:链表中节点的下一个还是自己
>         # 报数 m 次，移动指针
>         for _ in range(m-1):#报数m次只需要移动m-1次指针
>             prev = current#每次移动前先把prev更新为当前节点
>             current = current.next#再把current移到下一个节点
>         #循环结束后current正好指向第m个节点(要淘汰的人)    
>         # 移除当前节点（第 m 个节点）
>         prev.next = current.next#把要淘汰节点的前一个节点的next指针指向要淘汰节点的下一个节点,相当于从环中删掉当前节点
>         current = prev.next#将current指针移到下一个节点
> 
>     # 3. 返回最后存活的节点值
>     return current.val
> 
> # 示例：n=5个人，报数到3的人出列
> if __name__ == "__main__":
>     n = 5
>     m = 3
>     result = solve_josephus(n, m)
>     print(f"最后存活者的编号是: {result}")  # 输出：4
> ```

#### 链表的存储方式

**数组**在内存中是连续分布的,但是**链表**在内存中是**不连续分布**的

链表是通过指针域的指针**链接**在内存中的各个节点

因此,链表中的节点在内存中不是连续分布的 ，而是散乱分布在内存中的某地址上，分配机制取决于操作系统的内存管理。

![链表3](https://file1.kamacoder.com/i/algo/20200806194613920.png)

如图所示,这个链表起始节点为2,终止节点为7,各个节点分布在内存的不同地址空间上,通过指针串联在一起

#### 链表的定义

==**链表节点的定义**十分重要!!!==

```c++
// C++定义单链表节点	定义构造函数
struct ListNode {
    int val;  // 节点上存储的元素
    ListNode *next;  // 指向下一个节点的指针
    ListNode(int x) : val(x), next(NULL) {}  // 节点的构造函数
};
```

```python
class ListNode:
    """链表节点类"""
    def __init__(self, val=0, next=None):
        # 节点存储的值，默认值为0
        self.val = val
        # 指向下一个节点的引用，默认值为None（无后续节点）
        self.next = next
	#通过current指针从表头head开始,不断将current更新为current.next,直到current为None 
    
    # 自定义打印格式，方便调试（可选但推荐）
    def __str__(self):
        return f"ListNode(val={self.val})"
```

#### 链表的操作

##### 删除节点

![链表-删除节点](https://file1.kamacoder.com/i/algo/20200806195114541-20230310121459257.png)

删除D节点,只需要将C节点的next指针指向E节点即可

此时,D节点依然留在内存里(只会是不在这个链表中),在C++中要手动释放这个D节点(释放内存),Java、Python等有自己的内存回收机制,无需手动释放

##### 添加节点

![链表-添加节点](https://file1.kamacoder.com/i/algo/20200806195134331-20230310121503147.png)

链表的增添和删除都是O(1)操作,不会影响其他节点

不过,要是删除第五个节点,需要从头节点查找到第四个节点通过next指针进行删除操作,查找的时间复杂度是O(n)

#### 性能分析

![链表-链表与数据性能对比](https://file1.kamacoder.com/i/algo/20200806195200276.png)

数组定义时长度就固定,要想改动数组就要重新定义一个新的数组

链表的长度是不固定的，可以动态增删,适合数据量不固定,频繁增删较少查询的场景

### 移除链表元素

[力扣原题](https://leetcode.cn/problems/remove-linked-list-elements/)

```plain
#题目

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
```

#### 思路

用链表1 4 2 4举例,移除元素4

![203_链表删除元素1](https://file1.kamacoder.com/i/algo/20210316095351161.png)

如果使用C++,还要从内存中删除这两个移除的节点,清理节点内存之后如图所示:

![203_链表删除元素2](https://file1.kamacoder.com/i/algo/20210316095418280.png)

使用Java、Python则无需手动管理内存,使用C++一定要养成**手动清理内存**的好习惯

**移除操作**	==直接让节点next指针指向下下一个节点即可==

因为单链表的特殊性,只能指向下一个节点,刚刚删除的是链表中的第二个和第四个节点,如果删除的是头节点需要涉及如下链表操作的方式:

- **直接使用原来的链表进行删除操作**
- **设置一个虚拟头节点再进行删除操作**

首先直接使用原来的链表来进行移除

![203_链表删除元素3](https://file1.kamacoder.com/i/algo/2021031609544922.png)

移除头节点不同于移除其他节点的操作,因为**链表的其他节点都是通过前一个节点来移除当前节点**,但是头节点没有前一个节点

![203_链表删除元素4](https://file1.kamacoder.com/i/algo/20210316095512470.png)

**只要将头节点向后移动一位就从链表中移除了一个头节点**,同时要将原来的头节点从内存中删掉

![203_链表删除元素5](https://file1.kamacoder.com/i/algo/20210316095543775.png)

这样就移除了一个头节点,可以发现单链表中移除头节点和移除其他节点的操作方式不一样,需要单独写一段逻辑来处理移除头节点的情况,可以==**设置一个虚拟头节点**==**将所有节点按照统一的方式进行移除**

![203_链表删除元素6](https://file1.kamacoder.com/i/algo/20210316095619221.png)

首先要给链表添加一个虚拟头节点作为新的头节点,这样就实现了和移除链表其他节点方式的统一.在题目中，return 头结点的时候，需要return dummyNode->next; 这才是新的头结点

**使用递归的思路解决本题**

基础情况:对于空链表,不需要移除元素

递归情况:首先检查头节点的值是否为val,如果是则移除头节点,答案即为在后续节点上递归的结果;如果头节点的值不为val,答案为头节点与在头节点的后续节点上递归得到的新链表拼接的结果

```c++
//直接使用原来的链表来进行移除节点操作
//定义了Solution类的成员函数removeElements,接收两个参数(ListNode* head 链表的头节点指针,int val 需要删除的节点值)
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // 删除头结点
        while (head != NULL && head->val == val) { // 注意这里不是if,因为头节点可能连续多个都为目标值,需要循环检查,循环条件head != NULL避免空指针访问 head->val == val当前头节点值是目标值
            ListNode* tmp = head;//暂存当前要删除的头节点(后续head会移动,需要先保存指针才能释放内存)
            head = head->next;//将头节点指针移动到下一个节点,完成移除当前头节点的逻辑
            delete tmp;//释放被移除节点的内存,C++必须手动释放,否则会内存泄漏
        }

        // 删除非头结点,通过前驱节点操作后继节点(链表删除的经典逻辑)
        ListNode* cur = head;//定义遍历指针cur,从处理后的头节点开始遍历
        while (cur != NULL && cur->next!= NULL) {//避免空指针(比如头节点被删空后,cur为NULL;检查cur的下一个节点保证不为空)
            if (cur->next->val == val) {//下一个节点的值是要删除的值
                ListNode* tmp = cur->next;//暂存要删除的节点
                cur->next = cur->next->next;//让cur的next跳过目标节点,指向目标节点的下一个节点(完成链表的断链+重连)
                delete tmp;
            } else {//若下一个节点不是目标值，将cur后移一位，继续遍历
                cur = cur->next;
            }
        }
        return head;
    }
};


//设置虚拟头节点再进行移除节点操作
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummyHead = new ListNode(0); // 设置一个虚拟头结点
        dummyHead->next = head; // 将虚拟头结点指向head，这样方便后面做删除操作
        ListNode* cur = dummyHead;
        while (cur->next != NULL) {//不是最后一个节点，因为最后一个节点的next指向NULL
            if(cur->next->val == val) {
                ListNode* tmp = cur->next;
                cur->next = cur->next->next;
                delete tmp;
            } else {
                cur = cur->next;
            }
        }
        head = dummyHead->next;
        delete dummyHead;
        return head;
    }
};
//ListNode* cur 存的是地址，指向内存里真正的ListNode对象，ListNode是链表节点的类/结构体（包含val值和next指针）		这里cur不是ListNode对象本身，而是存储了ListNode对象内存地址的指针
// ->是c++里指针访问成员的专用运算符
// 如果有一个对象本身（非指针），用 . 访问成员 比如obj.val
// 如果有一个指向对象的指针，用 -> 访问成员 比如cur->next，等价于(*cur).next，需要先通过*拿到指针指向的对象，再用.访问next成员 
//ListNode* p中的*p表示取指针p指向的那个实际对象

//递归情况
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // 基础情况：空链表
        // 递归的底线,保证递归不会无限调用下去
        if (head == nullptr) {
            return nullptr;
        }

        // 递归处理,先处理子链表,再决定当前节点去留
        // 要删除整个链表中值为val的节点,可以先删除当前节点的下一个节点组成的子链表中的目标节点,再决定当前节点是否保留(先深入到链表的最末尾触发终止条件,再从末尾回溯到开头一步步处理每个节点)
        if (head->val == val) {
            //当前节点要被删除,先递归处理当前节点的下一个节点组成的子链表
            ListNode* newHead = removeElements(head->next, val);
            delete head;
            return newHead;
        } else {
            //当前节点要保留,所以递归处理当前节点的下一个节点组成的子链表
            head->next = removeElements(head->next, val);
            return head;
        }
    }
};

```

Python版本

```python
#定义通用的ListNode类
class ListNode:
    """链表节点类（和C++的ListNode对应）"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#直接操作原链表移除节点
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 1. 删除头结点（连续多个头节点为目标值的情况）
        # 循环条件：head不为空 且 当前头节点值等于目标值
        while head is not None and head.val == val:
            # Python无需暂存节点释放内存，直接移动头节点即可
            head = head.next
        
        # 2. 删除非头结点（通过前驱节点cur操作后继节点）
        cur = head  # 遍历指针从处理后的头节点开始
        # 循环条件：cur不为空 且 cur的下一个节点不为空（避免访问cur.next.val时报错）
        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                # 跳过目标节点，完成删除
                cur.next = cur.next.next
            else:
                # 下一个节点不是目标值，cur后移
                cur = cur.next       
        # 返回处理后的头节点
        return head

 
#设置虚拟头节点移除节点
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 创建虚拟头节点（值为0，无实际意义，仅作为统一的前驱节点）
        dummy_head = ListNode(0)
        dummy_head.next = head  # 虚拟头节点指向原头节点
        
        cur = dummy_head  # 遍历指针从虚拟头节点开始
        # 循环条件：cur的下一个节点不为空（只需检查这一个条件，因为dummy_head一定非空）
        while cur.next is not None:
            if cur.next.val == val:
                # 删除cur的下一个节点（无论是不是头节点，逻辑都一样）
                cur.next = cur.next.next
            else:
                # 非目标值，cur后移
                cur = cur.next
        
        # 注意：返回虚拟头节点的next（原头节点可能已被删除）
        # Python无需释放虚拟头节点，垃圾回收会自动处理
        return dummy_head.next


#递归方式移除节点	递归:递(深入);归(回溯)
#拆分大问题为小问题————先处理当前节点的下一个链表,再判断当前节点是否需要保留
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 递归终止条件：链表为空（没有节点可处理）
        if head is None:
            return None
        
        # 递归处理：先处理当前节点的下一级子链表，返回处理后的子链表头节点
        head.next = self.removeElements(head.next, val)
        
        # 判断当前节点是否需要保留：
        # 1. 若当前节点值等于val，返回下一个节点（相当于删除当前节点）
        # 2. 否则返回当前节点（保留）
        return head.next if head.val == val else head
#递归:待处理链表1->6->3
#首先是递(表示深入)
#第一次调用(node1,6),head!=None,则调用self.removeElements(node6,6);
#第二次调用(node6,6),head!=None,则调用self.removeElements(node3,6);	
#第三次调用(node3,6),head!=None,则调用self.removeElements(None,6);函数会暂停在这一行,等到removeElements(None,6)返回None后函数才会苏醒,苏醒后先执行这一行的赋值语句作用
#第四次调用(None,6),满足if语句,返回None;此时是递归出口,表示终止
#接着是归(表示回溯)
#调用(node3,6),接收调用(None,6)返回的None,执行node3.next=None,检查node3.val=3!=6,因此返回head(此时为node3)
#调用(node6,6),接收调用返回的node3,执行node6.next=node3,检查node6.val=6,因此要删除,返回node3
#调用(node1,6),接收node3,执行node1.next=node3,检查node1.val=1,因此返回node1
```

> 递归函数的执行不是一口气跑完,而是会在调用(递的步骤)下一层的地方**暂停**,等下一层**返回结果**后再**苏醒**并执行暂停之后的代码(归的步骤)
>
> 上面的递归是这样的,处理节点1的时候,执行head.next=removeElements(节点6,6)->暂停,先去处理节点6;一直作这样的处理,知道处理节点3的下一个节点None时,触发了终止条件返回None
>
> 返回None后函数苏醒,继续执行暂停点之后的代码

### 设计链表

[力扣原题](https://leetcode.cn/problems/design-linked-list/description/)

```plain
#题目

选择使用单链表或者双链表，设计并实现自己的链表
单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：
MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。

即实现：
获取第n个节点的值
头部插入节点
尾部插入节点
第n个节点前插入节点
删除第n个节点
```

注意：

1. 操作第n个点一定是current->next
2. 插入节点时注意更新顺序，否则指向会出错

C++代码

```c++
class MyLinkedList {
public:
    // 定义链表节点结构体
    struct LinkedNode {
        int val;
        LinkedNode* next;
        LinkedNode(int val):val(val), next(nullptr){}
    };

    // 初始化链表
    MyLinkedList() {
        _dummyHead = new LinkedNode(0); // 这里定义的头结点 是一个虚拟头结点，而不是真正的链表头结点
        _size = 0;
    }

    // 获取到第index个节点数值，如果index是非法数值直接返回-1， 注意index是从0开始的，第0个节点就是头结点
    // 定义一个名为get的函数，接收int类型的索引index，返回int类型的值
    int get(int index) {
        if (index > (_size - 1) || index < 0) {//_size是链表的实际节点总数
            return -1;
        }
        // 初始化遍历指针cur
        // LinkedNode* cur 定义一个指向链表节点的指针cur
        // _dummyHead->next 虚拟头节点的下一个节点，即链表中索引为0的节点
        LinkedNode* cur = _dummyHead->next;
        while(index--){ 
            // index-- 先使用index的当前值判断循环条件，再把index-1，这里如果用--index 就会陷入死循环
            cur = cur->next;
        }
        return cur->val;
    }

    // 在链表最前面插入一个节点，插入完成后，新插入的节点为链表的新的头结点
    void addAtHead(int val) {
        LinkedNode* newNode = new LinkedNode(val);//创建一个新的节点
        newNode->next = _dummyHead->next;
        _dummyHead->next = newNode;
        _size++;
    }

    // 在链表最后面添加一个节点
    void addAtTail(int val) {
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dummyHead;
        while(cur->next != nullptr){
            cur = cur->next;
        }//循环结束后cur已经指向了最后一个节点了
        cur->next = newNode;//将最后一个节点的指针指向新的节点即可
        _size++;
    }

    // 在第index个节点之前插入一个新节点，例如index为0，那么新插入的节点为链表的新头节点。
    // 如果index 等于链表的长度，则说明是新插入的节点为链表的尾结点
    // 如果index大于链表的长度，则返回空
    // 如果index小于0，则在头部插入节点
    void addAtIndex(int index, int val) {

        if(index > _size) return;
        if(index < 0) index = 0;        
        
        LinkedNode* newNode = new LinkedNode(val);//创建新节点
        //new LinkedNode(val)在堆内存中创建了一个LinkedNode对象，值为val，返回该节点的内存地址；定义指针newNode来接收新节点的地址（即指向新节点）
        LinkedNode* cur = _dummyHead;//初始化遍历指针cur，从虚拟头节点开始
        //插入操作需要找到插入位置的前驱节点，要插在某个节点前必须先找到该节点的前一个节点
        while(index--) {
            cur = cur->next;//cur指针向后移动一个节点
        }//循环结束后，cur正好指向要插入位置的前驱节点
        newNode->next = cur->next;
        /* 解释：
       cur->next是“插入位置原本的节点”（比如插在索引2，cur->next就是原来的索引2节点）；
       这一步必须先做！如果先改cur->next，会丢失原来的cur->next地址，新节点就找不到后续链表了。*/
        cur->next = newNode;
        _size++;
    }

    // 删除第index个节点，如果index 大于等于链表的长度，直接return，注意index是从0开始的
    void deleteAtIndex(int index) {
        if (index >= _size || index < 0) {
            return;
        }
        LinkedNode* cur = _dummyHead;
        while(index--) {
            cur = cur ->next;
        }
        LinkedNode* tmp = cur->next;
        cur->next = cur->next->next;
        delete tmp;
        //delete命令指示释放了tmp指针原本所指的那部分内存，
        //被delete后的指针tmp的值（地址）并非就是NULL，而是随机值。也就是被delete后，
        //如果不再加上一句tmp=nullptr,tmp会成为乱指的野指针
        //如果之后的程序不小心使用了tmp，会指向难以预想的内存空间
        tmp=nullptr;
        _size--;
    }

    // 打印链表
    void printLinkedList() {
        LinkedNode* cur = _dummyHead;
        while (cur->next != nullptr) {
            cout << cur->next->val << " ";
            cur = cur->next;
        }
        cout << endl;
    }
private:
    int _size;
    LinkedNode* _dummyHead;

};
```

```C++
//采用循环虚拟结点的双链表实现
class MyLinkedList {
public:
    // 定义双向链表节点结构体
    struct DList {
        int elem; // 节点存储的元素
        DList *next; // 指向下一个节点的指针
        DList *prev; // 指向上一个节点的指针
        // 构造函数，创建一个值为elem的新节点
        DList(int elem) : elem(elem), next(nullptr), prev(nullptr) {};
    };

    // 构造函数，初始化链表
    MyLinkedList() {
        sentinelNode = new DList(0); // 创建哨兵节点，不存储有效数据
        sentinelNode->next = sentinelNode; // 哨兵节点的下一个节点指向自身，形成循环
        sentinelNode->prev = sentinelNode; // 哨兵节点的上一个节点指向自身，形成循环
        size = 0; // 初始化链表大小为0
    }

    // 获取链表中第index个节点的值
    int get(int index) {
        if (index > (size - 1) || index < 0) { // 检查索引是否超出范围
            return -1; // 如果超出范围，返回-1
        }
        int num;
        int mid = size >> 1; // 计算链表中部位置
        DList *curNode = sentinelNode; // 从哨兵节点开始
        if (index < mid) { // 如果索引小于中部位置，从前往后遍历
            for (int i = 0; i < index + 1; i++) {
                curNode = curNode->next; // 移动到目标节点
            }
        } else { // 如果索引大于等于中部位置，从后往前遍历
            for (int i = 0; i < size - index; i++) {
                curNode = curNode->prev; // 移动到目标节点
            }
        }
        num = curNode->elem; // 获取目标节点的值
        return num; // 返回节点的值
    }

    // 在链表头部添加节点
    void addAtHead(int val) {
        DList *newNode = new DList(val); // 创建新节点
        DList *next = sentinelNode->next; // 获取当前头节点的下一个节点
        newNode->prev = sentinelNode; // 新节点的上一个节点指向哨兵节点
        newNode->next = next; // 新节点的下一个节点指向原来的头节点
        size++; // 链表大小加1
        sentinelNode->next = newNode; // 哨兵节点的下一个节点指向新节点
        next->prev = newNode; // 原来的头节点的上一个节点指向新节点
    }

    // 在链表尾部添加节点
    void addAtTail(int val) {
        DList *newNode = new DList(val); // 创建新节点
        DList *prev = sentinelNode->prev; // 获取当前尾节点的上一个节点
        newNode->next = sentinelNode; // 新节点的下一个节点指向哨兵节点
        newNode->prev = prev; // 新节点的上一个节点指向原来的尾节点
        size++; // 链表大小加1
        sentinelNode->prev = newNode; // 哨兵节点的上一个节点指向新节点
        prev->next = newNode; // 原来的尾节点的下一个节点指向新节点
    }

    // 在链表中的第index个节点之前添加值为val的节点
    void addAtIndex(int index, int val) {
        if (index > size) { // 检查索引是否超出范围
            return; // 如果超出范围，直接返回
        }
        if (index <= 0) { // 如果索引为0或负数，在头部添加节点
            addAtHead(val);
            return;
        }
        int num;
        int mid = size >> 1; // 计算链表中部位置
        DList *curNode = sentinelNode; // 从哨兵节点开始
        if (index < mid) { // 如果索引小于中部位置，从前往后遍历
            for (int i = 0; i < index; i++) {
                curNode = curNode->next; // 移动到目标位置的前一个节点
            }
            DList *temp = curNode->next; // 获取目标位置的节点
            DList *newNode = new DList(val); // 创建新节点
            curNode->next = newNode; // 在目标位置前添加新节点
            temp->prev = newNode; // 目标位置的节点的前一个节点指向新节点
            newNode->next = temp; // 新节点的下一个节点指向目标位置的结点
            newNode->prev = curNode; // 新节点的上一个节点指向当前节点
        } else { // 如果索引大于等于中部位置，从后往前遍历
            for (int i = 0; i < size - index; i++) {
                curNode = curNode->prev; // 移动到目标位置的后一个节点
            }
            DList *temp = curNode->prev; // 获取目标位置的节点
            DList *newNode = new DList(val); // 创建新节点
            curNode->prev = newNode; // 在目标位置后添加新节点
            temp->next = newNode; // 目标位置的节点的下一个节点指向新节点
            newNode->prev = temp; // 新节点的上一个节点指向目标位置的节点
            newNode->next = curNode; // 新节点的下一个节点指向当前节点
        }
        size++; // 链表大小加1
    }

    // 删除链表中的第index个节点
    void deleteAtIndex(int index) {
        if (index > (size - 1) || index < 0) { // 检查索引是否超出范围
            return; // 如果超出范围，直接返回
        }
        int num;
        int mid = size >> 1; // 计算链表中部位置
        DList *curNode = sentinelNode; // 从哨兵节点开始
        if (index < mid) { // 如果索引小于中部位置，从前往后遍历
            for (int i = 0; i < index; i++) {
                curNode = curNode->next; // 移动到目标位置的前一个节点
            }
            DList *next = curNode->next->next; // 获取目标位置的下一个节点
            curNode->next = next; // 删除目标位置的节点
            next->prev = curNode; // 目标位置的下一个节点的前一个节点指向当前节点
        } else { // 如果索引大于等于中部位置，从后往前遍历
            for (int i = 0; i < size - index - 1; i++) {
                curNode = curNode->prev; // 移动到目标位置的后一个节点
            }
            DList *prev = curNode->prev->prev; // 获取目标位置的下一个节点
            curNode->prev = prev; // 删除目标位置的节点
            prev->next = curNode; // 目标位置的下一个节点的下一个节点指向当前节点
        }
        size--; // 链表大小减1
    }

private:
    int size; // 链表的大小
    DList *sentinelNode; // 哨兵节点的指针
};
```

Python版本

```python
#（版本一）单链表法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val#节点存储的值
        self.next = next#节点的next指针，指向下一个节点
        
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        current = self.dummy_head.next
        for i in range(index):
            current = current.next     
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        #创建一个新节点值为val，这个新节点的next指针指向self.dummy_head.next
        #self.dummy_head是类的实例属性
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1
```

### 反转链表

```plain
#题目

已知单链表的头节点head，请反转链表，并返回反转后的链表
例如	输入head=[1,2,3,4,5]	输出：[5,4,3,2,1]
```

#### 思路

定义一个新的链表来实现链表元素的反转的话是对内存空间的浪费

只需要改变链表的next指针指向就可以直接将链表反转，而不用重新定义一个新的链表

![206_反转链表](https://file1.kamacoder.com/i/algo/20210218090901207.png)

用实例中的链表举例

1. 定义一个cur指针，指向头节点；再定义一个pre指针，初始化为null
2. 首先把cur->next节点用tmp指针保存一下，即保存一下这个指针
3. 接着改变cur->next的指向，将cur->next指向pre，此时反转了第一个节点
4. 循环走如下代码逻辑，继续移动pre和cur指针
5. 最后，cur指针指向了null，循环结束，链表反转完毕

#### 双指针法

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* temp; // 保存cur的下一个节点
        ListNode* cur = head;
        ListNode* pre = NULL;
        while(cur) {//当cur不是NULL时执行循环语句的内容
            temp = cur->next;  // 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur->next = pre; // 翻转操作
            // 更新pre 和 cur指针
            pre = cur;
            cur = temp;
        }
        return pre;
    }
};
```

#### 递归法

递归法利用双指针的原理，同样是当cur为空的时候循环结束，不断将cur指向pre

```c++
//定义链表的节点类
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//递归法其一，同双指针法原理
class Solution {
public:
    ListNode* reverse(ListNode* pre,ListNode* cur){
        if(cur == NULL) return pre;
        ListNode* temp = cur->next;
        cur->next = pre;
        // 可以和双指针法的代码进行对比，如下递归的写法，其实就是做了这两步
        // pre = cur;
        // cur = temp;
        return reverse(cur,temp);
    }
    ListNode* reverseList(ListNode* head) {
        // 和双指针法初始化是一样的逻辑
        // ListNode* cur = head;
        // ListNode* pre = NULL;
        return reverse(NULL, head);
    }

};

//递归法其二
//链表例子：1 -> 2 -> 3 -> NULL
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 1. 边缘条件判断：空链表直接返回NULL
        if(head == NULL) return NULL;
        // 2. 递归终止条件：只剩一个节点时，它就是反转后的头节点，直接返回
        if (head->next == NULL) return head;
        
        // 3. 递归调用：反转「当前节点后面的所有节点」
        ListNode *last = reverseList(head->next);
        /* 关键解释：
           - 对于 head=1，调用 reverseList(2)；
           - 对于 head=2，调用 reverseList(3)；
           - 对于 head=3，触发终止条件，返回 3（此时 last=3）；
           这一步的目的是：先把后面的子链表反转好，拿到反转后的子链表头节点 last。
        */
        
        // 4. 核心反转：把当前节点接到「反转后子链表的末尾」，局部反转
        head->next->next = head;
        /* 关键解释：
           - 以 head=2 为例：此时 head->next=3，这行代码就是 3->next=2；
           - 以 head=1 为例：此时 head->next=2（已经被反转过），这行代码就是 2->next=1；
           这一步完成了「当前节点」和「下一个节点」的指向反转。
        */
        
        // 5. 收尾：让当前节点成为新的尾节点（避免形成环）
        head->next = NULL;
        /* 关键解释：
           - 以 head=2 为例：把 2->next 置空，此时 2 是反转后子链表（3->2）的尾节点；
           - 以 head=1 为例：把 1->next 置空，此时 1 是最终链表（3->2->1）的尾节点；
           如果不置空，会出现 1->2->1 的环，导致链表出错。
        */
        
        // 6. 返回反转后的总头节点（始终是原链表的最后一个节点）
        return last;
    }
};
```

Python版本

```python
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#双指针法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while cur:
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        #循环结束时的cur为None，则pre为链表的头节点，返回pre即可
        return pre

#递归法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)
```

### 两两交换链表中的节点

```plain
#题目

给定一个链表，两两交换其中相邻的节点，返回交换后的链表
不能单纯的改变节点内部的值，需要实际的进行节点交换

输入；head=[1,2,3,4]	输出：[2,1,4,3]
```

#### 思路

使用虚拟头节点，不满每次针对头节点（没有前一个指针指向头节点）还要单独处理

初始时，cur指向虚拟头结点，然后进行如下三步：

![24.两两交换链表中的节点1](https://file1.kamacoder.com/i/algo/24.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B91.png)

操作之后，链表如下：

![24.两两交换链表中的节点2](https://file1.kamacoder.com/i/algo/24.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B92.png)

看这个可能就更直观一些了：

![24.两两交换链表中的节点3](https://file1.kamacoder.com/i/algo/24.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B93.png)

```c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummyHead = new ListNode(0); // 设置一个虚拟头结点
        dummyHead->next = head; // 将虚拟头结点指向head，这样方便后面做删除操作
        ListNode* cur = dummyHead;//初始化cur指针指向虚拟头节点
        while(cur->next != nullptr && cur->next->next != nullptr) {//注意条件顺序，此语句用于判断偶数个节点的下一个节点为null，奇数个节点的下下一个节点为null，此时停止循环
            //为什么要记录两个临时节点：因为做交换时需要先锁定交换对的前置节点，前置节点的next应该为交换对中的后面那个，建立指向后，后面那个节点断开了交换对的节点指向连接和后一个指向连接，同时要作为下一个交换对的前置节点
            ListNode* tmp = cur->next; // 记录临时节点
            ListNode* tmp1 = cur->next->next->next; // 记录临时节点

            cur->next = cur->next->next;    // 步骤一
            cur->next->next = tmp;          // 步骤二
            cur->next->next->next = tmp1;   // 步骤三

            cur = cur->next->next; // cur移动两位，准备下一轮交换
        }
        ListNode* result = dummyHead->next;
        delete dummyHead;
        return result;
    }
};
```

Python版本

```python
#定义节点类
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

##递归算法
#递归的本质是把大问题拆解成同类型的小问题，这段代码每次只处理当前链表的前两个节点的交换，把后续剩余链表的两两交换交给递归函数处理直到遇到终止条件（链表空/只剩一个节点）时停止递归并返回
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #递归出口，避免无限递归
        if head is None or head.next is None:
            return head

        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        #保存下一轮递归的入口
        next = head.next.next
        
        cur.next = pre  # 交换
        # 将以next为head的后续链表两两交换 ，递归调用swapPairs()，并等待返回结果，再赋值给节点的next
        pre.next = self.swapPairs(next)        
        return cur

    
##另一个版本（c++版本的python形式）
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)#定义并初始化一个虚拟头节点，创建一个新的ListNode实例通过关键字参数next=head把这个虚拟头节点的next指针指向原链表的真实头节点head
        current = dummy_head
        
        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next # 防止节点修改
            temp1 = current.next.next.next
            
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy_head.next
```

### 删除链表的倒数第N个节点

```plain
#题目

给定一个链表，删除链表的倒数第n个节点，并且返回链表的头节点
```

##### 思路

如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了

分为如下几步：

- 使用虚拟头结点，这样方便处理删除实际头结点的逻辑
- 定义fast指针和slow指针，初始值为虚拟头结点，如图：

![img](https://file1.kamacoder.com/i/algo/19.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.png)

- fast首先走n + 1步 ，为什么是n+1呢，因为只有这样同时移动的时候slow才能指向删除节点的上一个节点（方便做删除操作），如图： ![img](https://file1.kamacoder.com/i/algo/19.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B91.png)
- fast和slow同时移动，直到fast指向末尾，如图： ![img](https://file1.kamacoder.com/i/algo/19.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B92.png) 
- 删除slow指向的下一个节点，如图： ![img](https://file1.kamacoder.com/i/algo/19.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B93.png)

C++代码：

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* slow = dummyHead;
        ListNode* fast = dummyHead;
        //可以倒着想：快指针每前进一步的依据是倒数第n个节点中的n在从最后空指针null开始向后移动，fast由dummyhead到链表第1个节点即null到倒数第一个指针；n=0时，fast走了n步，应该指向的是第n个节点，比low快了n步，此时如果快慢指针同时移动，fast要走到null，需要sz-n+1步，此时low也走了这么多步，但不幸的是要删除倒数第n个节点即删除正数第sz-n+1个节点，而此时low指向的就是要删除的节点，这是不对的，要指向需删除节点的前一个节点才能实现删除该节点，因此在快慢指针同时移动前，快指针要比low快n+1步，因此fast要在while循环结束后再多走一步
        while(n-- && fast != NULL) {
            fast = fast->next;
        }
        fast = fast->next; // fast再提前走一步，因为需要让slow指向删除节点的上一个节点
        while (fast != NULL) {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next; 
        
        // ListNode *tmp = slow->next;  C++释放内存的逻辑
        // slow->next = tmp->next;
        // delete tmp;
        
        return dummyHead->next;
    }
};
```

Python代码

```python
#快慢指针法
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)
        
        # 创建两个指针，慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head
        
        # 快指针比慢指针快 n+1 步
        for i in range(n+1):
            fast = fast.next
        
        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next
        
        return dummy_head.next
    
#转倒数为正数法
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 步骤1：创建虚拟头节点，统一删除逻辑（包括删除原头节点的情况）
        dummy_head = ListNode(0, head)
        
        # 步骤2：统计链表的总节点数 sz
        sz = 0
        current = head  # 从真实头节点开始统计
        while current is not None:
            sz += 1
            current = current.next
        
        # 步骤3：找到要删除节点的「前驱节点」（用t计数控制移动）
        cur = dummy_head  # 从虚拟头节点开始移动
        t = 0  # 初始化计数器t
        # 循环条件：t < sz - n （移动到要删除节点的前驱位置）
        # 解释：sz-n 是前驱节点的位置（从0开始数），比如sz=5，n=2，sz-n=3，cur移动到第3个位置（t=3）
        while t < sz - n:
            cur = cur.next
            t += 1
        
        # 步骤4：删除目标节点（跳过cur的下一个节点）
        cur.next = cur.next.next
        
        # 步骤5：返回新链表的头节点（虚拟头的下一个）
        return dummy_head.next
```

### 链表相交

```plain
#题目

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
题目数据保证整个链式结构中不存在环，函数返回结果后链表必须保持原始结构
```

#### 思路

注意链表相交的定义⚠️：**节点的内存地址相同**，即==两个链表共享同一个物理节点==，一旦两个链表相交，从相交节点开始后面的所有节点必然都是同一个（因为节点的`next`指针指向的是固定地址），不可能出现交点后节点不重合的情况

本题就是求两个链表交点节点的指针	交点不是数值相等而是**指针**相等（同一个内存地址的节点）

利用**==相交链表的尾部一定重合==**来解决**两个链表起点不同，无法直接同时遍历找交点**

为了方便举例，假设节点元素数值相等，则节点指针相等。

看如下两个链表，目前curA指向链表A的头结点，curB指向链表B的头结点：

![面试题02.07.链表相交_1](https://file1.kamacoder.com/i/algo/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4_1.png)

求出两个链表的长度，并求出两个链表长度的差值gap，然后让curA移动gap步，实现两个链表的指针尾部对齐（即两个指针到链表末尾的节点数完全相同），如图：

![面试题02.07.链表相交_2](https://file1.kamacoder.com/i/algo/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4_2.png)

此时我们就可以比较curA和curB是否相同，如果不相同，同时向后移动curA和curB，如果遇到curA == curB，则找到交点。

> 解释一下：两个指针已经实现了尾部对齐，同时让两个指针向后遍历，指针相等的第一个节点就是相交节点

否则循环退出返回空指针。

C++代码

```c++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA;
        ListNode* curB = headB;
        int lenA = 0, lenB = 0;
        while (curA != NULL) { // 求链表A的长度
            lenA++;
            curA = curA->next;
        }
        while (curB != NULL) { // 求链表B的长度
            lenB++;
            curB = curB->next;
        }
        curA = headA;
        curB = headB;
        //不论链表A和B谁长谁短，强制让curA指向更长的链表，简化了逻辑，便于统一处理
        //比如B比A长，则把B的长度给A，让curA指向B的头；同样对B操作
        if (lenB > lenA) {
            swap (lenA, lenB);
            swap (curA, curB);
        }
        // 求长度差
        int gap = lenA - lenB;
        // 让curA和curB在同一起点上（末尾位置对齐）
        while (gap--) {
            curA = curA->next;
        }
        // 遍历curA 和 curB，遇到相同则直接返回
        while (curA != NULL) {
            if (curA == curB) {
                return curA;
            }
            curA = curA->next;
            curB = curB->next;
        }
        return NULL;
    }
};
```

Python代码

```python
#同时出发，代码复用，在函数内部调用别的函数，简化代码
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        # 通过移动较长的链表，使两链表长度相等
        if lenA > lenB:
            headA = self.moveForward(headA, lenA - lenB)
        else:
            headB = self.moveForward(headB, lenB - lenA)
        
        # 将两个头向前移动，直到它们相交
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

    #求链表的长度    
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    #根据两个链表长度的差值向前移动较长链表的指针，实现指针的尾部对齐
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    
#等比例法
#两个指针pointerA、pointerB 分别从 headA、headB 出发，遍历到自身链表末尾后，切换到另一个链表的头部继续遍历。
#循环的核心：指针没到末尾则向后走，到末尾则切换到另一个链表的头；循环终止条件是指针相等（交点或者都为None），如果链表相交则两个指针会在相交节点相遇，不相交则会同时走到None，总路程均相等
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况（空链表），如果任意一个链表为空则不可能有相交节点，直接返回None
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA
#Python的三元表达式 a = b if c else d 等价于
#if c:
#	a = b
#else:
#	a = d
```

### 环形链表II

```plain
#题目

给定一个链表的头节点head，返回链表开始入环的第一个节点。如果链表无环，则返回null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。
```

#### 思路

既然是环形，就可以考虑快慢指针，快指针能否追上慢指针，如果可以的话那就说明链表示环形的。定义`fast`和`slow`指针，从头节点出发，fast每次移动两个节点，slow每次移动一个节点，如果fast和slow指针在途中相遇这说明这个链表有环

fast指针一定先进入环中，如果fast指针和slow指针相遇的话，一定是在环中相遇的

画一个环，然后让 fast指针在任意一个节点开始追赶slow指针。

会发现最终都是这种情况， 如下图：

![142环形链表1](https://file1.kamacoder.com/i/algo/20210318162236720.png)

fast和slow各自再走一步， fast和slow就相遇了

这是因为fast是走两步，slow是走一步，**其实相对于slow来说，fast是一个节点一个节点的靠近slow的**，所以fast一定可以和slow重合。

动画如下：

![141.环形链表](https://file1.kamacoder.com/i/algo/141.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.gif)

此时已经能判断链表是否有环了，接下来要找到这个环的入口

假设从头节点到环形入口节点的节点数为x；环形入口节点到fast指针与slow指针相遇节点的节点数为y。从相遇节点再到环形入口节点的节点数为z

![20220925103433](https://file1.kamacoder.com/i/algo/20220925103433.png)

那么相遇时： slow指针走过的节点数为: `x + y`， fast指针走过的节点数：`x + y + n (y + z)`，n为fast指针在环内走了n圈才遇到slow指针， （y+z）为 一圈内节点的个数A。

> 为什么第一次在环中相遇，slow的步数是x+y而不是x+若干个环的长度+y呢
>
> 需要厘清如下三点：
>
> 1. **速度差**：fast一次走2步，slow一次走1步，fast相对于slow的速度是1步/次
> 2. **入环顺序**：fast速度更快，一定是fast先入环，slow后入环
> 3. **环的闭合性**：slow刚入环时，fast和slow之间的追击距离一定小于环的长度，那么可以看作slow静止，fast以1步/次的速度去追slow，所需要的次数绝对小于环的长度，再让slow动起来，说明slow走的路程绝对小于环的长度——>可以得到slow进环后走不足1圈就会被追上

因为fast指针是一步走两个节点，slow指针一步走一个节点， 所以 fast指针走过的节点数 = slow指针走过的节点数 * 2：

```
(x + y) * 2 = x + y + n (y + z)
```

两边消掉一个（x+y）: `x + y = n (y + z)`

因为要找环形的入口，那么要求的是x，因为x表示 头结点到 环形入口节点的的距离。

所以要求x ，将x单独放在左面：`x = n (y + z) - y` ,

再从n(y+z)中提出一个 （y+z）来，整理公式之后为如下公式：`x = (n - 1) (y + z) + z` 注意这里n一定是大于等于1的，因为 fast指针至少要多走一圈才能相遇slow指针。

这个公式说明什么呢？

先拿n为1的情况来举例，意味着fast指针在环形里转了一圈之后，就遇到了 slow指针了。

当 n为1的时候，公式就化解为 `x = z`，

这就意味着，**从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点**。

也就是在相遇节点处，定义一个指针index1，在头结点处定一个指针index2。

让index1和index2同时移动，每次移动一个节点， 那么他们相遇的地方就是 环形入口的节点。

动画如下：

![142.环形链表II（求入口）](https://file1.kamacoder.com/i/algo/142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II%EF%BC%88%E6%B1%82%E5%85%A5%E5%8F%A3%EF%BC%89.gif)

那么 n如果大于1是什么情况呢，就是fast指针在环形转n圈之后才遇到 slow指针。

其实这种情况和n为1的时候 效果是一样的，一样可以通过这个方法找到 环形的入口节点，只不过，index1 指针在环里 多转了(n-1)圈，然后再遇到index2，相遇点依然是环形的入口节点。

代码如下：

```c++
//定义链表结构体
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        //因为fast指针是走两步的，所以需要确保fast指向的节点不为空，fast的下一个节点也不为空
        while(fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            // 快慢指针相遇，此时从head 和 相遇点，同时查找直至相遇
            if (slow == fast) {
                ListNode* index1 = fast;//标记相遇点，也可以写成slow
                ListNode* index2 = head;//标记头节点
                while (index1 != index2) {
                    index1 = index1->next;
                    index2 = index2->next;
                }
                return index2; // 返回环的入口，自然也可以写成index1
            }
        }
        return NULL;
    }
};

//时间复杂度O(n)，快慢指针相遇前，指针走的次数小于链表长度，快慢指针相遇后，两个index指针走的次数也小于链表长度，总体为走的次数小于2n
```

Python代码

```python
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
#快慢指针法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None
    
#集合法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head#如果在集合中访问到了节点，那么就是环形的头节点
            visited.add(head)#将不在集合中的节点加入到集合之中
            head = head.next
        
        return None
```

### 链表__总结

#### 虚拟头节点

链表的一大问题就是操作当前节点必须要找前一个节点才能操作，但是头节点没有前一个节点

**每次对应头节点的情况都要单独处理，所以使用虚拟头节点就可以几觉这个问题**

#### 链表的基本操作

- 获取链表第index个节点的数值
- 在链表的最前面插入一个节点
- 在链表的最后面插入一个节点
- 在链表第index个节点前面插入一个节点
- 删除链表的第index个节点的数值

#### 反转链表

迭代法&&递归法

#### 删除倒数第N个节点

虚拟头节点+双指针法

#### 链表相交

双指针法找到两个链表的交点（引用完全相同，即内存地址完全相同的交点）
链表相交的物理意义是：**两个链表在某个节点处合并成了一个链**，本质就是共享后续节点，这是只有在**地址相同**时才成立的。

> 链表的每个`ListNode`节点在计算机中是一块独立的内存空间，每个节点的地址在内存中是独一无二的，节点的`val`是可以重复的，节点的`next`指针里存储的是**下一个节点的内存地址**
> 总结；一个链表节点，由**唯一的内存地址+可重复的val+存下一个地址的next指针**组成，计算机识别节点的唯一依据是内存地址
>
> 两个链表交点的定义是链表A和链表B在遍历过程中走到了**同一个内存地址**的节点，即两个链表共享了**这个节点**以及这个节点**之后的所有节点**
> 原因很简单：如果节点 C 是地址相同的交点，那么 C 的`next`指针里存的是下一个节点 D 的**唯一内存地址**，不管是从 A 链表访问`C.next`，还是从 B 链表访问`C.next`，得到的都是 D 的同一个地址，因此 D 也必然是共享节点，后续所有节点都会完全重合（地址都相同）。
>
> 代码判断两个节点是否是交点，用的是**直接比较节点变量**，这个判断的本质是比较节点的内存地址/引用，而不是比较节点的val

#### 环形链表

代码简单，主要在于数学证明

---

## 哈希表

### 哈希表理论基础

哈希表英文名为`Hash table`

> 哈希表是根据**关键码**的值而直接进行访问的数据结构

通俗来说,数组就是一张**哈希表**,哈希表中**关键码**就是数组的**索引下标**,可以通过下标直接访问数组中的元素

![哈希表1](https://file1.kamacoder.com/i/algo/20210104234805168.png)

**哈希表一般是用来快速判断一个元素是否出现在集合里**

> 例如要查询一个名字是否在这所学校里
>
> 枚举的时间复杂度是O(n),哈希表则只需要O(1)就可以做到
>
> 只需要初始化时把这所学校里学生的名字都存在哈希表里，在查询的时候通过索引直接就可以知道这位同学在不在这所学校里了。
>
> 将学生姓名映射到哈希表上就涉及到了**hash function ，也就是哈希函数**

#### 哈希函数

哈希函数如下图所示,通过hashCode把名字转化为数值,一般hashcode是通过特定编码方式,可以将其他数据格式转化为不同的数值,这样就把学生的名字映射为哈希表上的索引数字了

![哈希表2](https://file1.kamacoder.com/i/algo/2021010423484818.png)

如果hashCode得到的数值大于哈希表的大小了,为了保证映射出来的索引数字都落在哈希表上,可以对数值做一个取模的操作,这样就可以保证学生姓名一定可以映射到哈希表上了

如果学生的数量大于哈希表的大小，此时就算哈希函数计算的再均匀，也避免不了会有几位学生的名字同时映射到哈希表同一个索引下标的位置

由此就引出了**哈希碰撞**

#### 哈希碰撞

如图所示，小李和小王都映射到了索引下标 1 的位置，**这一现象叫做哈希碰撞**。

![哈希表3](https://file1.kamacoder.com/i/algo/2021010423494884.png)

哈希碰撞有两种解决方法:

- **拉链法（链地址法）**

  > 哈希表的底层是一个普通的**数组**，每个数组下标只能存放一个键值对。
  > 哈希碰撞的本质是不同的key通过哈希函数计算后得到了**相同的数组下标**
  > 拉链法就是把第一个到达哈希表中某个下标的元素作为**链表**的头节点存入，但后续元素哈希岛爱同一个位置时，就把这个元素**追加到该位置的链表末尾**；查找/删除元素时，先通过哈希函数定位对应的数组下标，再遍历对应下标内的链表来找到目标元素
  >
  > ```python
  > #python模拟哈希碰撞中拉链法的实现
  > class HashTable:
  >     def __init__(self, size=10):
  >         # 初始化哈希表：每个桶是一个空列表（模拟链表）
  >         self.size = size#定义哈希表底层数组的长度（桶的数量）
  >         #哈希表的核心存储结构_一个数组，数组中的每个元素都是空列表，用列表模拟链表
  >         self.buckets = [[] for _ in range(self.size)]
  >     
  >     # 简单的哈希函数：取模运算
  >     def _hash(self, key):#方法名前的_是Python的约定，代表是有方法，只在类内部用
  >         #hash(key)是内置函数，把所有可哈希对象生成一个唯一的整数哈希值
  >         #slif.size取模运算，把哈希值压缩
  >         return hash(key) % self.size 
  >     
  >     # 插入元素
  >     def put(self, key, value):
  >         #定位桶，先调用_hash方法算出key对应的桶下标
  >         bucket_index = self._hash(key)
  >         #拿到对应的桶（列表/链表）
  >         bucket = self.buckets[bucket_index]
  >         
  >         # 遍历桶里的元素，每个元素是(key,value)元组，检查key是否已存在，存在则更新值，保证一个key只有一个值
  >         for i, (k, v) in enumerate(bucket):
  >             if k == key:
  >                 bucket[i] = (key, value)
  >                 return
  >         # 处理碰撞/新增，不存在则追加到链表末尾
  >         bucket.append((key, value))
  >     
  >     # 获取元素
  >     def get(self, key):
  >         bucket_index = self._hash(key)
  >         bucket = self.buckets[bucket_index]
  >         
  >         # 遍历桶内的链表找目标key
  >         for k, v in bucket:
  >             if k == key:
  >                 return v
  >         # 没找到返回None
  >         return None
  > 
  > # 测试（修改后，确保碰撞）
  > ht = HashTable()
  > # 用数字key构造必然碰撞：5和15取模10都等于5，会放到同一个桶里
  > ht.put(5, 5)
  > ht.put(15, 10)  # 和5撞桶
  > ht.put(25, 15)  # 继续撞桶
  > ht.put("banana", 3)
  > 
  > print(ht.get(5))   # 输出：5
  > print(ht.get(15))  # 输出：10
  > print(ht.buckets)  # 能看到下标为5的桶里有3个元素！
  > ```

  刚刚小李和小王在索引1的位置发生了冲突，发生冲突的元素都被存储在链表中。 这样我们就可以通过索引找到小李和小王了

  ![哈希表4](https://file1.kamacoder.com/i/algo/20210104235015226.png)

  数据规模是dataSize,哈希表的大小是tableSize
  拉链法就是要选择适当的哈希表的大小,这样既不会因为数组空值而浪费大量内存,也不会因为链表太长而在查找上浪费太多时间

- **线性探测法**
  使用线性探测法时一定要保证**哈希表大小大于数据规模**,需要**依靠哈希表中的空位**来解决碰撞问题
  例如冲突的位置，放了小李，那么就**向下找一个空位**放置小王的信息。所以要求tableSize一定要大于dataSize ，要不然哈希表上就没有空置的位置来存放 冲突数据了。如图所示：
  ![哈希表5](https://file1.kamacoder.com/i/algo/20210104235109950.png)

#### 常见的三种哈希结构

有如下三种数据结构可以使用哈希法来解决问题:

- 数组(数据量少时优先用数组)
- 集合set
- 映射map

> 这里与教程略有不同,因为无C++基础,因此选择用python语言作通俗解释.[原文](https://www.programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E5%B8%B8%E8%A7%81%E7%9A%84%E4%B8%89%E7%A7%8D%E5%93%88%E5%B8%8C%E7%BB%93%E6%9E%84)
>
> 在C++中，set 和 map 分别提供以下三种数据结构，其底层实现以及优劣如下表所示：
>
> | 集合               | 底层实现 | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
> | ------------------ | -------- | -------- | ---------------- | ------------ | -------- | -------- |
> | std::set           | 红黑树   | 有序     | 否               | 否           | O(log n) | O(log n) |
> | std::multiset      | 红黑树   | 有序     | 是               | 否           | O(logn)  | O(logn)  |
> | std::unordered_set | 哈希表   | 无序     | 否               | 否           | O(1)     | O(1)     |
>
> std::unordered_set底层实现为哈希表，std::set 和std::multiset 的底层实现是红黑树，红黑树是一种平衡二叉搜索树，所以key值是有序的，但key不可以修改，改动key值会导致整棵树的错乱，所以只能删除和增加。
>
> | 映射               | 底层实现 | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
> | ------------------ | -------- | -------- | ---------------- | ------------ | -------- | -------- |
> | std::map           | 红黑树   | key有序  | key不可重复      | key不可修改  | O(logn)  | O(logn)  |
> | std::multimap      | 红黑树   | key有序  | key可重复        | key不可修改  | O(log n) | O(log n) |
> | std::unordered_map | 哈希表   | key无序  | key不可重复      | key不可修改  | O(1)     | O(1)     |
>
> std::unordered_map 底层实现为哈希表，std::map 和std::multimap 的底层实现是红黑树。同理，std::map 和std::multimap 的key也是有序的（这个问题也经常作为面试题，考察对语言容器底层的理解）。
>
> 当我们要使用集合来解决哈希问题的时候，优先使用**unordered_set**，因为它的查询和增删效率是最优的，如果需要**集合是有序的，那么就用set**，如果要求**不仅有序还要有重复数据的话，那么就用multiset**。
>
> 那么再来看一下map ，在map 是一个key value 的数据结构，map中，对key是有限制，对value没有限制的，因为key的存储方式使用红黑树实现的。
>
> 其他语言例如：java里的HashMap ，TreeMap 都是一样的原理。可以灵活贯通。
>
> 虽然std::set和std::multiset 的底层实现基于红黑树而非哈希表，它们通过红黑树来索引和存储数据。不过给我们的使用方式，还是哈希法的使用方式，即依靠键（key）来访问值（value）。所以使用这些数据结构来解决映射问题的方法，我们依然称之为哈希法。std::map也是一样的道理。
>
> 这里在说一下，一些C++的经典书籍上 例如STL源码剖析，说到了hash_set hash_map，这个与unordered_set，unordered_map又有什么关系呢？
>
> 实际上功能都是一样一样的， 但是unordered_set在C++11的时候被引入标准库了，而hash_set并没有，所以建议还是使用unordered_set比较好，这就好比一个是官方认证的，hash_set，hash_map 是C++11标准之前民间高手自发造的轮子。
>
> ![哈希表6](https://file1.kamacoder.com/i/algo/20210104235134572.png)

| 哈希结构 | Python实现 |                 核心作用                  |
| :------: | :--------: | :---------------------------------------: |
|   数组   |  列表list  |        利用**整数索引**快速存取值         |
| 集合Set  |  集合set   | 快速判断“元素**是否存在**”(只存键,不存值) |
| 映射Map  |  字典dict  |   快速存储/查询**键值对**(既存键又存值)   |

- 列表`list`——数组哈希(最简单、最快的哈希)

利用列表的**整数索引**作为哈希键,索引本身就是哈希计算的结果,通过索引直接访问值

需要满足两个条件:

1. **键**能被转换为**连续的、范围不大的整数**
2. 只需要通过整数索引**快速存取值**

访问速度极快,内存占用小(连续内存)	灵活性差:只能用整数当键,且键的范围必须是连续的小范围

```python
# 数组哈希的Python实现
# 需求：统计字符串中每个小写字母出现的次数
s = "anagram"
# 用长度26的列表（对应a-z），初始值都是0
count = [0] * 26
for c in s:
    # 把字符转换成0-25的整数索引（a→0，b→1...）
    index = ord(c) - ord('a')#字符转索引,ord()函数返回这个字符对应的Unicode编码值,相当于给每个字符绑定一个整数索引值,a为0,b为1……
    count[index] += 1#计数,取列表中第index个位置的值加一

print(count[0])  # a出现的次数：3
print(count[13]) # n出现的次数：1
```

- 集合`set`——哈希集合(只关注“有没有”)

底层是哈希表实现,值存储**唯一的元素(键)**,不存储对应的值,用于判断元素是否存在或者对数据去重

判断存在性速度极快、自动去重	只能存键不能存值(比如无法统计字符出现了几次),元素必须是不可变类型(比如不能存列表)

```python
# 哈希集合的Python实现
# 需求：判断字符串是否有重复字符
s = "abcde"
char_set = set()
for c in s:
    if c in char_set:
        print("有重复字符")
        break
    char_set.add(c)
else:
    print("无重复字符")  # 输出：无重复字符
```

- 字典`dict`——哈希映射(键值对,最灵活)

底层是哈希表实现,存储**键值对**,键唯一,可以通过键快速找到对应值

当需要关联键和值时(比如统计任意字符的出现次数)或者当键不是连续整数时适用

灵活性高(键可以为各种不可变类型)、支持键值映射	速度慢内存占用大

```python
# 哈希映射的Python实现
# 需求：统计字符串中任意字符（包括中文、符号）的出现次数
s = "你好呀，你好！"
count_dict = {}
for c in s:
    # 键是字符，值是次数
    count_dict[c] = count_dict.get(c, 0) + 1#
    #count_dict,get(c,0)——安全获取字符的当前计数,dict.get(key,默认值)用来根据key获取对应值 get(c, 0)里的0是第一次统计时的临时默认值，不是提前给所有字符绑定的初始值
    #给key绑定的value是指这个key字符出现的次数

print(count_dict)  # 输出：{'你': 2, '好': 2, '呀': 1, '，': 1, '！': 1}
```

##### 三种哈希的小结

1. 当你的 “键” 是**连续小范围整数**（比如 0-25、0-9）→ 优先用**列表**（速度最快、最省内存）；
2. 只需要判断 **“元素是否存在”** 或 **“去重”**→ 用 set（简单直接）；
3. 需要存储**键值对**（比如字符→次数、ID→信息），或键是字符串 / 不规则数字→ 用 dict（最灵活）；
4. 三者的核心优势都是**O (1) 的查询效率**，这也是哈希结构的核心价值，区别只在 “是否存值”“键的类型”。

#### 总结

**需要快速判断一个元素是否出现在集合里的时候,就要考虑哈希法**

哈希法**牺牲空间换时间**,需要使用额外的数组,`set`或者是`map`来存放数据,才能实现快速查找

当出现**需要判断一个元素是否出现过的场景时也应优先考虑哈希法**

### 有效的字母异位词

[力扣原题](https://leetcode.cn/problems/valid-anagram/description/)

```plain
#题目

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
注:字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。
```

#### 思路

数据量小,可以优先考虑使用数组,来记录字符串s里字符出现的次数

本题中只出现了小写字符而且字符a到z的ASCII是26个连续的数值

判断一下字符串s= "aee", t = "eae",举例操作如下:

![242.有效的字母异位词](https://file1.kamacoder.com/i/algo/242.%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.gif)

定义一个数组`record`来记录字符串s里字符出现的次数

需要**==把字符映射到数组(即哈希表的索引下标)上==**,**因为字符a到字符z的ASCII是26个连续的数值，所以字符a映射为下标0，相应的字符z映射为下标25**

再遍历 字符串s的时候，**只需要将 s[i] - ‘a’ (索引下标)所在的元素做+1 操作即可，并不需要记住字符a的ASCII，只要求出一个相对数值就可以了。** 这样就将字符串s中字符出现的次数，统计出来了。

检查字符串t中是否出现了这些字符时，需要在遍历字符串t的时候，对t中出现的字符映射哈希表索引上的数值再做-1的操作。

那么最后检查一下，**`record`数组如果有的元素不为零0，说明字符串s和t一定是谁多了字符或者谁少了字符，return false。**

最后如果record数组所有元素都为零0，说明字符串s和t是字母异位词，return true。

时间复杂度为O(n)，空间上因为定义是的一个常量大小的辅助数组，所以空间复杂度为O(1)。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1#[]内是取出字符对应在数组中的下标索引值.如果出现某字符,则应该在数组对应的下标位置上加1
        for i in t:
            record[ord(i) - ord("a")] -= 1#在t字符串中出现则应该-1
        for i in range(26):
            #record数组如果有的元素不为零0，说明字符串s和t一定是谁多了字符或者谁少了字符
            if record[i] != 0:
                return False
        return True

#暴力解法(会超出时间限制,n^2的运行时长太长了)
#字母异位词的字符串长度一定相同
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 第一步：长度不同直接返回False（必要优化）
        if len(s) != len(t):
            return False
        
        # 把字符串t转成列表，方便标记已匹配的字符
        t_list = list(t)
        
        # 遍历s的每个字符
        for c in s:
            found = False	#found值初始化(每次第二个for循环结束后都要初始化)
            # 遍历t的列表找匹配
            for i in range(len(t_list)):
                if t_list[i] == c:#如果在字符串t中找到了与s中相同的字符c
                    # 找到后标记为已使用（避免重复匹配）
                    t_list[i] = None#找到了的字符c应该把值更新为None
                    found = True#标记found为True,表示在t中找到了与s中相同的字符c
                    break#如果找到了,则无需再去t中找匹配的字符c,直接跳转到下一字符c的查找过程
            # 如果当前字符在t中找不到匹配，直接返回False
            #因为要t中字符与s中字符完全匹配,如果有找不到的情况,则found=False,此时if not found可以化为if True,执行语句
            if not found:
            #还可以写成 if found == False:    
                return False
        
        # 所有字符都匹配成功
        return True
```

学习一下`C++`代码

```c++
class Solution {
public:
    bool isAnagram(string s, string t) {
        int record[26] = {0};//c++静态数组
        for (int i = 0; i < s.size(); i++) {
            // 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            // c++中字符char本质上就是一个整数，它存储的是该字符在ASCII表中的编码值
            // python中字符str本身不是数字，必须先用ord()函数获取对应的Unicode码点
            record[s[i] - 'a']++;
        }
        for (int i = 0; i < t.size(); i++) {
            record[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (record[i] != 0) {
                // record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return false;
            }
        }
        // record数组所有元素都为零0，说明字符串s和t是字母异位词
        return true;
    }
};
```

### 两个数组的交集

[力扣原题](https://leetcode.cn/problems/intersection-of-two-arrays/description/)

```plain
#题目

给定两个数组nums1和nums2，返回它们的交集。输出结果中的每个元素一定是唯一的。可以不考虑输出结果的顺序。
```

#### 思路

哈希数据结构`unordered_set`

![set哈希法](https://file1.kamacoder.com/i/algo/20220707173513.png)

当限制数值大小时,可以使用数组来做哈希的题目

但是当哈希值比较少、特别分散、跨度非常大时,使用数组就造成了**空间的极大浪费**

因此,本题更适合用set,`std::set`和`std::multiset`底层实现都是红黑树，`std::unordered_set`的底层实现是哈希表， 使用`unordered_set `读写效率是最高的，并不需要对数据进行排序，而且还不要让数据重复，所以选择`unordered_set`。

```c++
#include <vector>   // 引入vector容器头文件，是动态数组，用于存储输入数组和交集结果
#include <unordered_set>  // 引入无序哈希集合头文件，用于去重以及快速查找

using namespace std;  // 使用std命名空间，避免重复写std::

class Solution {
public:
    // 函数功能：求两个整数数组的交集（结果元素唯一）
    // 参数：nums1 - 第一个输入数组；nums2 - 第二个输入数组
    // 返回值：vector<int> - 两个数组的交集（无重复元素）
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // 1. 定义存放最终结果的无序集合
        // 用unordered_set是为了自动给结果去重（集合元素具有唯一性）
        unordered_set<int> result_set; // 存放结果，之所以用set是为了给结果集去重
        // 2. 将nums1转换为无序集合nums_set，目的：
        //    - 对nums1去重
        //    - 利用unordered_set O(1)的查找效率，比遍历数组快得多
        unordered_set<int> nums_set(nums1.begin(), nums1.end());
        // 3. 遍历nums2的每一个元素，逐个检查是否在nums1的集合里
        for (int num : nums2) {
            // 发现nums2的元素 在nums_set里又出现过
            // nums_set.find(num)：查找元素num，返回指向该元素的迭代器；若不存在，返回end();这句if语句的意思是如果find()找回来的不是“没找到”的标志（end()），就说明找到了这个元素。
            if (nums_set.find(num) != nums_set.end()) {
                result_set.insert(num);
            }
        }
        // 4. 把结果集合转换成vector数组返回（因为函数要求返回vector类型）
        // vector<int>(result_set.begin(), result_set.end())：把set的元素全部拷贝到vector里
        return vector<int>(result_set.begin(), result_set.end());
    }
};

//数组作哈希表
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> result_set; // 存放结果，之所以用set是为了给结果集去重
        int hash[1005] = {0}; // 定义一个数组，默认数值为0，为了防止越界，题目要求num在0——1000内，取1005个索引构成的数组
        for (int num : nums1) { // nums1中出现的数字在hash数组中做记录
            hash[num] = 1;
        }
        for (int num : nums2) { // nums2中出现话，result记录
            if (hash[num] == 1) {
                result_set.insert(num);
            }
        }
        return vector<int>(result_set.begin(), result_set.end());
    }
};
```

set占用空间比数组大,而且速度比数组慢,set把数值映射到key上都要做hash计算,耗时严重

```python
#Python解法

#使用字典和集合
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
 
#使用数组
#这里键为nums1/2中的整数,我们要统计的目标数字就是哈希表要映射的核心对象
#哈希函数————哈希值=键本身(数字本身)
#哈希值————数组的索引,count1/2的下标k
#值————count1/2[k]的数值,实现了用**哈希值**作为索引去存储对应的值
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001#初始化哈希表
        count2 = [0]*1001#数组索引=哈希值=键(数字本身),数组值是数字出现的次数
        result = []#用于存储结果的list
        for i in range(len(nums1)):#先遍历nums1,对于nums1中出现的不同整数对应的次数进行计数
            count1[nums1[i]]+=1#数组值是数字出现的次数,数组下标是键是数字本身
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):#如果对于同一个数字,在两个原数组中均有出现,则count1/2对应的数组值均大于0,那么乘积也应该大于0(充要条件)
            if count1[k]*count2[k]>0:
                result.append(k)#需要的是数字本身,那么就是需要增加数组下标k
        return result
    
#暴力解法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []#用于存储交集元素
        for i in range(len(nums1)):
            j = 0#重置循环变量
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    nums.append(nums1[i])#如果出现相等情况,就要添加这个数字
                    break#因为返回的结果不需要重复,所以当nuns1中的数字在nums2中已经找到时应该直接跳出while循环,移到nums1的下一个下标索引去查
                else:
                    j += 1#自增变量
        return list(set(nums))#删除重复元素并排序
```

**哈希表**:

- 通过一个**哈希函数**,把要存储的**键**转换成一个唯一的**哈希值**
- 用**哈希值**作为索引去存储对应的值

### 快乐数

[力扣原题](https://leetcode.cn/problems/happy-number/)

```plain
#题目

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
```

#### 思路

注意关键词**无限循环**:这个意思是说在求和的过程中`sum`会重复出现

[如前所述](#哈希表理论基础),**遇到需要快速判断一个元素是否出现在集合里的时候,考虑使用==哈希法==**

> **关键点**:每个位置上的数字的**平方和**能否重复出现?
> 如果`sum`重复出现,则说明又要掉入循环重新计算了,这就陷入了无限循环,因此`sum`绝对不能出现相同的数值,如果出现了就要`return false`,否则就一直找到`sum==1`为止

先来学习一下C++代码吧

```c++
class Solution {
public:
    
    // 辅助函数getSum,计算一个整数各位上数字的平方和
    // 19%10=9,19/10=1
    int getSum(int n) {
        int sum = 0;
        while (n) {//等价于n!=0,当n被拆完所有位后循环终止
            sum += (n % 10) * (n % 10);//取最后一位数字并计算平方,累加到sum
            n /= 10;//去掉最后一位,整数除法,比如19/10=1,1/10=0
        }
        return sum;
    }
    
    // 主函数,判断输入的整数是否为快乐数,核心是用unordered_set检测循环
    // unordered_set是C++的STL(Standard Template Library,标准模板库)中的无序集合容器:存储元素唯一,底层基于哈希表实现,元素无序,常用判断set.find(元素)!=set.end(),表示元素存在于集合中(if语句的意思是如果find()找回来的不是“没找到”的标志end()，就说明找到了这个元素)
    bool isHappy(int n) {
        unordered_set<int> set;//用于记录已经出现过的平方和,检测循环
        while(1) {//无限循环,直到找到1或检测到重复的sum(陷入循环求平方和之中)
            int sum = getSum(n);//计算当前n的各位平方和
            //下面几个if语句都是同级别的,按顺序从上往下执行
            if (sum == 1) {
                return true;
            }
            // 如果这个sum曾经出现过(if语句成立表示的是在set中找到了这个sum元素)，说明已经陷入了无限循环了，立刻return false
            if (set.find(sum) != set.end()) {
                return false;
            } else {
                set.insert(sum);
            }
            n = sum;//将平方和赋值给n,进入下一轮计算
        }
    }
};

//unordered_set的find操作是O(1),哈希表查找
//时间复杂度和空间复杂度均为O(logn)
```

再来看一下Python代码

```python
#使用集合
class Solution:
    def isHappy(self, n: int) -> bool:        
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)#把变量n除以10的商重新赋值给n，把余数赋值给r
            new_num += r ** 2
        return new_num

#使用数组
class Solution:
   def isHappy(self, n: int) -> bool:
       record = []
       while n not in record:
           record.append(n)
           new_num = 0
           n_str = str(n)
           for i in n_str:
               new_num+=int(i)**2
           if new_num==1: return True
           else: n = new_num
       return False

#使用快慢指针
#计算各位平方和的过程可以看成一个**链表遍历**:每个数字是链表的一个节点,计算平方和的操作就是从当前节点走到下一个节点.快乐数的迭代只有两种结局:一是走到节点1(链表终止);二是进入一个环形循环(永远走不到1)
#快慢指针就是用O(1)空间检测这个链表里有没有环
#在这里快指针速度是慢指针的2倍,只要存在环必然会相遇(相遇就说明迭代陷入了循环,非快乐数);如果快指针先走到1则循环会提前终止
class Solution:
   def isHappy(self, n: int) -> bool:        
       slow = n
       fast = n
       #只有在两个条件同时满足时循环才会执行
       #条件1:fast指针走1步的结果不是1,如果是1则为快乐数直接终止无需循环
       #条件2:fast指针走两步的结果有效(非0)此条件本质是保证能继续迭代，避免无意义循环.等价于self.get_sum(self.get_sum(fast)) != 0
       while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
           slow = self.get_sum(slow)
           fast = self.get_sum(self.get_sum(fast))
           if slow == fast:
               return False
       return True

   def get_sum(self,n: int) -> int: 
       new_num = 0
       while n:
           n, r = divmod(n, 10)
           new_num += r ** 2
       return new_num
```

### 两数之和

[力扣原题]()

```plain
#题目

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
```

暴力解法很简单,for循环就完事了

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
        return []
    
#看看人家的暴力法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

#### 思路

之前做过[有效的字母异位词](#有效的字母异位词),利用的是**数组**作为哈希表来解决哈希问题
[两个数组的交集](#两个数组的交集)是利用**set**作为哈希表来解决哈希问题

再次强调:**==当需要<u>查询一个元素是否出现过</u>,或者<u>一个元素是否在集合里</u>的时候要第一时间想到哈希法==**

本题,需要一个集合来存放**遍历过的元素**,在遍历数组的时候去询问这个集合,某元素是否遍历过(即是否出现在这个集合中)
本题不仅需要知道元素有没有遍历过,还要知道这个元素对应的下标,需要使用`key-value`结构来存放,`key`存元素,`value`存下标,使用map正合适不过了

> 使用 数组 和 set 来做哈希法的局限
>
> - 数组的大小受限制,如果元素很少又很分散,哈希值太大则会造成内存空间的浪费
> - set是一个集合,里面放的元素只能是一个key,本题中不仅要判断y是否存在而且还要记录y的下标位置,因为要返回x和y的下标,所以set也无法使用

这时就要选择另一种数据结构`map`,一种`key-value`结构

C++中map，有三种类型：

| 映射               | 底层实现 | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
| ------------------ | -------- | -------- | ---------------- | ------------ | -------- | -------- |
| std::map           | 红黑树   | key有序  | key不可重复      | key不可修改  | O(log n) | O(log n) |
| std::multimap      | 红黑树   | key有序  | key可重复        | key不可修改  | O(log n) | O(log n) |
| std::unordered_map | 哈希表   | key无序  | key不可重复      | key不可修改  | O(1)     | O(1)     |

std::unordered_map 底层实现为哈希表，std::map 和std::multimap 的底层实现是红黑树。

**明确map作用和存储的元素分别表示什么**

**map的目的是用来存放我们访问过的元素**，因为遍历数组的时候，需要记录我们之前遍历过哪些元素和对应的下标，这样才能找到与当前元素相匹配的（也就是相加等于target）

这道题 我们需要 给出一个元素，判断这个元素是否出现过，如果出现过，返回这个元素的下标。

那么**判断元素是否出现**，这个元素就要作为key，所以**数组中的元素作为key**，**有key对应的就是value，value用来存下标**。

所以map中的存储结构为 **{key：数据元素，value：数组元素对应的下标}**。

在遍历数组的时候，只需要**在map中去查询是否有和目前遍历元素匹配的数值，如果有，就找到匹配对，如果没有，就把目前遍历的元素放进map中，因为map存放的就是我们访问过的元素**。

过程如下：

![过程一](https://file1.kamacoder.com/i/algo/20220711202638.png)

![过程二](https://file1.kamacoder.com/i/algo/20230220223536.png)

C++代码：

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map <int,int> map;
        for(int i = 0; i < nums.size(); i++) {
            // 遍历当前元素，并在map中寻找是否有匹配的key
            //auto是C++11的自动类型推导,iter是unordered_map的迭代器,指向找到的键值对
            auto iter = map.find(target - nums[i]); 
            if(iter != map.end()) {
                //iter->second:迭代器指向的是pair<int,int>类型的键值对,first是key(元素值),second是value(下标)
                return {iter->second, i};
            }
            // 如果没找到匹配对，就把访问过的元素和下标加入到map中
            map.insert(pair<int, int>(nums[i], i)); 
        }
        return {};
    }
};

//时间复杂度O(n),空间复杂度O(n)
```

- 为什么用哈希表:**用空间换时间**,优化查找效率,`find`操作平均时间复杂度O(1),可以把已遍历过的元素存起来,每次找补数时直接查表,只需一次遍历就能完成
- 哈希表为什么用`map`:需要存储 “元素值 → 下标” 的映射关系,`map`（包括 `unordered_map`）的键值对结构正好满足这种映射存储
- `map`用来存什么:用来存储**已经遍历过的数组元素，以及它们在原数组中的下标**.遍历到当前元素时，我们需要知道 “之前是否出现过能和当前元素凑成 target 的补数”，所以把已遍历的元素存到 `map` 里，供后续查找补数使用

```python
#使用字典,对应C++的map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):  
            if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target- value], index]
            records[value] = index    # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []
    
#使用集合
#使用集合的话,后续找补数的下标索引又要回到手动遍历数组找下标,时间复杂度下降为暴力算法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #创建一个集合来存储我们目前看到的数字
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
			#nums.index(complement)是线性查找，这会让整体时间复杂度退化为O(n²)
                return [nums.index(complement), i]
            seen.add(num)

#使用双指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 对输入列表进行排序
        nums_sorted = sorted(nums)
        
        # 使用双指针
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                # 如果和等于目标数，则返回两个数的下标
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                #当两个数是重复值时，直接用nums.index()永远会返回这个值在原数组中第一次出现的下标，必须修正找到第二个重复值的真实位置（由前述可得第二个重复值必然出现在原数组第一次出现的右边）例如nums=[3,3] target=6 标准输出应为[0,1]or[1,0] 若不修正则返回[0,0]
                #nums[left_index+1:]切片,跳过已找到的第一个重复元素,只在第一个重复元素的后面部分找第二个重复元素避免再次找到同一个下标
                #.index(nums_sorted[right])在切片后的列表中找目标值的下标,这个下标是切片后子列表的局部下标,不是原数组的全局下标
                #+left_index+1转换为原数组的全局下标,切片是从left_index+1开始的,需要把局部下标还原为原数组的下标
                if left_index == right_index:
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif current_sum < target:
                # 如果总和小于目标，则将左侧指针向右移动
                left += 1
            else:
                # 如果总和大于目标值，则将右指针向左移动
                right -= 1
```

### 四数相加II

[力扣原题](https://leetcode.cn/problems/4sum-ii/description/)

```plain
#题目

给你四个整数数组nums1、nums2、nums3和nums4 ，数组长度都是n，请你计算有多少个元组 (i, j, k, l) 能满足：

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
```

#### 思路

在[有效字母异位词](#有效的字母异位词)中利用数组下标做映射,因为字母出现的个数可控
本题中元素数值不确定(可能很大),用数组下标做映射会浪费大量的内存空间,因此需要考虑使用`set`或者`map`

另外,直接用四个`for`循环时间复杂度太高了,想想能不能两两分组,直接能将时间复杂度减半.把这种思维运用到哈希法中,就是在A、B、C、D四个大的数组中,先找到`a+b`并记录相应的和以及这个和出现的次数,存入到`map`中,再在`map`中去寻找`-(c+d)`是否出现过,如果出现过就要统计出现的次数.因此要考虑使用`map`来做此题   `key—value`键值对

```C++
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> umap; //key:a+b的数值，value:a+b数值出现的次数
        // 遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到map中
        for (int a : A) {
            for (int b : B) {
                umap[a + b]++;//代表有多少种不同的(a,b)组合能得到该和
            }
        }
        int count = 0; // 统计a+b+c+d = 0 出现的次数
        // 再遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，就把map中key对应的value也就是出现次数统计出来。
        for (int c : C) {
            for (int d : D) {
                //如果存在,umap[target]代表能和当前(c,d)凑出0的(a,b)组合数量
                //这里每一次子循环找到的都是一组不同的(c,d),找到了就加上对应的umap[target]即可,如果下一组(c,d)的和同样满足这一个target值,继续往上加就是了
                if (umap.find(0 - (c + d)) != umap.end()) {
                    count += umap[0 - (c + d)];
                }
            }
        }
        return count;
    }
};

//时间复杂度和空间复杂度均为O(n^2)
```

`Python`代码

```python
#字典
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                #也可以用一个语句实现if——else的功能
                #hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        
        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count
```

### 赎金信

[力扣原题](https://leetcode.cn/problems/ransom-note/description/)

```plain
#题目

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
ransomNote和magazine均由小写英文字母组成
```

#### 思路

本题判断第一个字符串`ransom`能不能由第二个字符串`magazines`里面的字符构成，但是这里需要注意两点。

- 第一点“为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思” 这里*说明杂志里面的字母不可重复使用。*
- 第二点 “你可以假设两个字符串均只含有小写字母。” *说明只有小写字母*，这一点很重要

暴力解法很简单

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 转为列表，方便删除操作
		ran_list = list(ransomNote)
		for char in magazine:
    		i = 0  # 初始化变量i
    		while i < len(ran_list):
        		if char == ran_list[i]:
            		ran_list.remove(char)
            		break
       	 		i += 1
        
        # 最终判断ran_list是否为空（空则说明全部匹配成功）
        return len(ran_list) == 0

    
#标准一点的解法 while需要自增操作,for循环不需要
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 转为列表，方便删除操作
        mag_list = list(magazine)
        ran_list = list(ransomNote)
        
        # 外层for循环：遍历magazine的字符（用副本遍历，避免原列表变化影响遍历）
        for char in mag_list.copy():  # 关键：用copy()遍历，否则原列表删元素会漏遍历
            # 内层for循环：遍历ransomNote的字符，找匹配
            for j in range(len(ran_list)):
                if char == ran_list[j]:
                    # 匹配到，删除ran_list中的该字符
                    ran_list.pop(j)
                    # 同时删除mag_list中的该字符（避免重复使用）
                    mag_list.remove(char)
                    # 找到一个就跳出内层循环，继续匹配下一个mag字符
                    break
        
        # 最终判断ran_list是否为空
        return len(ran_list) == 0
```

```c++
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        for (int i = 0; i < magazine.length(); i++) {
            for (int j = 0; j < ransomNote.length(); j++) {
                // 在ransomNote中找到和magazine相同的字符
                if (magazine[i] == ransomNote[j]) {
                    // ransomNote删除这个字符
                    //ransomNote.begin()的作用是返回指向字符串第一个字符的迭代器(字符的指针),.begin()+j是把迭代器向后移动j个位置,指向ransomNote中下标为j的字符,erase(迭代器位置)本质上是和erase(下标位置,删除长度)等价的
                    ransomNote.erase(ransomNote.begin() + j); 
                    //ransomNote.erase(j,1);
                    break;
                }
            }
        }
        // 如果ransomNote为空，则说明magazine的字符可以组成ransomNote
        if (ransomNote.length() == 0) {
            return true;
        }
        return false;
    }
};
```

想法:均由小写字母构成的话,能否采用数组进行哈希映射?

当然可以选择用空间换时间的哈希策略,用一个长度为26的数组来记录magazine里字母出现的次数,再用ransomNote去验证这个数组是否包含了ransomNote所需要的所有字母

那么这里为什么不使用map呢?

因为map消耗的空间比数组要大,而且map要维护红黑树或者哈希表,需要做哈希函数,是很费时的.数据量大的时候就能体现出来差别,使用数组时更加简单高效的方法

> 什么时候用数组?什么时候用map?
>
> |     维度     |                          数组实现                          |                          Map 实现                           |
> | :----------: | :--------------------------------------------------------: | :---------------------------------------------------------: |
> | **适用场景** | 字符集**有限、连续且范围已知**（如小写英文字母、0-9 数字） | 字符集**未知、范围大或不连续**（如包含大写、符号、Unicode） |
> |   **效率**   |     更高（直接索引访问，时间复杂度 O(1)，无哈希开销）      |        稍低（哈希表的哈希计算、冲突处理有额外开销）         |
> |   **空间**   |           固定（如 26 个位置，空间复杂度 O(1)）            |   动态（随字符数量变化，空间复杂度 O(k)，k 为不同字符数）   |
> |  **灵活性**  |                 低（仅支持固定范围的字符）                 |                   高（支持任意字符类型）                    |
>
> #### 选择原则
>
> 1. **优先用数组**：当你明确知道字符的范围是有限且连续的（比如这道题的小写英文字母），数组的速度和空间效率都更优。
> 2. **必须用 Map**：当字符集不确定、范围大或包含多种类型时（比如处理任意输入字符串、包含特殊符号），Map 是唯一选择。
>
> 相比于set,数组和map还是很类似的,因为他们本质上是键值对的结构,本题中需要统计字符出现次数的值,所以用set无法解决
> 数组和map是有对应关系的存储,知道键就能找到值
> set是只有存在性的存储.只能知道键存不存在,不知道出现了几次
>
> - 字符集连续且范围固定,优先使用数组(效率最高)
> - 字符集任意/不连续,使用map
> - 只需要判断元素是否存在,使用set

```C++
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int record[26] = {0};
        //如果ransomNote长度都大于magazine了,那肯定不能在magazine里面找到构成ransom的字符
        if (ransomNote.size() > magazine.size()) {
            return false;
        }
        for (int i = 0; i < magazine.length(); i++) {
            // 通过record数据记录 magazine里各个字符出现次数
            record[magazine[i]-'a'] ++;//下标索引虽是数字但能代表字母符号,下标对应的值即为字母在字符串中的出现次数
        }
        for (int j = 0; j < ransomNote.length(); j++) {
            // 遍历ransomNote，在record里对应的字符个数做--操作
            record[ransomNote[j]-'a']--;
            // 如果小于零说明ransomNote里出现的字符，magazine没有（或者字符个数不够多）
            if(record[ransomNote[j]-'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};

//时间复杂度: O(m+n)，其中m表示ransomNote的长度，n表示magazine的长度
//空间复杂度: O(1)
```

```python
#数组
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
    
#使用字典_对应map
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for c in magazine:
            #counts.get(c,0),这是安全取值,如果字符c已经在counts中就返回当前的计数值,如果不在就返回默认值0,避免直接取counts[c]时报错
            counts[c] = counts.get(c, 0) + 1
        for c in ransomNote:
            #c在counts中不存在,或者计数值已经为0时(表示现在这个c在counts中找不到多余的c了)
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True
```

### 三数之和

[力扣原题](https://leetcode.cn/problems/3sum/description/)

```plain
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为0且不重复的三元组。

注意：答案中不可以包含重复的三元组。输出的顺序和三元组的顺序并不重要
```

#### 思路

两层for循环可以确定两个数值,使用哈希法来确定第三个数`0-(a+b)`是否在数组里出现过,不过本题中说不可以包含重复的三元组.把符合条件的三元组放进vector中再去去重十分费时

下面给出哈希法的C++_code_

```c++
class Solution {
public:
    // 在一个数组中找到3个数形成的三元组，它们的和为0，不能重复使用（三数下标互不相同），且三元组不能重复。
    // b（存储）== 0-(a+c)（检索）
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;//存储最终的三元组结果
        sort(nums.begin(), nums.end());//对原数组进行排序
        
        for (int i = 0; i < nums.size(); i++) {
            // 如果a是正数，a<b<c，不可能形成和为0的三元组
            if (nums[i] > 0)
                break;
            
            // [a, a, ...] 如果本轮a和上轮a相同，那么找到的b，c也是相同的，所以去重a
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            // 这个set的作用是存储b,用于存储内层循环中遍历过的元素
            unordered_set<int> set;
            
            for (int k = i + 1; k < nums.size(); k++) {
                // 去重b=c时的b和c
                if (k > i + 2 && nums[k] == nums[k - 1] && nums[k - 1] == nums[k - 2])
                    continue;
                
                // a+b+c=0 <=> b=0-(a+c)
                int target = 0 - (nums[i] + nums[k]);
                if (set.find(target) != set.end()) {
                    result.push_back({nums[i], target, nums[k]});   // nums[k]成为c
                    set.erase(target);
                }
                else {
                    set.insert(nums[k]);                            // nums[k]成为b
                }
            }
        }

        return result;
    }
};

//时间复杂度: O(n^2)
//空间复杂度: O(n)，额外的 set 开销
```

##### 双指针法

动画效果如下：

![15.三数之和](https://file1.kamacoder.com/i/algo/15.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.gif)

拿这个nums数组来举例，首先将数组**排序**，然后有一层**for循环，i从下标0的地方开始**，同时**定一个下标left定义在i+1的位置上，定义下标right在数组结尾的位置上**。

依然还是在数组中找到 abc 使得a + b +c =0，这里相当于 a = nums[i]，b = nums[left]，c = nums[right]。

接下来如何移动left 和right呢， 如果nums[i] + nums[left] + nums[right] > 0 就说明 此时三数之和大了，因为数组是排序后了，所以right下标就应该向左移动，这样才能让三数之和小一些。

如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。

时间复杂度：O(n^2)。

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        // 找出a + b + c = 0
        // a = nums[i], b = nums[left], c = nums[right]
        for (int i = 0; i < nums.size(); i++) {
            // 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
            if (nums[i] > 0) {
                return result;
            }
            
            // 错误去重a方法，将会漏掉-1,-1,2 这种情况
            /*
            if (nums[i] == nums[i + 1]) {
                continue;
            }
            */
            
            // 正确去重a方法,与前一位去比较,如果相同,说明前一位已经被使用过了,不应该要这一位
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            //定义双指针
            int left = i + 1;
            int right = nums.size() - 1;
            while (right > left) {
                // 去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致 right<=left 了，从而漏掉了 0,0,0 这种三元组
                /*
                while (right > left && nums[right] == nums[right - 1]) right--;
                while (right > left && nums[left] == nums[left + 1]) left++;
                */
                if (nums[i] + nums[left] + nums[right] > 0) right--;
                else if (nums[i] + nums[left] + nums[right] < 0) left++;
                else {
                    result.push_back(vector<int>{nums[i], nums[left], nums[right]});
                    // 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                    while (right > left && nums[right] == nums[right - 1]) right--;
                    while (right > left && nums[left] == nums[left + 1]) left++;

                    // 找到答案时，双指针同时收缩
                    right--;
                    left++;
                }
            }

        }
        return result;
    }
};
```

##### 去重的逻辑

**a的去重**

 a, b ,c, 对应的就是 nums[i]，nums[left]，nums[right]

a 如果重复了怎么办，a是nums里遍历的元素，那么应该直接跳过去。

> 既然a重复了需要跳过,那么需要判断nums[i]与nums[i+1]是否相同还是判断nums[i]与nums[i-1]是否相同

假设写法如下:

```text
if (nums[i] == nums[i + 1]) { // 去重操作
    continue;
}
```

那我们就把 三元组中出现重复元素的情况直接pass掉了。 例如{-1, -1 ,2} 这组数据，当遍历到第一个-1 的时候，判断 下一个也是-1，那这组数据就pass了。

**我们要做的是 不能有重复的三元组，但三元组内的元素是可以重复的！**

所以这里是有两个重复的维度。

那么应该这么写：

```text
if (i > 0 && nums[i] == nums[i - 1]) {
    continue;
}
```

这么写就是当前使用 nums[i]，我们判断前一位是不是一样的元素，在看 {-1, -1 ,2} 这组数据，当遍历到 第一个 -1 的时候，只要前一位没有-1，那么 {-1, -1 ,2} 这组数据一样可以收录到 结果集里。

**b与c的去重**

可能在写本题时,对于去重的逻辑多加了 对right 和left 的去重：（代码中注释部分）

```text
while (right > left) {
    if (nums[i] + nums[left] + nums[right] > 0) {
        right--;
        // 去重 right
        while (left < right && nums[right] == nums[right + 1]) right--;
    } else if (nums[i] + nums[left] + nums[right] < 0) {
        left++;
        // 去重 left
        while (left < right && nums[left] == nums[left - 1]) left++;
    } else {
    }
}
```

但细想一下，这种去重其实对提升程序运行效率是没有帮助的。

拿right去重为例，即使不加这个去重逻辑，依然根据 `while (right > left)` 和 `if (nums[i] + nums[left] + nums[right] > 0)` 去完成right-- 的操作。

多加了 `while (left < right && nums[right] == nums[right + 1]) right--;` 这一行代码，其实就是把 需要执行的逻辑提前执行了，但并没有减少 判断的逻辑。

最直白的思考过程，就是right还是一个数一个数的减下去的，所以在哪里减的都是一样的。

```python
#双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                      
                    #双侧指针收缩,缩小检索区间
                    right -= 1
                    left += 1
                    
        return result

#字典
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 找出a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(len(nums)):
            # 排序之后如果第一个元素已经大于零，那么不可能凑成三元组
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: #三元组元素a去重
                continue
            d = {}
            s = set()  
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]:  # 去重b
                    continue
                
                c = 0 - (nums[i] + nums[j])
                if c in s:
                    result.append([nums[i], nums[j], c])
                    s.remove(c)  # 去重c
                else:
                    s.add(nums[j])  # 存入当前nums[j]作为候选
        
        return result
```

### 四数之和

[力扣原题](https://leetcode.cn/problems/4sum/description/)

```plain
#题目

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。答案中不可以包含重复的四元组
```







### 哈希表__总结







---

## 字符串

### 反转字符串

```plain
#题目

编写函数将输入的字符串反转，输入字符串以字符数组char[]的形式给出
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
```

#### 思路

如果题目关键的部分可以直接使用库函数解决时，那就不要用库函数

如果库函数只是解题过程中的一小部分，并且库函数的内部实现原理十分清晰时，可以考虑使用库函数

反转字符串可以参考[反转链表](#反转链表)，反转链表中使用了双指针的方法，这里仍然可以借鉴

字符串也是一种数组，所以元素在内存中是**连续分布**的，这就决定了反转链表和反转字符串方式上是有所差异的

对于字符串，我们定义两个指针（也可以说是索引下标），一个从字符串前面，一个从字符串后面，两个指针同时向中间移动，并交换元素。

以字符串`hello`为例，过程如下：

![344.反转字符串](https://file1.kamacoder.com/i/algo/344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.gif)

不难写出如下C++代码:

```cpp
void reverseString(vector<char>& s) {
    for (int i = 0, j = s.size() - 1; i < s.size()/2; i++, j--) {
        swap(s[i],s[j]);
    }
}
```

循环里只要做交换s[i] 和s[j]操作就可以了，那么我这里使用了swap 这个库函数。大家可以使用。

因为相信大家都知道交换函数如何实现，而且这个库函数仅仅是解题中的一部分， 所以这里使用库函数也是可以的。

swap可以有两种实现。

一种就是常见的交换数值：

```cpp
int tmp = s[i];
s[i] = s[j];
s[j] = tmp;
```

一种就是通过位运算：

```cpp
s[i] ^= s[j];
s[j] ^= s[i];
s[i] ^= s[j];
```

如果题目关键的部分直接用库函数就可以解决，建议不要使用库函数。

如果库函数仅仅是 解题过程中的一小部分，并且你已经很清楚这个库函数的内部实现原理的话，可以考虑使用库函数。

**在字符串相关的题目中，库函数对大家的诱惑力是非常大的，因为会有各种反转，切割取词之类的操作**，这也是为什么字符串的库函数这么丰富的原因。

C++代码如下：

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i = 0, j = s.size() - 1; i < s.size()/2; i++, j--) {
            swap(s[i],s[j]);
        }
    }
};
```

Python

```python
#双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(len(s)//2)更低
        # 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。推荐使用range
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
 
#使用栈 先进后出，后进先出
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()
       
#使用range
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
            
#或者使用切片		s[:] = s[::-1]
#使用列表推导		s[:] = [s[i] for i in range(len(s)-1,-1,-1)]	
#使用反转		s.reverse()		s[:] = reversed(s)
```

### 反转字符串II

```plain
#题目

给定一个字符串s和一个整数k；从字符串开头算起，每计数至2k个字符，就反转这2k个字符中的前k个字符
如果剩余字符少于k个，则将剩余字符全部反转
如果剩余字符小于2k单大于或者等于k个，则反转前k个字符，其余字符保持原样
```

#### 思路



### 替换数字

```plain
#题目

给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。
```

#### 思路

扩充数组到每个数字支付替换成`number`之后的大小

例如 字符串 "a5b" 的长度为3，那么 将 数字字符变成字符串 "number" 之后的字符串为 "anumberb" 长度为 8。

![20231030165201](https://file1.kamacoder.com/i/algo/20231030165201.png)

**从后向前替换数字字符**，也就是双指针法，过程如下：i指向新长度的末尾，j指向旧长度的末尾。

![img](https://file1.kamacoder.com/i/algo/20231030173058.png)

为什么要从后向前填充，从前向后填充不行么？

>  从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素整体向后移动。

**其实很多==数组填充类==的问题，其做法都是==先预先给数组扩容带填充后的大小==，然后再==从后向前进行操作==。**

这么做有两个好处：

1. 不用申请新数组。
2. 从后向前填充元素，避免了**从前向后填充元素时，每次添加元素都要将添加元素之后的所有元素向后移动**的问题。

C++_code

```c++
#include <iostream>
using namespace std;
int main() {
    string s;
    while (cin >> s) {
        int sOldIndex = s.size() - 1;
        int count = 0; // 统计数字的个数
        for (int i = 0; i < s.size(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                count++;
            }
        }
        // 扩充字符串s的大小，也就是将每个数字替换成"number"之后的大小
        s.resize(s.size() + count * 5);
        int sNewIndex = s.size() - 1;
        // 从后往前将数字替换为"number"
        while (sOldIndex >= 0) {
            if (s[sOldIndex] >= '0' && s[sOldIndex] <= '9') {
                s[sNewIndex--] = 'r';
                s[sNewIndex--] = 'e';
                s[sNewIndex--] = 'b';
                s[sNewIndex--] = 'm';
                s[sNewIndex--] = 'u';
                s[sNewIndex--] = 'n';
            } else {
                s[sNewIndex--] = s[sOldIndex];
            }
            sOldIndex--;
        }
        cout << s << endl;       
    }
}
```

Python_code

```python
class Solution(object):
    def subsitute_numbers(self, s):
        """
        :type s: str
        :rtype: str
        """#参数s是字符串，返回值也是字符串
        
        count = sum(1 for char in s if char.isdigit()) # 统计数字的个数
        expand_len = len(s) + (count * 5)  # 计算扩充后字符串的大小， x->number， 每有一个数字就要增加五个长度
        #创建固定长度的空列表，预分配内存地址，避免动态扩容
        res = [''] * expand_len
        
        new_index = expand_len - 1 # 指向扩充后字符串末尾
        old_index = len(s) - 1 # 指向原字符串末尾
        
        while old_index >= 0: # 从后往前， 遇到数字替换成“number”
            if s[old_index].isdigit():
                res[new_index-5:new_index+1] = "number"
                new_index -= 6
            else:
                res[new_index] = s[old_index]
                new_index -= 1
            old_index -= 1
        
        return "".join(res)

#主程序入口
if __name__ == "__main__":
    solution = Solution()

    while True:
        try:
            s = input()
            result = solution.subsitute_numbers(s)
            print(result)
        except EOFError:
            break
```

### 翻转字符串里的单词

```plain
#题目

给定一个字符串，逐个翻转字符串中的每个单词
```



### 右旋转字符串



### 实现strStr()函数——KMP算法

```plain
#题目

实现strStr()函数
给定一个haystack字符串和一个needle字符串，在haystack字符串中找出needle字符串出现的第一个位置。如果不存在则返回-1
```

#### KMP算法

这道题时经典的KMP算法题，用于解决字符串匹配问题

比如，文本串`aabaabaaf`，模式串`aabaaf`，求在文本串中是否出现过模式串

KMP的思想就是：**当出现字符串不匹配时，可以记录一部分之前已经匹配的文本内容，利用这些信息避免从头再去做匹配**

##### 前缀表

前缀表主要用于**回退**，它记录了模式串与文本串不匹配的时候，模式串应该从哪里开始重新匹配

next数组就是一个前缀表`prefix table`

通过一个例子来展示前缀表：要在文本串`aabaabaafa`中查找是否出现过一个模式串`aabaaf`

![KMP详解1](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B21.gif)

可以看到文本串中第六个字符b和模式串的第六个字符f不匹配了。如果用暴力匹配，就要从头开始匹配

如果使用前缀表匹配，那么就是从上次已经匹配的内容开始匹配，找到了模式串中第三个字符b继续开始匹配

前缀表的任务是当前位置匹配失败，找到之前已经匹配上的位置，再重新匹配，这也意味着在某个字符失配时，前缀表会告诉你下一步匹配中，模式串应该跳到哪个位置

前缀表：记录模式串中每个位置`j`的**最长相等前后缀长度**，当匹配失败时，告知`j`应该回退到哪个位置

##### 最长相等前后缀

- **前缀&&后缀**

  - 前缀：不包含最后一个字符且以第一个字符开头的所有连续子串
  - 后缀：不包含第一个字符且以最后一个字符结尾的所有连续子串
  - 举例：对于一个字符串`t='aabaa'`，它的前缀组成的列表为`['a','aa','aab','aaba']`，它的后缀组成的列表为`["a", "aa", "baa", "abaa"]`

- **最长相等前后缀**

  前缀和后缀中**长度最长且内容相等**的子串长度
  在上例中，最长的子串是`aa`，所以长度为2

##### 前缀表必要性

前缀表为什么能告诉我们上次匹配的位置并跳过

回顾之前匹配的过程，发现在下标5的地方遇到不匹配，模式串是指向f，字符串指向b

![KMP精讲1](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B21.png)

![KMP精讲2](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B22.png)

然后就找到了下标2，指向b，继续匹配

**下标5之前这部分的字符串（也就是字符串`aabaa`）的最长相等的 前缀 和 后缀字符串是 子字符串`aa` ，因为找到了最长相等的前缀和后缀，匹配失败的位置是后缀子串的后面，那么我们找到与其相同的前缀的后面重新匹配就可以了。**

所以前缀表具有告诉我们当前位置匹配失败，跳到之前已经匹配过的地方的能力。

假设有文本串`... a a b a a X ...`，现在有模式串`a a b a a f`；此时模式串的前5个字符`aabaa`和文本串对应位置时完全匹配的，目标是找到模式串的一个**新的起始位置**继续匹配且**不回退文本串的指针**

已匹配的`aabaa`的最长相等前后缀是`aa`，意味着：
文本串中已匹配的最后2个字符（后缀）是`aa`
模式串中已匹配的最前2个字符（前缀）是`aa`
因为文本串和模式串的`aabaa`完全匹配，所以文本串的后缀`aa`=模式串的前缀`aa`

已知匹配失败在`f`，说明文本串的`X`不等于`f`，但是文本串的后缀`aa`是确定匹配的，是和模式串开头的`aa`完全一样的，那这部分`aa`就不需要重新匹配了——直接把模式串的 “前缀`aa`” 对齐到文本串的 “后缀`aa`”，然后从模式串`aa`的下一个位置开始匹配即可

##### 计算前缀表

![KMP精讲5](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B25.png)

长度为前1个字符的子串`a`，最长相同前后缀的长度为0。（注意字符串的**前缀是指不包含最后一个字符的所有以第一个字符开头的连续子串**；**后缀是指不包含第一个字符的所有以最后一个字符结尾的连续子串**。）

![KMP精讲6](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B26.png)

长度为前2个字符的子串`aa`，最长相同前后缀的长度为1。

长度为前3个字符的子串`aab`，最长相同前后缀的长度为0。

长度为前4个字符的子串`aaba`，最长相同前后缀的长度为1。 

长度为前5个字符的子串`aabaa`，最长相同前后缀的长度为2。

长度为前6个字符的子串`aabaaf`，最长相同前后缀的长度为0。

求得的最长相同前后缀的长度就是对应前缀表的元素，如图：

![KMP精讲8](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B28.png)

可以看出模式串与前缀表对应位置的数字表示的就是：**下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀。**

再来看一下如何利用 前缀表找到 当字符不匹配的时候应该指针应该移动的位置。如动画所示：

![KMP精讲2](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B22.gif)

找到的**不匹配**的位置， 那么此时我们要看它的**前一个字符的前缀表的数值**是多少。

为什么要前一个字符的前缀表的数值呢，因为要找**前面字符串的最长相同的前缀和后缀**。

所以要看前一位的 前缀表的数值。

前一个字符的前缀表的数值是2， 所以把下标移动到下标2的位置继续比配。 可以再反复看一下上面的动画。

##### 前缀表&next数组

next数组既可以是前缀表，也可以是前缀表统一减一（右移一位，初始位置为-1）

##### 使用next数组来匹配

**以下我们以前缀表统一减一之后的next数组来做演示**。

有了next数组，就可以根据next数组来 匹配文本串s，和模式串t了。

注意next数组是新前缀表（旧前缀表统一减一了）。

匹配过程动画如下：

![KMP精讲4](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B24.gif)

n为文本串长度，m为模式串长度，因为在匹配的过程中，根据前缀表不断调整匹配的位置，可以看出匹配的过程是O(n)，之前还要单独生成next数组，时间复杂度是O(m)。所以整个KMP算法的时间复杂度是O(n+m)的。

暴力的解法显而易见是O(n × m)，所以**KMP在字符串匹配中极大地提高了搜索的效率。**

##### 构造next数组

定义一个函数getNext来构建next数组，函数参数为指向next数组的指针，和一个字符串。 代码如下：

```text
void getNext(int* next, const string& s)
```

**构造next数组其实就是计算模式串s的前缀表的过程。** 主要有如下三步：

1. 初始化
2. 处理前后缀不相同的情况
3. 处理前后缀相同的情况

详解一下

1. 初始化：

定义两个指针i和j，j指向前缀末尾位置，i指向后缀末尾位置。

> j的值等于前缀最后一个字符的下标，i的值等于后缀最后一个字符的下标

然后还要对next数组进行初始化赋值，如下：

```cpp
int j = -1;
next[0] = j;
```

j 为什么要初始化为 -1呢，因为之前说过 前缀表要统一减一的操作仅仅是其中的一种实现，我们这里选择j初始化为-1，下文还会给出j不初始化为-1的实现代码。

next[i] 表示 i（包括i）之前最长相等的前后缀长度（其实就是j）

所以初始化next[0] = j 。

2. 处理前后缀不相同的情况

因为j初始化为-1，那么i就从1开始，进行s[i] 与 s[j+1]的比较。

所以遍历模式串s的循环下标i 要从 1开始，代码如下：

```cpp
for (int i = 1; i < s.size(); i++) {//对每个以i为后缀末尾的子串，找到它的最长相等前后缀记录到next[i]，前后缀不匹配则回退j，前后缀匹配则推进j
```

如果 s[i] 与 s[j+1]不相同，也就是遇到 前后缀末尾不相同的情况，就要向前回退。

怎么回退呢？

next[j]就是记录着j（包括j）之前的子串的相同前后缀的长度。

那么 s[i] 与 s[j+1] 不相同，就要找 j+1前一个元素在next数组里的值（就是next[j]）。

所以，处理前后缀不相同的情况代码如下：

```cpp
while (j >= 0 && s[i] != s[j + 1]) { // 前后缀不相同了
    j = next[j]; // 向前回退
}
```

3. 处理前后缀相同的情况

如果 s[i] 与 s[j + 1] 相同，那么就说明同时向后移动i 和j 的时候找到了相同的前后缀，同时还要将j（前缀的长度）赋给next[i], 因为next[i]要记录相同前后缀的长度。

代码如下：

```text
if (s[i] == s[j + 1]) { // 找到相同的前后缀
    j++;
}
next[i] = j;
```

最后整体构建next数组的函数代码如下：

```cpp
void getNext(int* next, const string& s){
    int j = -1;
    next[0] = j;
    for(int i = 1; i < s.size(); i++) { // 注意i从1开始
        while (j >= 0 && s[i] != s[j + 1]) { // 前后缀不相同了
            j = next[j]; // 向前回退
        }
        if (s[i] == s[j + 1]) { // 找到相同的前后缀
            j++;
        }
        next[i] = j; // 将j（前缀的长度）赋给next[i]
    }
}
```

代码构造next数组的逻辑流程动画如下：

![KMP精讲3](https://file1.kamacoder.com/i/algo/KMP%E7%B2%BE%E8%AE%B23.gif)

得到了next数组后就可以用这个来做匹配了



### 重复的子字符串









#### 前缀表

记录模式串中每个位置`j`的**最长相等前后缀长度**，当匹配失败时，告知`j`应该回退到哪个位置

- **前缀&&后缀**

  - 前缀：不包含最后一个字符且以第一个字符开头的所有连续子串
  - 后缀：不包含第一个字符且以最后一个字符结尾的所有连续子串
  - 举例：对于一个字符串`t='aabaa'`，它的前缀组成的列表为`['a','aa','aab','aaba']`，它的后缀组成的列表为`["a", "aa", "baa", "abaa"]`

- **最长相等前后缀**

  前缀和后缀中**长度最长且内容相等**的子串长度
  在上例中，最长的子串是`aa`，所以长度为2

- **前缀表定义**

  前缀表（prefix数组）是一个和模式串长度相同的数组，`prefix[i]`表示模式串前`i+1`个字符组成的子串的**最长前后缀长度**

  以模式串`t='aabaaf'`为例，计算前缀表

  | 索引 i | 子串 t [0..i] |  最长相等前后缀长度   | prefix[i] |
  | :----: | :-----------: | :-------------------: | :-------: |
  |   0    |      "a"      |  无前后缀（长度 1）   |     0     |
  |   1    |     "aa"      |  前缀 "a" = 后缀 "a"  |     1     |
  |   2    |     "aab"     |     无相等前后缀      |     0     |
  |   3    |    "aaba"     |  前缀 "a" = 后缀 "a"  |     1     |
  |   4    |    "aabaa"    | 前缀 "aa" = 后缀 "aa" |     2     |
  |   5    |   "aabaaf"    |     无相等前后缀      |     0     |

  最终前缀表：`prefix = [0,1,0,1,2,0]`。



### 字符串__总结



---

## 双指针法

### 移除元素



### 反转字符串



### 替换元素



### 翻转字符串里的单词



### 翻转链表



### 删除链表的倒数第N个节点



### 链表相交



### 环形链表II



### 三数之和



### 四数之和



### 双指针__总结



---

## 栈与队列

###  栈与队列理论基础

#### 栈

**栈（`stack`）：后进先出**	摞盘子，最后放上去的盘子最先拿下来	FILO,First In Last Out

栈的底层可以用两种结构实现：

- 数组（`list`）：缓存友好，内存连续，出入栈操作效率高；数组满了需要扩容
- 链表：无固定大小限制，动态扩容；内存不连续，范围效率低

**栈是一种特殊的线性表**，数据元素**插入（入栈，Push）**和**删除（出栈，Pop）**只能在线性表的**同一端**进行。这一端被称为**栈顶**，另一端则被称为**栈底**	==即**出入栈操作**都**只能**从线性表的**栈顶**进行==

      |   |   <- 栈顶 (操作端)
      | C |
      | B |
      | A |   <- 栈底 (固定端)
      |___|

*初始栈为空，经过 `Push(A)`, `Push(B)`, `Push(C)` 操作后，栈内状态如图所示。下一个 `Pop()` 操作将返回元素 `C`。*

##### 用Python实现栈

法1:直接用列表，不够规范

```python
# 列表模拟栈
stack = []

# 入栈（push）
stack.append(1)
stack.append(2)
stack.append(3)
print("栈内容:", stack)  # 输出: [1,2,3]

# 出栈（pop）
top_elem = stack.pop()
print("出栈元素:", top_elem)  # 输出: 3
print("出栈后的新栈:", stack)     # 输出: [1,2]

# 查看栈顶（peek）
peek_elem = stack[-1]
print("栈顶元素:", peek_elem)  # 输出: 2

# 判空
print("是否为空:", len(stack) == 0)  # 输出: False

# 大小
print("栈大小:", len(stack))  # 输出: 2
```

法2:封装成类，增加异常处理（比如空栈pop时会报错），更加健壮

```python
class Stack:
    def __init__(self):
        self.items = []  # 底层用列表存储
    
    def push(self, item):
        """入栈：向栈顶添加元素"""
        self.items.append(item)
    
    def pop(self):
        """出栈：移除并返回栈顶元素，空栈则抛异常"""
        if self.is_empty():
            raise IndexError("栈为空，无法执行pop操作")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素，不移除"""
        if self.is_empty():
            raise IndexError("栈为空，无法查看栈顶")
        return self.items[-1]
    
    def is_empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """返回栈的大小"""
        return len(self.items)

# 测试栈类
s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # 输出: 20
print(s.pop())   # 输出: 20
print(s.size())  # 输出: 1
# s.pop()  # 此时栈剩1个元素，pop后空；再pop会抛异常
```

#### 队列

**队列（`queue`）：先进先出**	排队买票，队伍前面的人先得到服务	FIFO,First In First Out

**队列**是一种特殊的线性表，其数据元素的**插入（入队，Enqueue）**和**删除（出队，Dequeue）**操作分别在线性表的**两端**进行。插入端成为**队尾**，删除端称为**队头**

      出队 Dequeue <-- | A | B | C | D | <-- 入队 Enqueue
                      ^               ^
                    队头(Front)      队尾(Rear)

队列在实际开发中需要使用`collections.deque`，即双端队列，基于**双向链表**实现，`append()`右入队和`popleft()`左出队都是O（1）

##### 用Python实现队列

法1:列表模拟，仅作演示

```python
# 列表模拟队列（效率低，仅演示）
queue = []

# 入队（enqueue）
queue.append(1)
queue.append(2)
queue.append(3)
print("队列内容:", queue)  # 输出: [1,2,3]

# 出队（dequeue）
front_elem = queue.pop(0)  # 效率O(n)，不推荐！
print("出队元素:", front_elem)  # 输出: 1
print("出队后队列:", queue)     # 输出: [2,3]
```

法2:deque实现	`collections.deque`

双端队列允许从两端插入和删除

```python
from collections import deque

# 初始化队列
queue = deque()

# 入队（enqueue）
queue.append(1)
queue.append(2)
queue.append(3)
print("队列内容:", queue)  # 输出: deque([1,2,3])

# 出队（dequeue）
front_elem = queue.popleft()  # 效率O(1)，推荐！
print("出队元素:", front_elem)  # 输出: 1
print("出队后队列:", queue)     # 输出: deque([2,3])

# 查看队首
front_elem = queue[0]
print("队首元素:", front_elem)  # 输出: 2

# 判空
print("是否为空:", len(queue) == 0)  # 输出: False

# 大小
print("队列大小:", len(queue))  # 输出: 2
```

### 用栈实现队列

```plain
#题目

只使用两个栈实现先入先出队列。队列应该要支持一般队列支持的所有操作
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
```

#### 思路

用栈来模拟队列的行为，如果只用一个栈（后进先出）是无法实现队列（先进先出），可以设置两个栈：一个输入栈，一个输出栈；用动画模拟

![232.用栈实现队列版本2](https://file1.kamacoder.com/i/algo/232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97%E7%89%88%E6%9C%AC2.gif)

在push数据的时候，只要数据放进输入栈就好，**但在pop的时候，操作就复杂一些，输出栈如果为空，就把进栈数据==全部导入==进来（注意是全部导入）**，再从出栈弹出数据，如果输出栈不为空，则直接从出栈弹出数据就可以了。

最后如何判断队列为空呢？**如果进栈和出栈都为空的话，说明模拟的队列为空了。**

```c++
class MyQueue {//定义模拟队列的类
public:
    stack<int> stIn;//输入栈，接收入队的元素，输出元素给输出栈
    stack<int> stOut;//输出栈，提供出队的元素，接收输入栈的输出元素
    /** Initialize your data structure here. */  //在这里初始化你的数据结构
    MyQueue() {

    }
    /** Push element x to the back of queue. */
    void push(int x) {
        stIn.push(x);//栈的push：压入栈顶
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        // 只有当stOut为空的时候，再从stIn里导入数据（导入stIn全部数据）
        if (stOut.empty()) {
            // 从stIn导入数据直到stIn为空
            while(!stIn.empty()) {
                stOut.push(stIn.top());//取输入栈的栈顶元素，压入输出栈栈顶
                stIn.pop();//移除输入栈栈顶元素（已转移到输出栈，避免重复）
            }//循环结束后输入栈的所有元素已经被转移到了输出栈
        }
        int result = stOut.top();//输出栈栈顶=队列队首
        stOut.pop();//移除输出栈栈顶=队列出队操作
        return result;//返回被移除的队首元素（即queue.pop()）
    }

    /** Get the front element. */   //获取队首元素，不移除
    int peek() {
        int res = this->pop(); // 复用pop()函数，调用pop()拿到了队首元素，此时元素被移除
        stOut.push(res); // 因为pop函数弹出了元素res，所以再添加回去
        return res;
    }

    /** Returns whether the queue is empty. */   //判断队列是否为空
    bool empty() {
        //队列的所有元素要么在输入栈，要么在输出栈，只有两者都空时，队列才空
        return stIn.empty() && stOut.empty();
    }
};

//peek()的实现直接复用了pop()，对于功能相近的函数要抽象出来，尽可能复用代码，而不是做cv工程师
```

```python
class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)

    #c++的逻辑和python略有不同，不过原理都是输出栈为空时才将所有输入栈元素倒入到输出栈，输出栈不为空时，调用栈的pop()弹出元素
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #调用自定义的empty()来判断队列是否为空，如果队列为空，直接返回None
        if self.empty():
            return None
        #如果输出栈有元素直接弹出栈顶
        if self.stack_out:
            return self.stack_out.pop()
        #如果输出栈为空，先把输入栈所有元素弹出到输出栈
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)
```

### 用队列实现栈

```plain
#题目

使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
```

#### 思路

单向队列

队列是先进先出的规则，把一个队列中数据导入另一个队列中，数据的顺序并没有变为先进后出

这时需要想到用另一个队列作为备份

**用两个队列que1和que2实现栈的功能，que2其实完全就是一个备份的作用**，把que1最后面的元素以外的元素都备份到que2，然后弹出最后面的元素，再把其他元素从que2导回que1。

![225.用队列实现栈](https://file1.kamacoder.com/i/algo/225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.gif)

```c++
class MyStack {
public:
    queue<int> que1;
    queue<int> que2; // 辅助队列，用来备份

    /** Initialize your data structure here. */
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        que1.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {//pop()移除并返回栈顶元素
        int size = que1.size();
        size--;
        while (size--) { // 将que1 导入que2，但要留下最后一个元素
            //front()只获取队首元素，不会移除该元素，返回值时队首元素的拷贝
            que2.push(que1.front());
            //pop()只移除队首元素，因为que1的队首元素已经拷贝了一份被push到que2了，所以要移除队首元素
            que1.pop();
        }

        int result = que1.front(); // 留下的最后一个元素就是要返回的值
        que1.pop();
        que1 = que2;            // 再将que2赋值给que1
        while (!que2.empty()) { // 当que2不为空时持续pop()，以清空que2
            que2.pop();
        }
        return result;
    }

    /** Get the top element.
     ** Can not use back() direactly.
     */
    int top(){//top()只查看栈顶元素，只是获取值，不移除元素
        int size = que1.size();
        size--;
        while (size--){
            // 将que1 导入que2，但要留下最后一个元素
            que2.push(que1.front());
            que1.pop();
        }

        int result = que1.front(); // 留下的最后一个元素就是要回返的值
        que2.push(que1.front());   // 获取值后将最后一个元素也加入que2中，保持原本的结构不变
        que1.pop();

        que1 = que2; // 再将que2赋值给que1
        while (!que2.empty()){
            // 清空que2
            que2.pop();
        }
        return result;
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return que1.empty();
    }
};
//时间复杂度: pop为O(n)，top为O(n)，其他为O(1)
```

但是这道题用一个队列就足够了

一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外）重新添加到队列尾部，此时再去弹出元素就是栈的顺序了

```c++
class MyStack {
public:
    queue<int> que;

    MyStack() {

    }

    void push(int x) {
        que.push(x);
    }

    int pop() {
        int size = que.size();
        size--;
        while (size--) { // 将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部
            que.push(que.front());
            que.pop();
        }
        int result = que.front(); // 此时弹出的元素顺序就是栈的顺序了
        que.pop();
        return result;
    }

    int top(){
        int size = que.size();
        size--;
        while (size--){
            // 将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部
            que.push(que.front());
            que.pop();
        }
        int result = que.front(); // 此时获得的元素就是栈顶的元素了
        que.push(que.front());    // 将获取完的元素也重新添加到队列尾部，保证数据结构没有变化
        que.pop();
        return result;
    }

    bool empty() {
        return que.empty();
    }
};
//时间复杂度: pop为O(n)，top为O(n)，其他为O(1)
```

python代码

```python
#双队列实现
from collections import deque

class MyStack:

    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n)
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        """
        直接append即可
        """
        self.queue_in.append(x)


    def pop(self) -> int:
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
        
        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()

    def top(self) -> int:
        """
        写法一：
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可（这里实际上用到了栈）
        写法二：
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个，并使用temp变量暂存
        6. 把temp追加到queue_in的末尾
        """
        # 写法一：
        # if self.empty():
        #     return None
        
        # return self.queue_in[-1]    # 这里实际上用到了栈，因为直接获取了queue_in的末尾元素

        # 写法二：
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in 
        temp = self.queue_out.popleft()   
        self.queue_in.append(temp)#将获取完的元素重新添加到队尾，保证数据结构没变化
        return temp


    def empty(self) -> bool:
        """
        因为只有in存了数据，只要判断in是不是有数即可
        """
        return len(self.queue_in) == 0

    
#单队列实现栈
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        # 写法一：
        # if self.empty():
        #     return None
        # return self.que[-1]

        # 写法二：
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.que
```

### 有效的括号

```plIn
#题目

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
```

#### 思路

括号匹配是使用栈解决的经典问题

题目要求括号的顺序是一样的，如果有左括号出现那么相应的位置则必须要有右括号出现

栈结构的特殊性，非常适合做**对称匹配**类的题目

首先分析一下三种不匹配的情况：

1. 左括号多了
    ![括号匹配1](https://file1.kamacoder.com/i/algo/2020080915505387.png)
2. 括号的类型没有匹配上
    ![括号匹配2](https://file1.kamacoder.com/i/algo/20200809155107397.png)
3. 右括号多了
    ![括号匹配3](https://file1.kamacoder.com/i/algo/20200809155115779.png)

我们的代码只要覆盖了这三种不匹配的情况，就不会出问题，可以看出 动手之前分析好题目的重要性。

动画如下：

![20.有效括号](https://file1.kamacoder.com/i/algo/20.%E6%9C%89%E6%95%88%E6%8B%AC%E5%8F%B7.gif)

第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false

第二种情况：遍历字符串匹配的过程中，发现栈里没有要匹配的字符。所以return false

第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号return false

那么什么时候说明左括号和右括号全都匹配了呢，就是字符串遍历完之后，栈是空的，就说明全都匹配了。

分析完之后，代码其实就比较好写了，

但还有一些技巧，在匹配左括号的时候，右括号先入栈，就只需要比较当前元素和栈顶相不相等就可以了，比左括号先入栈代码实现要简单的多了！

遍历到左括号时向栈内存对应的右括号，遍历到右括号时从栈中取出栈顶元素作比较（是否相等，不相等则说明左右括号不匹配了，直接返回false）；字符串遍历结束后若栈不为空，则说明左括号多了，不匹配；字符串遍历未结束时（下标索引的for循环未结束）若栈为空，则说明右括号多了，不匹配

实现C++代码如下：

```cpp
class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0) return false; //剪枝：如果s的长度为奇数，一定不匹配
        stack<char> st;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') st.push(')');
            else if (s[i] == '{') st.push('}');
            else if (s[i] == '[') st.push(']');
            // 以上完成向栈内添加对应的右括号元素，下面就开始判断出现右括号时是否匹配
            // 第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号 return false
            // 第二种情况：遍历字符串匹配的过程中，发现栈里没有我们要匹配的字符。所以return false
            else if (st.empty() || st.top() != s[i]) return false;
            else st.pop(); // st.top() 与 s[i]相等，栈弹出元素，便于进行下一个下标索引的匹配（for循环）
        }//for循环结束,字符串遍历结束
        // 第一种情况：此时我们已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false，否则就return true
        return st.empty();
    }
};
```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        
        return True if not stack else False
```

### 删除字符串中的所有相邻重复项

```plain
#题目

给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

例如：输入abbaca，输出ca
```

#### 思路

本题与上题有效的括号是同类型的匹配问题，同样要匹配随后作消除处理，那么同样也可以用栈来解决

在删除相邻的重复项时，需要知道当前遍历的这个元素，在前一位是否遍历过一样数值的元素，用栈来存放遍历过的元素，当遍历当前的这个元素时，查看栈顶元素是否与当前元素相同，随后再去做对应的消除处理

![1047.删除字符串中的所有相邻重复项](https://file1.kamacoder.com/i/algo/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.gif)



从栈中弹出剩余元素，因为栈里弹出的元素是倒序的，所以需要再对字符串反转一下

C++代码

```c++
class Solution {
public:
    string removeDuplicates(string S) {
        stack<char> st;
        for (char s : S) {
            //栈为空或者栈顶元素不等于当前遍历的元素时需要向栈内压入该元素
            if (st.empty() || s != st.top()) {
                st.push(s);
            } else {
                st.pop(); // s 与 st.top()相等的情况
            }
        }//循环结束时所有字符元素已经遍历完成，已经删除所有相邻的重复元素
        string result = "";
        while (!st.empty()) { // 将栈中元素放到result字符串汇总
            result += st.top();
            st.pop();
        }
        reverse (result.begin(), result.end()); // 此时字符串需要反转一下
        return result;

    }
};


//用字符串直接作为栈	  尾--->头，字符串尾部作为模拟栈的栈顶 
class Solution {
public:
    string removeDuplicates(string S) {
        string result;//用string模拟栈，存储最终结果
        for(char s : S) {//遍历原字符串的每个字符
            if(result.empty() || result.back() != s) {
                result.push_back(s);//压入栈，追加到字符串末尾，即压入到栈顶
            }
            else {//栈顶字符 == 当前字符（相邻重复）
                result.pop_back();//弹出栈顶，删除字符串中的最后一个字符
            }
        }
        return result;
    }
};
```

```python
# 方法一，使用栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item:#res不为空且res栈顶元素等于遍历到的元素则删除
                res.pop()
            else:
                res.append(item)
        #遍历结束后 res = ['c','a']
        return "".join(res)  # 字符串拼接


#方法二，使用双指针模拟栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)#将字符串转化为列表
        slow = fast = 0#初始化快慢指针
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])
```

### 逆波兰表达式求值

```plain
#题目

根据 逆波兰表示法，求表达式的值	逆波兰式：后缀表达式，将运算符写在操作数之后
有效的运算符包括 + ,  - ,  * ,  / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
```

#### 思路

递归就是栈来实现的，**栈与递归之间在某种程度上是可以转换的**

逆波兰表达式相当于二叉树的后序遍历，将运算符作为中间节点，按照后续遍历的规则画出一个二叉树

![150.逆波兰表达式求值](https://file1.kamacoder.com/i/algo/150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.gif)

```c++
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (int i = 0;i < tokens.size();i++){
            if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/"){
                long long nums1 = st.top();
                st.pop();
                long long nums2 = st.top();
                st.pop();
                if (tokens[i] == "+"){
                    st.push(nums2 + nums1);
                }
                if (tokens[i] == "-" ){
                    st.push(nums2 - nums1);
                }
                if (tokens[i] == "*"){
                    st.push(nums2 * nums1);
                }
                if (tokens[i] == "/"){
                    st.push(nums2 / nums1);
                }
            }else{
                st.push(stoll(tokens[i]));
            }
        }
        long long result = st.top();
        st.pop();
        return result;
    }
};
```

```python
#方法一，c++逻辑的镜像
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                
                #注意这一段一定要放在第一层if循环内，因为若放在if外，stack可能是空的栈，取不到元素是会报错的
                nums2 = stack[-1]
                stack.pop()
                nums1 = stack[-1]
                stack.pop()
                
                if tokens[i] == '+':
                    stack.append(nums1 + nums2)
                if tokens[i] == '-':
                    stack.append(nums1 - nums2)
                if tokens[i] == '*':
                    stack.append(nums1 * nums2)
                if tokens[i] == '/':
                    stack.append(int(nums1 / nums2))#python没有整除，用int()向零取整
            else:
                stack.append(int(tokens[i]))
        result = stack[-1]
        stack.pop()
        return result

#方法二
from operator import add, sub, mul #+、-、*

def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution(object):
    op_map = {'+': add, '-': sub, '*': mul, '/': div}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
        return stack.pop()
```

### 滑动窗口最大值

```plain
#题目

给定一个数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的k个数字。滑动窗口每次只向右移动一位
返回滑动窗口中的最大值
```

#### 思路

首先引入单调队列的概念
队列里元素始终保持**单调递增/单调递减**，必须使用**双端队列`deque`**，支持**队头、队尾**同时删去元素

此题若使用暴力方法，遍历一遍的过程中每次从窗口中再找到最大的数字，明显是O(nxk)的时间复杂度

我们需要这样一个队列：随着窗口移动，队列一进一出，每次移动之后队列告诉我们里面的最大值是什么
每次窗口移动的时候，调用que.pop(滑动窗口中移除元素的数值)，que.push(滑动窗口添加元素的数值)，然后que.front()就返回我们要的最大值。

举个例子观察单调队列是如何维护队列里的元素

![239.滑动窗口最大值](https://file1.kamacoder.com/i/algo/239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.gif)

对于窗口里的元素{2, 3, 5, 1 ,4}，单调队列里只维护{5, 4} 就够了，保持单调队列里单调递减，此时队列出口元素就是窗口里最大元素

单调队列的套路：

1. 右边入（元素进入队尾，同时维护队列单调性）
   push，如果push的元素value大于队尾元素的值，那么就将队尾（即队列入口）的元素弹出
2. 左边出（元素离开队首）
   pop，如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素
3. 记录/维护答案（队首元素）
   只要通过`que.front()`就可以返回当前窗口的最大值

![239.滑动窗口最大值-2](https://file1.kamacoder.com/i/algo/239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC-2.gif)

```c++
class Solution {
private:
    class MyQueue { //单调队列（从大到小）
    public:
        deque<int> que; // 使用deque来实现单调队列
        // 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
        // 同时pop之前判断队列当前是否为空。
        void pop(int value) {
            if (!que.empty() && value == que.front()) {
                que.pop_front();
            }
        }
        // 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
        // 这样就保持了队列里的数值是单调从大到小的了。
        void push(int value) {
            while (!que.empty() && value > que.back()) {
                que.pop_back();
            }
            que.push_back(value);

        }
        // 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
        int front() {
            return que.front();
        }
    };
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        MyQueue que;
        vector<int> result;
        for (int i = 0; i < k; i++) { // 先将前k的元素放进队列
            que.push(nums[i]);
        }
        result.push_back(que.front()); // result 记录前k的元素的最大值
        for (int i = k; i < nums.size(); i++) {
            que.pop(nums[i - k]); // 滑动窗口移除最前面元素
            que.push(nums[i]); // 滑动窗口前加入最后面的元素
            result.push_back(que.front()); // 记录对应的最大值
        }
        return result;
    }
};


//方法二
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans(n - k + 1); // 窗口个数
        deque<int> q; // 双端队列

        for (int i = 0; i < n; i++) {
            // 1. 右边入
            while (!q.empty() && nums[q.back()] <= nums[i]) {
                q.pop_back(); // 维护 q 的单调性
            }
            q.push_back(i); // 注意保存的是下标，这样下面可以判断队首是否离开窗口

            // 2. 左边出
            int left = i - k + 1; // 窗口左端点
            if (q.front() < left) { // 队首离开窗口
                q.pop_front();
            }

            // 3. 在窗口左端点处记录答案
            if (left >= 0) {
                // 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans[left] = nums[q.front()];
            }
        }

        return ans;
    }
};
```

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = [] # 结果集合
        kept_nums = deque() # 单调队列

        for i in range(len(nums)):
            update_kept_nums(kept_nums, nums[i]) # 右侧新元素加入

            if i >= k and nums[i - k] == kept_nums[0]: # 左侧旧元素如果等于单调队列头元素，需要移除头元素
                kept_nums.popleft()

            if i >= k - 1:
                max_list.append(kept_nums[0])

        return max_list

def update_kept_nums(kept_nums, num): # num 是新加入的元素
    # 所有小于新元素的队列尾部元素，在新元素出现后，都是没有价值的，都需要被移除
    while kept_nums and num > kept_nums[-1]:
        kept_nums.pop()

    kept_nums.append(num)
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)  # 由窗口个数提前初始化答案数组
        q = deque()  # 双端队列，队列内的元素为原数组nums的下标

        for i, x in enumerate(nums):
            # 1. 右边入
            #当队列不为空且队尾元素小于等于当前下标索引对应的num时进入循环
            #stack[-1]栈顶元素
            #循环比较，直到当前num小于队尾元素或者没有队尾元素了（空队列）
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 注意保存的是下标，这样下面可以判断队首是否离开窗口

            # 2. 左边出
            left = i - k + 1  # 窗口左端点
            if q[0] < left:  # 队首离开窗口
                q.popleft()

            # 3. 在窗口左端点处记录答案
            if left >= 0:
                # 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans[left] = nums[q[0]]

        return ans
```

### 前K个高频元素

```plain
#题目

给定一个非空的整数数组，返回其中出现频率前k高的元素
```

#### 思路

本题主要涉及如下三块内容：

1. 统计元素出现的频率
2. 对频率排序
3. 找出前k个高频元素

统计元素出现的频率，可以使用map来进行统计

对频率进行排序，可以用**优先级队列**

优先级队列就是一个披着队列外衣的**堆**，优先级队列对外接口只是从**队头取元素，队尾添加元素**

优先级队列内部元素是自动依照元素的权值排列，缺省情况下`priority_queue`利用`max-heap`（大顶堆）完成对元素的排序，这个大顶堆是以`vector`为表现形式的`complete binary tree`（完全二叉树）。

**堆**是一颗完全二叉树，树中每个节点的值都不小于（或者不大于）其左右孩子的值。如果父亲节点是大于等于左右孩子即为大顶堆，小于等于左右孩子就是小顶堆

- 大顶堆（堆头是最大元素）
- 小顶堆（堆头是最小元素）

大小顶堆可以直接用`priority_queue`（优先级队列）就可以了，底层实现是一样的，从小到大排就是小顶堆，从大到小排就是大顶堆

本题要使用优先级队列来对部分频率进行排序，因为只需要**维护k个有序的序列**就可以了，所以不需要使用快排（因为快排要将`map`转换为`vector`然后再对整个数组进行排序，是浪费时间的）

此题要求前k个高频元素，如果使用大顶堆的话，定义一个大小为k的大顶堆，在每次移动更新大顶堆的时候，每次弹出都把最大的元素弹出去了，这样就无法保留下来前k个高频元素了

而且使用大顶堆的话需要把所有元素都进行排序，所以如果只排序k个元素的话要使用小顶堆，小顶堆每次将最小的元素弹出，最后小顶堆里积累的是前k个最大元素

寻找前k个最大元素流程如图所示：（图中的频率只有三个，所以正好构成一个大小为3的小顶堆，如果频率更多一些，则用这个小顶堆进行扫描）

![347.前K个高频元素](https://file1.kamacoder.com/i/algo/347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.jpg)

我们来看一下C++代码：

```cpp
class Solution {
public:
    // 小顶堆
    class mycomparison {
    public:
        bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
            return lhs.second > rhs.second;
        }
    };
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // 要统计元素出现频率
        unordered_map<int, int> map; // map<nums[i],对应出现的次数>
        for (int i = 0; i < nums.size(); i++) {
            map[nums[i]]++;
        }

        // 对频率排序
        // 定义一个小顶堆，大小为k
        priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison> pri_que;

        // 用固定大小为k的小顶堆，扫面所有频率的数值
        for (unordered_map<int, int>::iterator it = map.begin(); it != map.end(); it++) {
            pri_que.push(*it);
            if (pri_que.size() > k) { // 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                pri_que.pop();
            }
        }

        // 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        vector<int> result(k);
        for (int i = k - 1; i >= 0; i--) {
            result[i] = pri_que.top().first;
            pri_que.pop();
        }
        return result;

    }
};
```

python

```python
#方法一
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
    
#方法二
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 使用字典统计数字出现次数
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        # 更改字典，key为出现次数，value为相应的数字的集合
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
        # 排序
        key = list(index_dict.keys())
        key.sort()
        result = []
        cnt = 0
        # 获取前k项
        while key and cnt != k:
            result += index_dict[key[-1]]
            cnt += len(index_dict[key[-1]])
            key.pop()

        return result[0: k]
```

### 栈与队列__总结





---

## 二叉树

### 二叉树理论基础

二叉树是一种“树形”的数据结构，有一个“根”，然后从根节点开始分叉，**每个节点最多只能有两个子节点**（左子节点&右子节点），这也是“二叉”的由来

二叉树的核心定义：

- **节点**：二叉树的基本单元：包括` 数据（值）`、`指向左子节点的指针/引用`、 `指向右子节点的指针/引用`
- **根节点**：树最顶端的节点，没有父节点
- **叶子节点**：没有左右子节点的节点（树的末梢）
- **节点的度**：节点拥有的子节点数量（二叉树中节点的度只能为0、1、2，最多只能为2）
- **数的深度/高度**：从根节点到最远叶子节点的路径上的节点数

二叉树主要可以分为`满二叉树`和`完全二叉树`两种形式

#### 满二叉树

如果一颗二叉树只有度为0的节点和度为2的节点，并且度为0的节点在同一层上，则这颗二叉树为满二叉树

![img](https://file1.kamacoder.com/i/algo/20200806185805576.png)

这棵树是满二叉树，也可以说是深度为k，有2^k-1^个节点的二叉树

#### 完全二叉树

在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第h层（h从1开始），则该层包含1～2^h-1^个节点

![img](https://file1.kamacoder.com/i/algo/20200920221638903.png)

优先级队列是一个堆，堆就是一颗完全二叉树，同时保证父子节点的顺序关系

[优先级队列应用__栈与队列](#前k个高频元素)

#### 二叉搜索树

二叉搜索树是有数值的，**二叉搜索树是一个有序树**

- 若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值
- 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值
- 它的左、右子树也分别为二叉排序树

下面这两颗树都是搜索树

![img](https://file1.kamacoder.com/i/algo/20200806190304693.png)

#### 平衡二叉搜索树

平衡二叉搜索树又被称为**AVL树（Adelson-Velsky and Landis）**，具有如下性质：它是一颗**空树**或者它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一颗平衡二叉树

![img](https://file1.kamacoder.com/i/algo/20200806190511967.png)

判断一棵树是否为平衡二叉搜索树：

- 是二叉搜索树：对任意节点，左子树所有值< 根节点值<右子树所有值（中序遍历递增）
- 是平衡树：树中每一个节点的左右子树高度差的绝对值小于等于1（这个差值即为平衡因子）

> 补充：
>
> 空节点的高度为0
>
> 叶子节点（无子节点）的高度为1
>
> 非叶子节点高度=`max（左子树高度，右子树高度）+1`
>
> 平衡因子为左子树高度-右子树高度

**C++中map、set、multimap，multiset的底层实现都是平衡二叉搜索树**，所以map、set的增删操作时间时间复杂度是logn

#### 二叉树的存储方式

二叉树可以**链式存储**，也可以**顺序存储**

- 链式存储：利用指针，把分布在各个地址的节点串联在一起

![img](https://file1.kamacoder.com/i/algo/2020092019554618.png)

- 顺序存储：利用数组存储二叉树，顺序存储的元素在内存中是连续分布的

![img](https://file1.kamacoder.com/i/algo/20200920200429452.png)

利用数组存储的二叉树如何实现遍历：

**如果父节点的数组下标是i，那么它的左孩子就是ix2+1，右孩子就是ix2+2**

一般而言，都是用链式存储二叉树

#### 二叉树的遍历方式

二叉树主要有两种遍历方式：

1. 深度优先遍历DFS：先往深走，遇到叶子节点再往回走
2. 广度优先遍历BFS：一层层地遍历

**以上两种遍历是[图论](#图论)中最基本的两种遍历方式**

从深度优先遍历和广度优先遍历进一步拓展:

- 深度优先遍历（递归法、迭代法）
  - 前序遍历（中左右）
  - 中序遍历（左中右）
  - 后序遍历（左右中）
- 广度优先遍历（迭代法）
  - 层序遍历（从上到下、从左到右）

深度优先遍历中的==**前中后**==指的是中间节点的遍历顺序，前中后序指的是中间节点的位置

![img](https://file1.kamacoder.com/i/algo/20200806191109896.png)

在二叉树相关题目中，经常使用递归的方法来实现深度优先遍历，也就是实现前中后序遍历，使用递归比较方便

在栈与队列中，栈就是递归的一种实现结构，也就是说前中后序遍历的逻辑可以借助栈使用递归的方式来实现

广度优先遍历的实现一般使用队列来实现，因为队列具有先进先出的特点，所以可以一层一层的来遍历二叉树

#### 二叉树的定义

给出链式存储的二叉树节点的定义方式

```C++
#include <iostream>
// 定义二叉树节点结构体
struct TreeNode {
    int val;                // 节点存储的值
    TreeNode *left;         // 指向左子节点的指针
    TreeNode *right;        // 指向右子节点的指针
    // 构造函数：初始化节点（默认值0，左右指针为空）
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

int main() {
    // 示例：创建一棵简单的二叉树（根=1，左=2，右=3）
    TreeNode* root = new TreeNode(1);    // 根节点
    root->left = new TreeNode(2);        // 根的左子节点
    root->right = new TreeNode(3);       // 根的右子节点
    
    // 记得释放内存（避免内存泄漏）
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
```

```python
class TreeNode:
    # 初始化二叉树节点：值、左子节点、右子节点
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # 节点存储的值
        self.left = left     # 指向左子节点的引用（默认None）
        self.right = right   # 指向右子节点的引用（默认None）

# 示例：创建一棵简单的二叉树（根=1，左=2，右=3）
root = TreeNode(1)          # 根节点
root.left = TreeNode(2)     # 根的左子节点
root.right = TreeNode(3)    # 根的右子节点
```

能发现二叉树的定义和链表差不多，相对于链表，二叉树的节点里多了一个指针，有两个指针指向左右孩子

**注意⚠️：一定要注意数据结构的定义以及简单逻辑的代码书写**

### 二叉树的递归遍历

重点：避免掉入==**一看就会，一写就废**==的泥潭之中

递归算法三要素：

1. **确定递归函数的<u>参数和返回值</u>**：确定哪些参数是递归的过程中需要处理的，就在递归函数中加上这个参数，还要明确每次递归的返回值是什么来确定递归函数的返回类型
2. **确定终止条件**：递归算法运行时经常会遇到栈溢出的错误，就是没写终止条件或者终止条件不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出
3. **确定单层递归的逻辑**：确定每一层递归需要处理的信息，重复调用自己来实现递归

>  以前序遍历（<u>中左右</u>）为例：

1. **确定递归函数的参数和返回值**：因为要打印出前序遍历节点的数值，所以参数里需要传入vecotr来放节点的数值，除了这一点就不需要再处理什么别的数据了，也不需要有返回值，所以递归函数返回的类型就是void

   > `vector`是C++_STL中最常用的容器之一，是动态可伸缩的数组，可以随意往里加/减元素，它会在底层自动管理内存
   >
   > `void`是C++的关键字，本意为**空/无**，通常用`void 函数名()`表示函数执行完成后不返回任何值;用`函数名(void)`表示函数无参数
   >
   > ```c++
   > //示例
   > #include <iostream>
   > #include <vector>
   > using namespace std;
   > 
   > // 无返回值的函数：仅打印vector内容，不需要返回结果
   > void printVector(const vector<int>& vec) {
   >     if (vec.empty()) {
   >         cout << "vector 为空" << endl;
   >         return; // 无返回值的函数也能用return，仅表示提前结束
   >     }
   >     cout << "vector 内容：";
   >     for (int num : vec) {
   >         cout << num << " ";
   >     }
   >     cout << endl;
   > }
   > 
   > int main() {
   >     vector<int> nums = {10, 20, 30};
   >     printVector(nums); // 调用无返回值函数，无需接收结果
   >     
   >     vector<int> emptyVec;
   >     printVector(emptyVec);
   >     
   >     return 0;
   > }
   > 
   > //运行结果
   > //vector 内容：10 20 30 
   > //vector 为空
   > ```

   ```c++
   void traversal(TreeNode* cur, vector<int>& vec)
   //遍历二叉树，并将遍历到的节点值存入一个int类型的vector中；函数无返回值，仅通过参数的引用实现数据的输出，将遍历结果写入外部的vector
   //TreeNode是自定义的二叉树节点类型（通常是结构体/类，包含节点值和左右点指针）；*表示这是一个指针，cur指向当前正在遍历的二叉树节点；整体作用是告诉函数从哪个节点开始遍历
   //vector<int>表示存储整数的动态数组；&是引用符号，表示这是引用传递，而不是简单的值拷贝；整体是一个引用传递的动态数组，用于存储遍历结果，作用是避免拷贝整个vector来节省内存，此外内部对vec的修改会直接作用于外部传入的原vector
   ```

   > 这里来区分一下引用传递&和值拷贝：
   > 值拷贝：把文件复印一份给函数，函数修改的是复印件，原件完全不受影响
   > 引用传递：给函数一个文件的快捷方式/别名，函数直接操作原件，修改会直接反映到原件上

2. **确定终止条件**：在递归过程中，当前遍历的节点是空了，那么本层递归就要结束了；因此如果当前遍历的这个节点是空，就直接return

   ```c++
   if (cur == NULL) return;
   ```

3. **确定单层递归的逻辑**：前序遍历是中左右的顺序，所以在单层递归的逻辑是要先去取出中节点的数值

   ```c++
   vec.push_back(cur->val);    // 中
   traversal(cur->left, vec);  // 左
   traversal(cur->right, vec); // 右
   ```

   单层递归的逻辑就是按照中左右的顺序来处理的，这样二叉树的前序遍历，基本就写完了，再看一下完整代码：

   前序遍历：

   ```cpp
   class Solution {
   public:
       //定义辅助递归函数traversal
       void traversal(TreeNode* cur, vector<int>& vec) {
           //空节点是二叉树的叶子节点的子节点，没有值可收集也没有子树可遍历
           if (cur == NULL) return;//当前节点是空，说明没有值可以收集，直接退出递归层
           vec.push_back(cur->val);    // 中，末尾追加
           traversal(cur->left, vec);  // 左
           traversal(cur->right, vec); // 右
       }
       //定义对外接口函数
       vector<int> preorderTraversal(TreeNode* root) {
           vector<int> result;//存储遍历结果的局部容器
           traversal(root, result);//调用递归函数填充结果
           return result;
       }
   };
   ```

python

```python
# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []#初始化空列表，存储遍历结果
        
        #定义内部的递归函数dfs，深度优先搜索
        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)#收集当前节点的值
            dfs(node.right)
        
        #调用dfs，从根节点1开始遍历
        dfs(root)
        return res
###前中后序遍历的前中后表示的是 中间节点 在前or中or后，比如若为中序遍历，即左中右，那么要先深入到最左端的叶子节点再回到中间节点再回到左节点的遍历
```

### 二叉树的迭代遍历

在[栈与队列](#栈与队列)中已知匹配问题是栈的强项，递归的实现就是：**每一次递归调用都会把函数的局部变量、参数值和返回地址等压入调用栈中**，然后递归返回的时候，从栈顶弹出上一次递归的各项参数，也是递归能返回上一层位置的原因

#### 前序遍历

前序遍历是中左右，每次先处理的是中间节点；所以要先将根节点放入栈中，然后将右孩子加入栈，再加入左孩子

![二叉树前序遍历（迭代法）](https://file1.kamacoder.com/i/algo/%E4%BA%8C%E5%8F%89%E6%A0%91%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86%EF%BC%88%E8%BF%AD%E4%BB%A3%E6%B3%95%EF%BC%89.gif)

```c++
//前序遍历，代码中空节点不入栈
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        //用于模拟递归调用栈，存储的是指向TreeNode的指针
        stack<TreeNode*> st;
        vector<int> result;
        if (root == NULL) return result;
        //初始化栈，先把根节点压入栈
        st.push(root);
        //核心循环：只要栈不为空，就继续遍历（模拟递归的调用栈未空则继续）
        while (!st.empty()) {
            //取出栈顶节点，st.top()返回的是栈中存储的TreeNode*类型元素，必须用同类型指针变量来接收，node不是完整的TreeNode对象，只是一个存储对象内存地址的变量
            TreeNode* node = st.top();                       // 中
            st.pop();//弹出栈顶节点，已经取出了就无需保留在栈中
            //收集当前节点的值，node是指针，必须用->访问节点的成员变量val
            result.push_back(node->val);
            //压入右子节点（空节点不压入，避免处理空指针）
            if (node->right) st.push(node->right);           // 右（空节点不入栈）
            if (node->left) st.push(node->left);             // 左（空节点不入栈）
        }
        return result;
    }
};
```

> `->`是c++中**指针访问成员变量/函数**的语法符号，和`.`普通对象访问成员是一对互补的语法
>
> .	  访问 普通对象/对象引用 的成员
>
> ->	访问 指针指向的对象 的成员

#### 中序遍历

在前序遍历的迭代过程中，有两个操作：

1. 处理：将元素放进result数组中
2. 访问：遍历节点

前序遍历的顺序是中左右，先访问的元素是中间节点，要处理的元素也是中间节点，所以刚刚才能写出相对简洁的代码，**因为<u>要访问的元素</u>和<u>要处理的元素</u>顺序是一致的，都是中间节点。**

**因为前序遍历中访问节点（遍历节点）和处理节点（将元素放进result数组中）可以同步处理，但是中序就无法做到同步**

中序遍历是左中右，先访问的是二叉树顶部的节点，然后再一层层向下访问，直到到达树左面的最底部，然后再开始处理节点（即把节点的数值放进result数组中），这就造成了**处理顺序和访问顺序不一致的结果**

因此在使用迭代法写中序遍历时，需要借助指针的遍历来帮助访问节点，栈则用来处理节点上的元素

![二叉树中序遍历（迭代法）](https://file1.kamacoder.com/i/algo/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%EF%BC%88%E8%BF%AD%E4%BB%A3%E6%B3%95%EF%BC%89.gif)

**中序遍历，可以写出如下代码：**

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        //这里栈的作用时记录遍历路径，方便回溯到根节点；用于暂存待处理的根节点
        stack<TreeNode*> st;
        //遍历指针cur，负责访问节点（先走到最左），初始指向根节点
        //cur的核心作用是替代递归中的逐层深入左子树的过程
        TreeNode* cur = root;
        //循环条件：还有未访问的节点（需要继续深入左子树）or栈中还有暂存的根节点（需要回溯）
        while (cur != NULL || !st.empty()) {
            //分支1；cur不为空，继续深入左子树
            if (cur != NULL) { // 指针来访问节点，访问到最底层
                st.push(cur); // 暂存当前节点到栈中
                cur = cur->left;                // 移动cur到左子节点，继续找最左节点
            } else {//分支2；cur为空，左子树遍历完了，回溯处理栈中的根节点
                cur = st.top(); //取出栈顶的待处理根节点，此时左子树已空该处理根了
                st.pop();
                result.push_back(cur->val);     // 中
                cur = cur->right;               // 右
            }
        }
        return result;
    }
};
//前序遍历时栈直接存储待访问的节点，中序遍历需要cur指针配合栈完成深入+回溯
```

#### 后序遍历

前序遍历是中左右，后序遍历是左右中，那么我们只需要调整一下前序遍历的代码顺序，就变成中右左的遍历顺序，然后在反转result数组，输出的结果顺序就是左右中了，如下图：

![前序到后序](https://file1.kamacoder.com/i/algo/20200808200338924.png)

**所以后序遍历只需要前序遍历的代码稍作修改就可以了，代码如下：**

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> result;
        if (root == NULL) return result;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top();
            st.pop();
            result.push_back(node->val);
            if (node->left) st.push(node->left); // 相对于前序遍历，这更改一下入栈顺序 （空节点不入栈）
            if (node->right) st.push(node->right); // 空节点不入栈
        }
        reverse(result.begin(), result.end()); // 将结果反转之后就是左右中的顺序了
        return result;
    }
};
```

### 二叉树的统一迭代法



### 二叉树的层序遍历



### 翻转二叉树



### 二叉树周末总结



### 对称二叉树



### 二叉树的最大深度



### 二叉树的最小深度



### 完全二叉树的节点个数



### 平衡二叉树



### 二叉树的所有路径



### 二叉树周末总结



### 左叶子之和



### 找树左下角的值



### 路径总和



### 从中序与后序遍历序列构造二叉树



### 最大二叉树



### 二叉树周末总结



### 合并二叉树



### 二叉搜索树中的搜索



### 验证二叉搜索树



### 二叉搜索树的最小绝对差



### 二叉搜索中的众数



### 二叉树的最近公共祖先



### 二叉树周末总结



### 二叉搜索树的最近公共祖先



### 二叉搜索树中的插入操作



### 删除二叉搜索树中的节点



### 修建二叉搜索树



### 将有序数组转换为二叉搜索树



### 把二叉搜索树转换为累加树



### 二叉树__总结



---

## 回溯算法

### 回溯算法理论基础

回溯法是一种搜索的方式

回溯是递归的副产品，只要有递归就会有回溯

回溯函数就是递归函数，这两个指的是同一个函数

#### 回溯法的效率

回溯的本质是穷举，穷举所有可能，然后选出想要的答案；若是想要让回溯法高效一些，可以加一些**剪枝**的操作，但也改变不了回溯法就是穷举的本质

> 剪枝：通过预判排除无效分支，提前终止没必要的递归/搜索/遍历
> 剪枝主要用在搜索，回溯，动态规划，博弈搜索；其中回溯/DFS剪枝最常见
> **剪枝 = 提前判断 + 放弃无效路径**

很多问题没得选，没有很高效的解法，能用暴力解法完成就已是万事大吉

#### 回溯法解决的问题

回溯法一般可以解决如下几种问题：

- 组合问题：N个数里面按一定规则找出k个数的集合
- 切割问题：一个字符串按一定规则有几种切割方式
- 子集问题：一个N个数的集合里有多少符合条件的子集
- 排列问题：N个数按一定规则全排列，有几种排列方式
- 棋盘问题：N皇后，解数独等等

> 组合：不强调元素的顺序
>
> 排列：强调元素的顺序
>
> 排列有序，组合无序

回溯法解决的问题都可以抽象为**树形**结构，因为回溯法解决的都是在集合中递归查找子集，**集合的大小就构成了数的宽度，递归的深度就构成了树的深度**

递归就必须有终止条件，所以必然是一颗高度有限的树

#### 回溯法模版

回溯三部曲：

- 回溯函数模版返回值以及参数

在回溯算法中，函数返回值一般为void，void表示**这个函数执行完后，不向调用者返回任何数据**

回溯算法需要的参数不像二叉树递归的时候那么容易一次性确定下来，所以一般是先写逻辑，然后需要什么参数，就填什么参数

回溯函数伪代码如下：

```text
void backtracking(参数)
```

- 回溯函数终止条件

回溯法的问题都可以抽象为树形结构，那么遍历树形结构一定要有终止条件

从树中可以看出，一般来说搜到叶子结点了也就找到了满足条件的一条答案，把这个答案存放起来并结束本层递归

回溯函数终止条件伪代码如下：

```text
if (终止条件) {
    存放结果;
    return;
}
```

- 回溯搜索的遍历过程

回溯法一般是在集合中递归搜索，集合的大小构成了树的宽度，递归的深度构成的树的深度。

如图：

![回溯算法理论基础](https://file1.kamacoder.com/i/algo/20210130173631174.png)

注意图中，特意举例集合大小和孩子的数量是相等的！

回溯函数遍历过程伪代码如下：

```text
for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
    处理节点;
    backtracking(路径，选择列表); // 递归
    回溯，撤销处理结果
}
```

for循环就是遍历集合区间，可以理解一个节点有多少个孩子，这个for循环就执行多少次。

backtracking这里自己调用自己，实现递归。

从图中看出**for循环可以理解是横向遍历，backtracking（递归）就是纵向遍历**，这样就把这棵树全遍历完了，一般来说，搜索叶子节点就是找的其中一个结果了。

分析完过程，回溯算法模板框架如下：

```text
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

**这份模板很重要，后面做回溯法的题目都靠它了！**

### 组合问题



### 组合(优化)



### 组合总和III



### 电话号码的字母组合





### 回溯小结





### 组合总和



### 组合总和II



### 分割回文串





### 复原IP地址



### 子集问题



### 回溯小结



### 子集II



### 递增子序列



### 全排列



### 全排列II



### 回溯小结



### 回溯算法去重问题的另一种写法



### N皇后



### 解数独



### 回溯法总结







---

## 贪心算法

### 贪心算法理论基础



### 分发饼干



### 摆动序列



### 最大子序和



### 贪心小结



### 买卖股票的最佳时机II



### 跳跃游戏



### 跳跃游戏II



### K次取反后最大化的数组和





### 贪心小结



### 加油站



### 分发糖果



### 柠檬水找零



### 根据身高重建队列



### 贪心小结



### 根据身高重建队列(vector原理讲解)





### 用最少数量的箭引爆气球



### 无重叠区间



### 划分字母区间



### 合并区间



### 贪心小结



### 单调递增的数字



### 监控二叉树





### 贪心算法总结





---

## 动态规划

### 动态规划理论基础



### 斐波那契数



### 爬楼梯



### 使用最小花费爬楼梯



### 动态规划小结





### 不同路径



### 不同路径II



### 整数拆分





### 不同的二叉搜索树





### 动态规划小结





### 0—1背包理论基础



### 分割等和子集



### 最后一块石头的重量II



### 动态规划小结





### 目标和



### 一和零



### 完全背包理论基础



### 零钱兑换II



### 动态规划小结



### 组合总和IV



### 爬楼梯(进阶)





### 零钱兑换





### 完全平方数





### 动态规划小结





### 单词拆分





### 多重背包理论基础



### 背包问题总结



### 打家劫舍



### 买卖股票的最佳时机(32,34,35,36)



### 动态规划小结(33,38)





### 最佳买卖股票时机含冷冻期





### 买卖股票的最佳时机含手续费





### 股票问题总结



### 最长上升子序列



### 最长连续递增序列



### 最长重复子数组



### 最长公共子序列



### 不相交的线



### 最大子序列之和



### 判断子序列





### 不同的子序列





### 两个字符串的删除操作



### 编辑距离



### 编辑距离总结



### 回文子串





### 最长回文子序列



### 动态规划总结





---

## 单调栈

### 每日温度



### 下一个更大元素I



### 下一个更大元素II



### 接雨水



### 柱状图中的最大矩形



---

## 图论

### 图的理论基础



### 深度优先搜索理论基础



### 可达路径



### 广度优先搜索理论基础



### 岛屿问题——孤岛计数.深度搜索



### 岛屿问题——孤岛计数.广度搜索



### 岛屿问题——最大岛屿的面积



### 岛屿问题——孤岛的总面积



### 岛屿问题——沉没孤岛



### 岛屿问题——高山流水



### 岛屿问题——建造最大工岛



### 岛屿问题——海岸线计算



### 字符串迁移



### 有向图的完全连通



### 并查集理论基础



### 寻找存在的路线



### 多余的边(17,18)



### 最小生成树(19,20)



### 拓扑排序



### Dijkstra朴素版



### Dijkstra堆优化版



### Bellman_ford算法



### Bellman_ford——队列优化



### Bellman_ford——判断负权回路



### Bellman_ford——单源有限量最短路



### Floyd算法



### A*算法



### 最短路问题总结



### 图论总结





---

**完结撒花**🎉
**需要继续努力哦**💪
只作为测试用vscode上传github的一句话

测试一下md，被DNS劫持了

测试一下，为什么每次都是重启了才能成功

烦死我了！！！！

26.03.12再次测试