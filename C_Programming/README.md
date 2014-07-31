<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

- [What are main characteristics of C language?](#what-are-main-characteristics-of-c-language)
- [What is difference between i++ and ++i?](#what-is-difference-between-i-and-i)
- [Difference between ++*p, *p++ and *++p](#difference-between-p-p-and-p)
- [What is l-value?](#what-is-l-value)
- [How to write your own sizeof operator?](#how-to-write-your-own-sizeof-operator)
- [Difference between pointer and array in C?](#difference-between-pointer-and-array-in-c)
- [Understanding **volatile** qualifier in C](#understanding-volatile-qualifier-in-c)
- [Can a variable be both const and volatile?](#can-a-variable-be-both-const-and-volatile)
- [What is the difference between declaration and definition of a variable/function](#what-is-the-difference-between-declaration-and-definition-of-a-variablefunction)
- [What are different storage class specifiers in C?](#what-are-different-storage-class-specifiers-in-c)
- [What is scope of a variable? How are variables scoped in C?](#what-is-scope-of-a-variable-how-are-variables-scoped-in-c)
- [What is NULL pointer? ](#what-is-null-pointer)
- [What is Dangling pointer?](#what-is-dangling-pointer)
- [What are local static variables? What is their use?](#what-are-local-static-variables-what-is-their-use)
- [What are static functions? What is their use?](#what-are-static-functions-what-is-their-use)
- [Assertions in C/C++](#assertions-in-cc)
- [C Precedence Table](#c-precedence-table)
- [References](#references)
- [Awesome sites about C programming](#awesome-sites-about-c-programming)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


###What are main characteristics of C language?
---------------------------------------------
C is a procedural language. The main features of C language include low-level access to memory, simple set of keywords, and clean style. These features make it suitable for system programming like operating system or compiler development.

What is difference between i++ and ++i?
---------------------------------------
* The expression 'i++' returns the old value and then increments i. The expression ++i increments the value and returns new value.
* Precedence of postfix ++ is higher than that of prefix ++.
* Associativity of postfix ++ is left to right and associativity of prefix ++ is right to left.
* In C++, ++i can be used as l-value, but i++ cannot be. In C, they both cannot be used as l-value.

Difference between ++*p, *p++ and *++p
---------------------------------------

*Program 1*

	#include <stdio.h>
	int main(void)
	{
		int arr[] = {10, 20};
		int *p = arr;
		++*p;
		printf("arr[0] = %d, arr[1] = %d, *p = %d", arr[0], arr[1], *p);
		return 0;
	}
	
*Program 2*

	#include <stdio.h>
	int main(void)
	{
		int arr[] = {10, 20};
		int *p = arr;
		*p++;
		printf("arr[0] = %d, arr[1] = %d, *p = %d", arr[0], arr[1], *p);
		return 0;
	}
	
*Program 3*

	#include <stdio.h>
	int main(void)
	{
		int arr[] = {10, 20};
		int *p = arr;
		*++p;
		printf("arr[0] = %d, arr[1] = %d, *p = %d", arr[0], arr[1], *p);
		return 0;
	}
	
The output of above programs and all such programs can be easily guessed by remembering following simple rules about postfix ++, prefix ++ and * (dereference) operators:

* Precedence of prefix ++ and * is same. Associativity of both is right to left.
* Precedence of postfix ++ is higher than both * and prefix ++. Associativity of postfix ++ is left to right.

The expression ++\*p has two operators of same precedence, so compiler looks for associativity. Associativity of operators is right to left. Therefore the expression is treated as ++(\*p). **Therefore the output of first program is "arr[0] = 11, arr[1] = 20, \*p = 11"**.

The expression \*p++ is treated as \*(p++) as the precedence of postfix ++ is higher than \*. **Therefore the output of second program is "arr[0] = 10, arr[1] = 20, \*p = 20"**.

The expression \*++p has two operators of same precedence, so compiler looks for assoiativity. Associativity of operators is right to left. Therefore the expression is treated as \*(++p). **Therefore the output of second program is "arr[0] = 10, arr[1] = 20, \*p = 20"**.

*Another example:*
	
	#include <stdio.h>

	int main()
	{
	   int i[] = {3, 5};
	   int *p = i;
	   int j = --*p++;

	   printf("j = %d\n\n", j);
	   return 0;
	}

	//OUTPUT: j = 2

What is l-value?
----------------
* l-value or location value refers to an expression that can be used on left side of assignment operator. For example in expression "a = 3", a is l-value and 3 is r-value.
* l-values are of two types:
	* **nonmodifiable l-value** represent a l-value that can not be modified. const variables are "nonmodifiable l-value".
	* **modifiable l-value** represent a l-value that can be modified.

How to write your own sizeof operator?
--------------------------------------

	#define my_sizeof(type) (char *)(&type+1)-(char*)(&type)

Difference between pointer and array in C?
------------------------------------------
Pointers are used for storing address of dynamically allocated arrays and for arrays which are passed as arguments to functions. In other contexts, arrays and pointer are two different things, see the following programs to justify this statement.

**Behavior of sizeof operator**

	// 1st program to show that array and pointers are different
	#include <stdio.h>
	int main()
	{
	   int arr[] = {10, 20, 30, 40, 50, 60};
	   int *ptr = arr;
		
	   // sizeof(int) * (number of element in arr[]) is printed
	   printf("Size of arr[] %d\n", sizeof(arr));
	 
	   // sizeof a pointer is printed which is same for all type 
	   // of pointers (char *, void *, etc)
	   printf("Size of ptr %d", sizeof(ptr));
	   return 0;
	}

Output:

	Size of arr[] 24
	Size of ptr 4

**Assigning any address to an array variable is not allowed.**

	// IInd program to show that array and pointers are different
	#include <stdio.h>
	int main()
	{
	   int arr[] = {10, 20}, x = 10;
	   int *ptr = &x; // This is fine
	   arr = &x;  // Compiler Error
	   return 0;
	}

Output:

	Compiler Error: incompatible types when assigning to 
		          type 'int[2]' from type 'int *' 

**Although array and pointer are different things, following properties of array make them look similar.**

**1) Array name gives address of first element of array.**

	#include <stdio.h>
	int main()
	{
	   int arr[] = {10, 20, 30, 40, 50, 60};
	   int *ptr = arr;  // Assigns address of array to ptr
	   printf("Value of first element is %d", *ptr)
	   return 0;
	}

Output:

	Value of first element is 10
 
**2) Array members are accessed using pointer arithmetic.**
Compiler uses pointer arithmetic to access array element. For example, an expression like "arr[i]" is treated as *(arr + i) by the compiler. That is why the expressions like *(arr + i) work for array arr, and expressions like ptr[i] also work for pointer ptr.

	#include <stdio.h>
	int main()
	{
	   int arr[] = {10, 20, 30, 40, 50, 60};
	   int *ptr = arr;
	   printf("arr[2] = %d\n", arr[2]);
	   printf("*(ptr + 2) = %d\n", *(arr + 2));
	   printf("ptr[2] = %d\n", ptr[2]);
	   printf("*(ptr + 2) = %d\n", *(ptr + 2));
	   return 0;
	}

Output:

	arr[2] = 30
	*(ptr + 2) = 30
	ptr[2] = 30
	*(ptr + 2) = 30 
	 
**3) Array parameters are always passed as pointers, even when we use square brackets.**

	#include <stdio.h>
	 
	int fun(int ptr[])
	{
	   int x = 10;
	 
	   // size of a pointer is printed
	   printf("sizeof(ptr) = %d\n", sizeof(ptr));
	 
	   // This allowed because ptr is a pointer, not array
	   ptr = &x;
	 
	   printf("*ptr = %d ", *ptr);
	 
	   return 0;
	}
	int main()
	{
	   int arr[] = {10, 20, 30, 40, 50, 60};
	   fun(arr);
	   return 0;
	}

Output:

	sizeof(ptr) = 4
	*ptr = 10

Understanding **volatile** qualifier in C
----------------------------------------
* The volatile keyword is intended to prevent the compiler from applying any optimizations on objects that can change in ways that cannot be determined by the compiler.

* Objects declared as volatile are omitted from optimization because their values can be changed by code outside the scope of current code at any time. The system always reads the current value of a volatile object from the memory location rather than keeping its value in temporary register at the point it is requested, even if a previous instruction asked for a value from the same object. So the simple question is, how can value of a variable change in such a way that compiler cannot predict. Consider the following cases for answer to this question.
	* Global variables modified by an interrupt service routine outside the scope: For example, a global variable can represent a data port (usually global pointer referred as memory mapped IO) which will be updated dynamically. The code reading data port must be declared as volatile in order to fetch latest data available at the port. Failing to declare variable as volatile, the compiler will optimize the code in such a way that it will read the port only once and keeps using the same value in a temporary register to speed up the program (speed optimization). In general, an ISR used to update these data port when there is an interrupt due to availability of new data

	* Global variables within a multi-threaded application: There are multiple ways for threads communication, viz, message passing, shared memory, mail boxes, etc. A global variable is weak form of shared memory. When two threads sharing information via global variable, they need to be qualified with volatile. Since threads run asynchronously, any update of global variable due to one thread should be fetched freshly by another consumer thread. Compiler can read the global variable and can place them in temporary variable of current thread context. To nullify the effect of compiler optimizations, such global variables to be qualified as volatile

* If we do not use volatile qualifier, the following problems may arise
	* Code may not work as expected when optimization is turned on.
	* Code may not work as expected when interrupts are enabled and used.

Let us see an example to understand how compilers interpret volatile keyword. Consider below code, we are changing value of const object using pointer and we are compiling code without optimization option. Hence compiler won't do any optimization and will change value of const object.

	/* Compile code without optimization option */
	#include <stdio.h>
	int main(void)
	{
		const int local = 10;
		int *ptr = (int*) &local;
	 
		printf("Initial value of local : %d \n", local);
	 
		*ptr = 100;
	 
		printf("Modified value of local: %d \n", local);
	 
		return 0;
	}

When we compile code with "-save-temps" option of gcc it generates 3 output files

* preprocessed code (having .i extention)
* assembly code (having .s extention) and
* object code (having .o option).

We compile code without optimization, that's why the size of assembly code will be larger (which is highlighted in red color below).

Output:

	  [ashish@ubuntu]$ gcc volatile.c -o volatile -save-temps
	  [ashish@ubuntu]$ ./volatile
	  Initial value of local : 10
	  Modified value of local: 100
	  [ashish@ubuntu]$ ls -l volatile.s
	  -rw-r-r- 1 ashish ashish 731 2016-11-19 16:19 volatile.s
	  [ashish@ubuntu]$

Let us compile same code with optimization option (i.e. -O option). In thr below code, "local" is declared as const (and non-volatile), GCC compiler does optimization and ignores the instructions which try to change value of const object. Hence value of const object remains same.

	/* Compile code with optimization option */
	#include <stdio.h>
	 
	int main(void)
	{
		const int local = 10;
		int *ptr = (int*) &local;
	 
		printf("Initial value of local : %d \n", local);
	 
		*ptr = 100;
	 
		printf("Modified value of local: %d \n", local);
	 
		return 0;
	}

For above code, compiler does optimization, that's why the size of assembly code will reduce.

Output:

	  [ashish@ubuntu]$ gcc -O3 volatile.c -o volatile -save-temps
	  [ashish@ubuntu]$ ./volatile
	  Initial value of local : 10
	  Modified value of local: 10
	  [ashish@ubuntu]$ ls -l volatile.s
	  -rw-r-r- 1 ashish ashish 626 2016-11-19 16:21 volatile.s

Let us declare const object as volatile and compile code with optimization option. Although we compile code with optimization option, value of const object will change, because variable is declared as volatile that means don't do any optimization.

	/* Compile code with optimization option */
	#include <stdio.h>
	 
	int main(void)
	{
		const volatile int local = 10;
		int *ptr = (int*) &local;
	 
		printf("Initial value of local : %d \n", local);
	 
		*ptr = 100;
	 
		printf("Modified value of local: %d \n", local);
	 
		return 0;
	}

Output:

	  [ashish@ubuntu]$ gcc -O3 volatile.c -o volatile -save-temp
	  [ashish@ubuntu]$ ./volatile
	  Initial value of local : 10
	  Modified value of local: 100
	  [ashish@ubuntu]$ ls -l volatile.s
	  -rw-r-r- 1 ashish ashish 711 2016-11-19 16:22 volatile.s
	  [ashish@ubuntu]$
  
The above example may not be a good practical example, the purpose was to explain how compilers interpret volatile keyword. As a practical example, think of touch sensor on mobile phones. The driver abstracting touch sensor will read the location of touch and send it to higher level applications. The driver itself should not modify (const-ness) the read location, and make sure it reads the touch input every time fresh (volatile-ness). Such driver must read the touch sensor input in const volatile manner.

Can a variable be both const and volatile?
-----------------------------------------
yes, the const means that the variable cannot be assigned a new value. The value can be changed by other code or pointer. For example the following program works fine.

	int main(void)
	{
		const volatile int local = 10;
		int *ptr = (int*) &local; 
		printf("Initial value of local : %d \n", local); 
		*ptr = 100; 
		printf("Modified value of local: %d \n", local); 
		return 0;
	}

What is the difference between declaration and definition of a variable/function
--------------------------------------------------------------------------------
Declaration of a variable/function simply declares that the variable/function exists somewhere in the program but the memory is not allocated for them. But the declaration of a variable/function serves an important role. And that is the type of the variable/function. Therefore, when a variable is declared, the program knows the data type of that variable. In case of function declaration, the program knows what are the arguments to that functions, their data types, the order of arguments and the return type of the function. So that's all about declaration. Coming to the definition, when we define a variable/function, apart from the role of declaration, it also allocates memory for that variable/function. Therefore, we can think of definition as a super set of declaration. (or declaration as a subset of definition). From this explanation, it should be obvious that a variable/function can be declared any number of times but it can be defined only once. (Remember the basic principle that you can't have two locations of the same variable/function).

	// This is only declaration. y is not allocated memory by this statement 
	extern int y; 

	// This is both declaration and definition, memory to x is allocated by this statement.
	int x;
	  
What are different storage class specifiers in C?
-------------------------------------------------
auto, register, static, extern

What is scope of a variable? How are variables scoped in C?
-----------------------------------------------------------
Scope of a variable is the part of the program where the variable may directly be accessible. In C, all identifiers are lexically (or statically) scoped.
**Lexical scoping** (sometimes known as static scoping ) is a convention used with many programming languages that sets the scope (range of functionality) of a variable so that it may only be called (referenced) from within the block of code in which it is defined. The scope is determined when the code is compiled. A variable declared in this fashion is sometimes called a private variable.
The opposite approach is known as **dynamic scoping** . Dynamic scoping creates variables that can be called from outside the block of code in which they are defined. A variable declared in this fashion is sometimes called a public variable.

What is NULL pointer? 
---------------------
NULL is used to indicate that the pointer doesn't point to a valid location. Ideally, we should initialize pointers as NULL if we don't know their value at the time of declaration. Also, we should make a pointer NULL when memory pointed by it is deallocated in the middle of a program.

What is Dangling pointer?
-------------------------
Dangling Pointer is a pointer that doesn't point to a valid memory location. Dangling pointers arise when an object is deleted or deallocated, without modifying the value of the pointer, so that the pointer still points to the memory location of the deallocated memory. Following are examples.

*Example 1*

	int *ptr = (int *)malloc(sizeof(int));
	.............
	.............
	free(ptr); 
 
	// ptr is a dangling pointer now and operations like following are invalid	
	*ptr = 10;  // or printf("%d", *ptr);

*Example 2*

	int *ptr = NULL
	{
	   int x  = 10;
	   ptr = &x;
	}
	// x goes out of scope and memory allocated to x is free now.
	// So ptr is a dangling pointer now.
	
What are local static variables? What is their use?
---------------------------------------------------
A local static variable is a variable whose lifetime doesn't end with a function call where it is declared. It extends for the lifetime of complete program. All calls to the function share the same copy of local static variables. Static variables can be used to count the number of times a function is called. Also, static variables get the default value as 0. For example, the following program prints "0 1"

	#include <stdio.h>
	void fun()
	{
		// static variables get the default value as 0.
		static int x;
		printf("%d ", x);
		x = x + 1;
	}
	 
	int main()
	{
		fun();
		fun();
		return 0;
	}
	// Output: 0 1
	
What are static functions? What is their use?
----------------------------------------------
In C, functions are global by default. The "static" keyword before a function name makes it static. Unlike global functions in C, access to static functions is restricted to the file where they are declared. Therefore, when we want to restrict access to functions, we make them static. Another reason for making functions static can be reuse of the same function name in other files.

Assertions in C/C++
-------------------
Assertions are statements used to test assumptions made by programmer. For example, we may use assertion to check if pointer returned by malloc() is NULL or not.

**Following is syntax for assertion**

	void assert( int expression ); 

If expression evaluates to 0 (false), then the expression, sourcecode filename, and line number are sent to the standard error, and then abort() function is called.

For example, consider the following program.

	#include <stdio.h>
	#include <assert.h>
	 
	int main()
	{
		int x = 7;
	 
		/*  Some big code in between and let's say x 
		   is accidentally changed to 9  */
		x = 9;
	 
		// Programmer assumes x to be 7 in rest of the code
		assert(x==7);
	 
		/* Rest of the code */
	 
		return 0;
	}

Output

	Assertion failed: x==5, file test.cpp, line 13 

**Assertion Vs Normal Error Handling**

Assertions are mainly used to check logically impossible situations. For example, they can be used to check the state a code expects before it starts running or state after it finishes running. Unlike normal error handling, assertions are generally disabled at run-time. Therefore, it is not a good idea to write statements in asser() that can cause side effects. For example writing something like assert(x = 5) is not a good ideas as x is changed and this change won't happen when assertions are disabled. See this for more details.

**Ignoring Assertions**

In C/C++, we can completely remove assertions at compile time using the preprocessor **NDEBUG**.

	// The below program runs fine because NDEBUG is defined
	# define NDEBUG
	# include <assert.h>
	 
	int main()
	{
		int x = 7;
		assert (x==5);
		return 0;
	}
	
The above program compiles and runs fine.

C Precedence Table
--------------------
<table>
        <tr>
          <th>
            <p align="center"><b 
            >Operator</b></p></th>
          <th><b>Description</b></th>
          <th>
            <p align="center"><b 
            >Associativity</b></p></th></tr>
        <center>
        <tr>
          <td align="center"><font size="2" 
            >( )<br>[ ]<br 
            >.<br>-&gt;<br 
            >++ --</font></td>
          <td><font size="2">Parentheses (function call) 
            (see Note 1)<br>Brackets (array subscript)<br 
            >Member selection via object name<br 
            >Member selection via pointer<br 
            >Postfix increment/decrement (see Note 
          2)</font></td>
          <td valign="top">
            <p align="center"><font 
            size=2>left-to-right</font></p></td></tr>
        <tr>
          <td align="center"><font 
            ><font size="2"><font>++ 
            --<br>+ -<br>! ~<br 
            >(<i>type</i>)<br 
            >*<br>&amp;<br 
            >sizeof</font> </font></font></td>
          <td><font size="2">Prefix increment/decrement<br 
            >Unary plus/minus<br 
            >Logical negation/bitwise complement<br 
            >Cast (convert value to temporary value of <i 
            >type</i>)<br 
            >Dereference<br>Address (of 
            operand)<br 
            >Determine size in bytes on this implementation</font></td>
          <td valign="top" align="center"><font 
            size=2>right-to-left</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >* &nbsp;/&nbsp; %</font></td>
          <td><font 
            size=2>Multiplication/division/modulus</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >+ &nbsp;-</font></td>
          <td><font size="2">Addition/subtraction</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >&lt;&lt;&nbsp; &gt;&gt;</font></td>
          <td><font size="2">Bitwise shift left, Bitwise 
            shift right</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >&lt;&nbsp; &lt;=<br 
            >&gt;&nbsp; &gt;=</font></td>
          <td><font size="2">Relational less than/less than 
            or equal to<br>Relational greater than/greater 
            than or equal to</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >== &nbsp;!=</font></td>
          <td><font size="2">Relational is equal to/is not 
            equal to</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >&amp;</font></td>
          <td><font size="2">Bitwise AND</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >^</font></td>
          <td><font size="2">Bitwise exclusive OR</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >|</font></td>
          <td><font size="2">Bitwise inclusive OR</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >&amp;&amp;</font></td>
          <td><font size="2">Logical AND</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >| |</font></td>
          <td><font size="2">Logical OR</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >? :</font></td>
          <td><font size="2">Ternary conditional</font></td>
          <td valign="top" align="center"><font 
            size=2>right-to-left</font></td></tr>
        <tr>
          <td align="center"><font size="2" 
            >=<br>+= &nbsp;-=<br 
            >*=&nbsp; /=<br>%=&nbsp; 
            &amp;=<br>^=&nbsp; |=<br 
            >&lt;&lt;=&nbsp; &gt;&gt;=</font></td>
          <td><font size="2">Assignment<br 
            >Addition/subtraction assignment<br 
            >Multiplication/division assignment<br 
            >Modulus/bitwise AND assignment<br 
            >Bitwise exclusive/inclusive OR assignment<br 
            >Bitwise shift left/right assignment</font></td>
          <td valign="top" align="center"><font 
            size=2>right-to-left</font></td></tr>
        <tr>
          <td>
            <p align="center"><font size="2" 
            >,</font></p></td>
          <td><font size="2">Comma (separate 
            expressions)</font></td>
          <td valign="top" align="center"><font 
            size=2>left-to-right</font></td></tr>
        <tr>
          <td colspan="3">
            <blockquote>
              <dl>
                <dt style="MARGIN-TOP: 12px"><font 
                size=2><b>Note 1:</b> </font>
                <dd><font size="2">Parentheses are also used 
                to group sub-expressions to force a different precedence; such 
                parenthetical expressions can be nested and are evaluated from 
                inner to outer. </font>
                <dt><font size="2"><b 
                >Note 2:</b> </font>
                <dd><font size="2">Postfix 
                increment/decrement have high precedence, but the actual 
                increment or decrement of the operand is delayed (to be 
                accomplished sometime before the statement completes execution). 
                So in the statement <font><b 
                >y = x * z++; </b></font>the current value 
                of <font><b 
                >z</b></font> is used to evaluate the 
                expression (<i>i.e., </i><font 
                ><b>z++ 
                </b></font>evaluates to <font><b 
                >z</b></font>) and <font 
                ><b>z</b></font> only 
                incremented after all else is done. 
        </font></dd></dl></blockquote></td></tr></center></table>

References
----------
* http://geeksquiz.com/

Awesome sites about C programming
------------------------------------
* http://sathyamvellal.in/blog/cool-c-programming/
