#python模拟哈希碰撞中拉链法的实现
class HashTable:
    def __init__(self, size=10):
        # 初始化哈希表：每个桶是一个空列表（模拟链表）
        self.size = size#定义哈希表底层数组的长度（桶的数量）
        #哈希表的核心存储结构_一个数组，数组中的每个元素都是空列表，用列表模拟链表
        self.buckets = [[] for _ in range(self.size)]
    
    # 简单的哈希函数：取模运算
    def _hash(self, key):#方法名前的_是Python的约定，代表是有方法，只在类内部用
        #hash(key)是内置函数，把所有可哈希对象生成一个唯一的整数哈希值
        #slif.size取模运算，把哈希值压缩
        return hash(key) % self.size 
    
    # 插入元素
    def put(self, key, value):
        #定位桶，先调用_hash方法算出key对应的桶下标
        bucket_index = self._hash(key)
        #拿到对应的桶（列表/链表）
        bucket = self.buckets[bucket_index]
        
        # 遍历桶里的元素，每个元素是(key,value)元组，检查key是否已存在，存在则更新值，保证一个key只有一个值
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # 处理碰撞/新增，不存在则追加到链表末尾
        bucket.append((key, value))
    
    # 获取元素
    def get(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        # 遍历桶内的链表找目标key
        for k, v in bucket:
            if k == key:
                return v
        # 没找到返回None
        return None

# 测试（修改后，确保碰撞）
ht = HashTable()
# 用数字key构造必然碰撞：5和15取模10都等于5，会放到同一个桶里
ht.put(5, 5)
ht.put(15, 10)  # 和5撞桶
ht.put(25, 15)  # 继续撞桶
ht.put("banana", 3)

print(ht.get(5))   # 输出：5
print(ht.get(15))  # 输出：10
print(ht.buckets)  # 能看到下标为5的桶里有3个元素！
