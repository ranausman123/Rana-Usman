Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> academic_tuple=('name','father name','red number','CNIC number','CGPA')
>>> Usman_registration=('SP24-BBA-081',)
>>> fruit_tuple=('apple','banana','cherry')
>>> numbers_tuple=(2,4,6,8,9)
>>> mixed_tuple=(1,'apple',5,'True',4.8)
>>> single_item_tuple=(9,)
>>> fruit=('apple','banan','cherry')
>>> print(fruit_tuple[0])
apple
>>> print(fruit_tuple[2])
cherry
>>>  print(fruit_tuple[-2])
 
SyntaxError: unexpected indent
>>>  print(fruit_tuple[-2])
 
SyntaxError: unexpected indent
>>> print(fruit_tuple[-2])
banana
>>> print(fruit_tuple[-1])
cherry
>>> print(fruit[1])
banan
>>> fruit_tuple[0]='blueberry'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fruit_tuple[0]='blueberry'
TypeError: 'tuple' object does not support item assignment
>>> tuple1=(2,3,4,5,6)
>>> tuple2=(1,7,9)
>>> combine_tuple=tuple1+tuple2
>>> print(combine_tuple)
(2, 3, 4, 5, 6, 1, 7, 9)
>>> numbers=(0,1,2,3,4,5,6,7)
>>> print(numbers[1:6])
(1, 2, 3, 4, 5)
>>> print(numbers[:6])
(0, 1, 2, 3, 4, 5)
>>> print(numbers[1:])
(1, 2, 3, 4, 5, 6, 7)
>>> tuple1=('hello',)
>>> repeated_tuple=tuple1*6
>>> print(repeated_tuple)
('hello', 'hello', 'hello', 'hello', 'hello', 'hello')
>>> print(fruit_tuple.count('orange'))
0
>>> print(fruit_tuple.count('banana'))
1
>>> print(fruit_tuple.index('cherry'))
2
>>> tuple1=('cherry')
>>> print(tuple1.count('r'))
2
>>> print(fruit.count('a'))
0
>>> 
KeyboardInterrupt
>>> fruit=('apple','banan','cherry')
>>> print(fruit.count('a'))
0
>>> a_count=sum(fruit.count('a'))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a_count=sum(fruit.count('a'))
TypeError: 'int' object is not iterable
>>> a_count=sum(fruit.count('a') for fruit in fruit)
>>> print("fruit'a':", a_count)
fruit'a': 3
>>> a_count=sum(fruit.break('apple') for fruit in fruit)
SyntaxError: invalid syntax
>>> a_break=sum(fruit.break('apple') for fruit in fruit)
SyntaxError: invalid syntax
>>> break
SyntaxError: 'break' outside loop
>>> 
