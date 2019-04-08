[m-initial]:https://github.com/TimeSoil/Daily-Tech/blob/4141df26ade702bed9399963aeedcde7a234e764/LeetCode/simple/screenshots/mergeTwoLists/mergeTwoLists-mergeTwoLists-initial.png?raw=true

[m-first-step]:https://github.com/TimeSoil/Daily-Tech/blob/4141df26ade702bed9399963aeedcde7a234e764/LeetCode/simple/screenshots/mergeTwoLists/mergeTwoLists-mergeTwoLists-first-step.png

[m-second-step]:https://github.com/TimeSoil/Daily-Tech/blob/4141df26ade702bed9399963aeedcde7a234e764/LeetCode/simple/screenshots/mergeTwoLists/mergeTwoLists-mergeTwoLists-second-step.png

[m-third-step]:https://github.com/TimeSoil/Daily-Tech/blob/4141df26ade702bed9399963aeedcde7a234e764/LeetCode/simple/screenshots/mergeTwoLists/mergeTwoLists-mergeTwoLists-third-step.png
[m-code]:https://github.com/TimeSoil/Daily-Tech/blob/180b1c7f1a66e17c0cfbef9f8e1d77c732859bd8/LeetCode/simple/mergeTwoLists.py

# MergeTwoLists - Python        
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
([代码][m-code])
## 1.初始化，并预处理
![][m-initial]

__预处理__：
1. 链表判空
2. 记录头节点

**```将L2的节点放入L1```**

```Python
if l1 == None and l2 == None:
	return None
elif l1 == None:
	return l2
elif l2 == None:
	return l1

if l2.val <= l1.val: root = l2
else: root = l1

p1, p2 = l1, l2
while p2 != None:
	.
	.
	.
return root
```

## 2.进行第一轮判断
![][m-first-step]

```(while循环内代码)```

```python
if p2.val <= p1.val:
	while p2.next != None and p2.next.val <= p1.val:
		p2 = p2.next
	l2 = p2.next
	p2.next = p1
	p2 = l2
```

## 3.进行第二轮判断
![][m-second-step]

```(紧接 第一轮判断 所示代码)```

```python
else:
	while p1.next != None and p1.next.val < p2.val:
		p1 = p1.next
	l2 = p2.next
	p2.next = p1.next
	p1.next = p2
	p2 = l2
```

## 4.进行第三轮判断
![][m-third-step]

```(完整 while循环 代码)```

```python
while p2 != None:
	if p2.val <= p1.val:
		while p2.next != None and p2.next.val <= p1.val:
			p2 = p2.next
		l2 = p2.next
		p2.next = p1
	else:
		while p1.next != None and p1.next.val < p2.val:
			p1 = p1.next
		l2 = p2.next
		p2.next = p1.next
		p1.next = p2
	p2 = l2

return root
```
## 5.进行第四轮判断
__剩下一个就留作练习啦~~~__([代码][m-code])




