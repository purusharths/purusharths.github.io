---
title: "C++ 11 Reference Guide"
summary: C++11 guide taken from Dr. Ole Klein's Lecture
date: 2021-05-11 10:14
Tags: 
  - c++
  - scientific-computing
---

For full lecture and scirpt visit [OOPFSC](https://conan.iwr.uni-heidelberg.de/teaching/oopfsc_ws2020/)
# C++ 11 a reference guide
# Table of Contents
1. [Introduction](#introduction)
    + [Stack and Heap](#stack-heap)
    + [References and Pointers](#references)
    + [Static](#static)
    + [lvalue and rvalue references](#lrref)
    + [const](#const-expr)
    + [auto](#auto)
    + [order of precedence](#oderprecedence)
    + [enum](#enum)
    + [move scemantics](#moveschem)
    + [operator overloading](#operatoroverload)
    + [function parameter dissection(int&, const )](#funcparam)
    + [constexpr](#constexpr)
    + [explicit](#explicit)
    + [Inheritance](#inheritance)
2. [Function Pointers](#funcpointer)
    + Function Pointers
    + Functors
    + Lambda
3. [Constructors](#constructors)
    + Default
    + Copy Constructor and copy assignment operator
    + Move Constructor and move assignment operator
    + Delegating constructor 
    + Rule of three and Five
4. [Standard Template Library](#stl)
5. [Containers](#containers)
    + Sequences
        + array
        + std::vector
        + Other Sequences
    + Associative Containers
    + unordered map
    + Complexity Gurantee
5. [Iterators](#iterators)
    + range based loops
6. [Algorithms](#algorithms)
    + transform
    + bind
    + for_each
    + count_if, copy_if, find_if, shuffle
7. [Companion Classes](#companion-classes)
    + std::pair
    + std::tuple 
9. [Exception](#exception)
    + throwing and catching exceptions
    + static
    + static_assert
10. [RAII](#raii)
11. [Smart Pointers](#smart-pointers)
    + Unique_pointer
    + Shared_pointer
    + Weak Pointer
12. [Templates](#templates)
    + Templates
    + Templates and classes
    + Template Template Prameters
    + Template argument deduction
    + Template Specilization (explicit, partial, implicit)
    + Template Metaprogramming
    + Overloading templates
    + SFINAE
    + variadic templates
13. [Polymorphism](#polymorphism)
    + Static<br>
    + Dynamic<br>
14. [Threads](#threads)
15. [Misc](#misc)
    + Using
    + typedef
    + namespaces
    + auto, decltype, declvalue
    + trailing return type
    + different ways of initialization

---
## Introduction <a name="introduction"></a>
  + ### Stack&Heap
```cpp
Entity e; // on stack
Entity* e = new Entity(); // on heap. Heap allocation returns a memory address
```
  + ### References
```cpp
int main(){
    int a = 5;
    int& b = a;
    int* c = &a;

    // reference to a pointer value!!
    //  so that the value is not copied into a new vairable.
    int& d = *c; // value at address of a.

    std::cout<<a<<std::endl;
    std::cout<<b<<std::endl;
    std::cout<<c<<std::endl;
    std::cout<<d<<std::endl;
    a = 2;
    int& e = *c; // value at address of a
    std::cout<<e<<std::endl;
}
OUTPUT: 
5
5
0x7fffb10d4db4
5
2
```
  + ### Static
  + ### lrref
  + ### const
  + ### Auto
  + ### order of precedence
      `(*foo)(20)`: `(*foo)`is a pointer pointing to a function with inteer args
      ```cpp
      [] > *
        *foo(20) -> points to the value of foo with paramter 20
        (*foo)(20) -> 
          |     |__________> Give 20 as param to it
       Location of  foo -----------^
      ```
  + ### enum
  + ### move scemantics
  + ### operator overloading
  + ### function parameter dissection (int&, const )
  + ### constexpr
  + ### explicit
  + ### inheritance
```cpp 
class Base {
protected:
  int prot;

public:
  Base() : prot() {} // initlize prot to default
};

class Derived : public Base {
public:
  void print() { std::cout << prot << std::endl; }
};

int main() {
  Derived d;
  d.print();
}
```

**Calling Base class Constructor**
```cpp 
class Base {
protected:
  int prot;

public:
  Base(int a) : prot(a) {} // initlize prot to default
};

class Derived : public Base {
public:
  Derived(int d): Base(d) {}
  void print() { std::cout << prot << std::endl; }
};

int main() {
  Derived d(10);
  d.print();
}
```


`friend`: private members of a class are not accessible to outside code, unless a class is marked as friend.
```cpp 
// Friend class

class GetCustomerData {
public:
  static std::string GetName(Customer &customer) { return customer.name; }
};

class Customer {
private:
  friend class GetCustomerData;
  std::string name;

public:
  Customer(std::string name) : name(name) {}
};

int main() {
  Customer tom("Tom");
  GetCustomerData getName;
  std::cout << getName.GetName(tom);
}
```



```cpp 
struct Shape { // Generic type: Shape
    double length, width;

    Shape(double l = 1, double w = 1 ){
        length = l;
        width = w;
    } // structs have public constructors

    double Area(){
        return length * width;
    }

private:
    int id;

};

struct Circle : Shape{
    Circle(double width){
        this->width = width;
    }

    double Area(){
        return 3.1459 * std::pow((width/2),2);
    }
};

int main(){
    Shape shape (10, 10);
    std::cout << "Square Area: " << shape.Area() << std::endl;

    Circle circle(10);
    std::cout << "Circle Area: " << circle.Area() << std::endl;

    Shape rectangle{10,15}; // initilization by aggreegate
    std::cout << "Square Area: " << rectangle.Area() << std::endl;
}


```

----
## Function Pointers <a name="funcpointer"></a>
  + ### Function Pointers
      Normal pointers but points to a function.
      ```cpp
      int func(a, b){
          return a+b;
      }

      (*func)(1,2)
      ```
      Example:
      ```cpp
        double someComplexFunction(int val) { return sin(val) + tan(val); }

        void PrintVector(int val) { std::cout << ": " << val << std::endl; }

        void ForEach(const std::vector<int> &values, // takes a vector
        // function pointer to a function which takes an int and returns double
                     double (*mathfunc)(int val), 
                     void (*printfunc)(int val2)) { 
            for (int value : values) {
                printfunc(mathfunc(value));
            }
        }

        int main() {
        std::vector<int> values = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        ForEach(values, someComplexFunction, PrintVector);
        }      
      ```
  + ### Functors
    + Are like Function objects, works as function and are created by overloading ``operator()``.
    + Basically overload the `()` operator so that it can be called by the object as fuction.
    + Used in built-in functions, parameter bindings, and play an important role in STL. 
    ```cpp
    double POW(double x, double y) { return pow(x, y); }

    // pratical example
    // can't use template because the value can be non-constant during compile 
    // time add2 is just clunky

    template <typename T> class AddValue {
      T val;

    public:
      AddValue(T j) : val(j) {}
      void operator()(T i) { std::cout << i + val << std::endl; }
    };

    class TestFunct {
    public:
      TestFunct(double x) : value(x){};
      double operator()(double val) { return value * val; }
      operator std::string() const { return "X"; }
      double get_value() const { return value; }

    private:
      double value;
    };

    int main() {
      // -------------------------------------------------** USE OF FUNCTORS **/
      //   TestFunct t(2);
      //   t(5);
      //   std::cout << t(5)  << std::endl;
      //   std::cout << (std::string)t << std::endl;

      // -----------------------------------------------** 1. Built in functions
      int a = 4, b = 5;
      if (std::less<int>()(a, b)) { // a < b search for other built in funcitons
      }

      //---------------------------------------------------- 2. Parameterized
      // Functions
      AddValue<int> adval(20);
      std::vector<int> vec = {1, 2};
      int x = 20; // will not work with templates
      std::for_each(vec.begin(), vec.end(), AddValue<int>(x));

      //------------------------------------------------------- 3. Parameter
      // Binding
      std::set<int> myset = {2, 3, 5,
                             6}; // multiply with 10 and save the result in vec3
      std::vector<int> vec3;

      int x3 = std::multiplies<int>()(2, 3);

      std::transform(
          myset.begin(), myset.end(),
          std::back_inserter(vec), // save the result in vec
          std::bind(std::multiplies<int>(), std::placeholders::_1,
                    10)); // bind function because transform takes only oneparam 
                        //  placeholder -> first param from set and second is 10

      // //------------------------------------------- 4. convert function to
      // functor

      auto f = std::function<double(double, double)>(POW); // now a functor?
    }
    ```
  
  + ### Lambda
      Throwaway functions
        `[capture clause] (parameters) -> return-type  { definition of method }` 
        eg:
        
      ```cpp  
      auto func_square = [&](int i) mutable  {a = 1;return i*i+a;};
      ```
       When you start to write more complex lambdas you will quickly encounter cases where the return type cannot be deduced by the compiler. To resolve this you are allowed to explicitly specify a return type for a lambda function, using -> T:
      ```cpp  
        void func4(std::vector<double>& v) {
        std::transform(v.begin(), v.end(), v.begin(),
        [](double d) -> double {
            if (d < 0.0001) {
                return 0;
            } else {
                return d;
            }
        });
        }
      ```
      #### "Capturing" variables
      So far we've not used anything other than what was passed to the lambda within it, but we can also use other variables, within the lambda. If you want to access other variables you can use the capture clause (the [] of the expression), which has so far been unused in these examples, e.g.:
      ```cpp
      void func5(std::vector<double>& v, const double& epsilon) {
            ...
              [epsilon](double d) -> double { ... }
            ...  
      ```
      + Can capture both by reference and value.
        + `[&epsilon]` captures by reference
        + `[&]` captures all variables used in the lambda by reference
        + `[=]` captures all variables used in the lambda by value
        + `[&, epsilon]` captures variables like with [&], but epsilon by value
        + `[=, &epsilon]` captures variables like with [=], but epsilon by reference
      




        

---
## Constructors <a name="constructor"></a>
From GFG:
    
>Let us understand the types of constructors in C++ by taking a real-world example. Suppose you went to a shop to buy a marker. When you want to buy a marker, what are the options? The first one you go to a shop and say give me a marker. So just saying give me a marker mean that you did not set which brand name and which color, you didn’t mention anything just say you want a marker. So when we said just I want a marker so whatever the frequently sold marker is there in the market or in his shop he will simply hand over that. And this is what a default constructor is! The second method you go to a shop and say I want a marker a red in color and XYZ brand. So you are mentioning this and he will give you that marker. So in this case you have given the parameters. And this is what a parameterized constructor is! Then the third one you go to a shop and say I want a marker like this(a physical marker on your hand). So the shopkeeper will see that marker. Okay, and he will give a new marker for you. So copy of that marker. And that’s what copy constructor is!
  + ### Default
  Default constructor is the constructor which doesn’t take any argument. It has no parameters. If we do not specify a constructor, C++ compiler generates a default constructor for us (expects no parameters and has an empty body).
  ```cpp
    construct(){
        a = 10;
        b = 20;
    }  
  ```
Even if we do not define any constructor explicitly, the compiler will automatically provide a default constructor implicitly.

  + ### Copy Constructor and copy assignment operator
  Copy constructor is used when an object is being copied. A copy constructor performs a deep copy of all the member variables especially pointers.
  Classes have shallow copy by default.
  ```cpp
  // Copying basics
    struct Vector2 {
      float x, y;
    };

    int main() {
      int a = 2;
      int b = a; // two seprate vars created
      b = 3; // changing the value of b dosen't effect a
      std::cout << a << std::endl;  // 2

      Vector2 original = {3, 5};
      Vector2 copy = original; // two seprate vars created
      copy.x = 10; // changing the value of copy dosen't affect original
      std::cout << original.x << std::endl; // 3

      Vector2 *heap_original = new Vector2(); 
      Vector2 *heap_copy = heap_original; // copying the memory address
      
      // changing the value of copy DOES change the value of original
      heap_copy->x = 10;  

      std::cout << heap_original->x << std::endl;  // 10
    }
  ```
  This is problamatic, because if we had created a copy and the original object was deleted (calling the destructor to the original pointer), the copied object will refer to a freed up memory (segmentation fault).
  
  Copy constructor takes the const object of the same class: `ClassName(const ClassName &old_obj)`.
  ```cpp 
  class String{
    private:
      char *m_buffer;
      size_t m_size;

    public:
      String(const char *str) { // Paramterized constructor
        m_size = strlen(str);
        m_buffer = new char[m_size + 1];
        memcpy(m_buffer, str, m_size);
      }
    // String s2 = s1;
      String(const String &strobj) { // Copy constructor
        m_size = strobj.m_size; // copy the size of the object being passed
        // m_size = s1.size;
        memcpy(m_buffer, strobj.m_buffer, m_size + 1);
      }
   }
  ```
  Copy assignment operator
  The assignment operator for a class is what allows you to use = to assign one instance to another. For example:
  ```cpp
  MyClass c1, c2;
  c1 = c2;  // assigns c2 to c1 
  ```
If you do not declare an assignment operator, the compiler gives you one implicitly. The implicit assignment operator does member-wise assignment of each data member from the source object.
  ```cpp
      Test t1, t2;
      t2 = t1;  // calls assignment operator, same as "t2.operator=(t1);"
      Test t3 = t1;  // calls copy constructor, same as "Test t3(t1);"
  ```
  
  Set copy constructor to `delete` to disable copying (for instance in unique pointers). 
  ```cpp
  String(const char* str) = delete;
  ```
  + ### Move Constructor and move assignment operator
    #### lvalue and rvalue references
    + lvalue: an object that occupies some identifiable location in memory.
    + rvalue: an object that is not lvalue
        + `int i;` lvalue because `&i` gives the location of i.
        + (i+2),(x+y) are rvalues, &(i+2) gives an error.
    + References in general are lvalue references.
    + lvalues can be implicitly transformed into rvalues, but not the other way around.
    
    Returning lvalues from function:
    ```cpp
    int global;

    int& foo(){ return global; }
    ...

    foo() = 5000;
    std::cout << global; // 5000
    ```
    C++ has a lot of const references because const references can take both lvalues and rvalues.
    
    ```cpp 
    #include <iostream>

    // lvalue reference with const - it can accept rvalues as well
    void function(const int &val) { 
      std::cout << val << std::endl;
    }

    void function(int &&val) { // rvalue reference
      std::cout << "Called with value: " << val << std::endl;
    }

    int main() {
      int a = 30;
      function(a);
      function(10);
    }
    ```
    Note that rvalue references don not necerssirely denote rvalue refernce in templated functions. It depends on teh type that is used to instantiate the template. 
    If instantiated with lvalue/rvalue, it collapses to lvalue/rvalue respectively.
    
    With rvalue references, we have a way to detect temp values (since rvalue in essence is temp). This way we can arrange something special for temp values.
    
    **Rvalue references are used for move schemantics and perfect forawrding**
    
    + #### Move Schemantics
        + allows to move objects around
        + single biggest usecase of rvalue.
        + wasn't possible before c++11

    Move constructor moves the resources in the heap (instead of copying),  preventing unnecessary copying of data in the memory.
    
    ```cpp
                  // rvalue reference
        Object_name(Object_name&& obj) : data{ obj.data } {
            // Nulling out the pointer to the temporary data
            obj.data = nullptr;
        }
    ```
    
    ```cpp
    private:
       int* data;
       ..
    public:
       Move(Move&& source) : data{ source.data } {
            source.data = nullptr;
       }    
    ```
    + #### Perfect forwarding
    
    
  + ### Delegating / converting constructor
      + Allows a constructor to invoke another constructor.
      + Reduces code duplication.
    ```cpp
    // default constructor delegates the assignemnt to Paramterized constructor
    Entity() : Entity(0, 0) { 
     std::cout << "Default Constructor " << std::endl; 
    }
    Entity(int val1, int val2) : Entity(val1, val2, 0) {
    std::cout << "Double Constructor with values " << val1 << " " << val2
              << std::endl;
    }
    Entity(int val1, int val2, int val3) : a(val1), b(val2), c(val3) {
    std::cout << "Final Constructor with values " << val1 << " " << val2 << " "
              << val3 << std::endl;
    }
    ~Entity() {}
    };
    ```
  + ### Rule of three and Five

## Standard Template Library <a name="#stl"></a>

The Standard Library is a set of classes and functions that is part of the C++ language standard. It provides most of the common “tools of the trade”: data structures and associated algorithms, I/O and file access, exception handling, etc. The components are easily recognized because they are in the std namespace.

Most general STL parts:
+ input and output streams
+ containers (a.k.a. data structures) and iterators
+ algorithms and functors
+ companion classes (pair and tuple)
+ exceptions


## Containers <a name="containers"></a>
Containers are Data Structures. C++ provides different types of containers. (#addflowchart)
1. *Sequences* (Elements are associated with integer index)
    * Vector, arrays, list, dequeue, forward list.
2. *Associative Containers* (Arbitary index type)
    * set, map, multi-set, multi-map.
3. *Unsorted associative containers* (based on hash tables, faster than associative containers)
4. *Container Adapters*
    * Stack (LIFO), Queue (FIFO), Priority Queue.

The elements of container objects all have the same type, specified as a template parameter. This restriction can be somewhat lifted through dynamic polymorphism (how?)
1. ## Sequences
  + ### array
  ```c++int stack_array[20];
	int* arr = new int[10]; // heap
	int* ptr = arr; // array var itself is a pointer

	*(ptr+4) = 100; // changes value in a

	for(int i = 0; i<10; i++){
		std::cout << arr[i]<< std::endl;
	}
    
    
    OUTPUT
    0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 
  ```
  + ### std::vector
      Creation:
      ```c++ 
      std::vector<typename> first = {1,2};
      std::vector<int> second (4,100); // four ints with value 100
      std::vector<int> third (second); // a copy of second
      std::vecotr<int> test;
      test.push_back(10); // add 10 to test
      test.push_back({4,5,6});
      ```
      Create a 2D vector and initilize all entries to 0
      ```cpp
        int main(){ 
            int m = 2, n = 5;
            vector<vector<int>> vec(m, vector<int> (n, 0));
            return 0;
        }
      ```
      Access elements with `test.get(0)` or `test[0]` (Operator [] was overloaded for easier access)
      While resizing, `std::vector` needs to copy all elements (?).
      Looping through the vector: use for-each
      ```cpp
      for(int& v : first){
          std::cout << v << std::endl;
      }
      // equivalent for loop
      for(int i = 0; i< vec.size(); i++){
          std::cout << v[i] << std::endl;
      }
      ```
      Always trasfer vectors as reference to avoid unnecessary copies. Use `const` if the vector is not expected to be modified. <br>
      **push_back vs emplace_back**
      STL containers now uses emplace_back which lets the container create an object rather than it being mannually created and then being copied. 
      ```cpp
      struct Point{ 
          int x, y;
          Point(int xp, int xy): x{xp}, y{xu} {};
      };
      int main(){
          std::vector<Point> vec;
          // push_back
          Point p1(2,2);
          vec.push_back(p1);
          // vs
          vec.emplace_back(4,4); // doesn't need a copy.
      }
      
      ```
      With emplace, we provie the constructor arguments, and the container creates the object.
      
      **2D vector**
      ```cpp
      std::vector<std::vector<double>> vec;

      for (int i = 0; i < vec.size(); i++) {
        std::vector<double> tmp_var;
        for (int j = 0; j < ydata.size(); j++) {
          tmp.push_back(function(xdata[i][j], ydata[i][j]));
        }
    vec.push_back(tmp_var);
      ```
* ### Other Sequences 
      - array: `int arr[100]` (Stack) and `int* heapArray = new int[100];` (heap)
      - list: `std::list<double> c; // empty doubley-linked list.` 
      - stack: `std::stack<int, std::vector> b; // Stack based on vector` 
      - queue: `std::queue<int, std::list> d; // Queue based on list`

2. ## Associative Containers
    * Set: key is unique and identical to its associated value
    * Multiset: like set, but key may appear multiple times
    * Map:  key is unique, value is pair of index and some mapped type
    * multimap:  like map, but key may appear multiple times
3. ## unordered map
```c++

    std::unordered_map<std::string, int> map1;

    map1["Puru"] = 5;
    map1["C++"] = 20; 

    using dict = std::unordered_map<std::string, int>;

    // how to iterate?

    for (dict::const_iterator it = map1.begin(); it!=map1.end(); it++){
        // & so as not to copy the values because `it` is a pointer. check test.cpp
        const std::string& key = (*it).first;//it->first;
        const int& value = it->second;        
        std::cout<<  key <<":" <<  value <<std::endl;
    }
```

4. ## Complexity Gurantee
|                               | Access    | Add/Del Element    |
|-------------------------------|-----------|-------------|
| std::vector                   | O(1)      | O(1)\*, O(N) |
| std::list                     | O(N)      | O(1)        |
| sorted associative containers | O (log N) | O (log N)   |
| Unsorted associative containers| O(1)*,O(N) | O(1)*,O(N)|

\*amortized (avergaged over many calls)

Use vector by default. 

      
 ---
## Iterators <a name="iterators"></a>
Main way to interact with containers is via iterators. Moreover, iterators are mandatory for containers which do not have simple indexing system (contigious memory). Being generilization for pointers, iterators can be dereferenced(\*) and advanced(++). For each container type there exists:

```c++
T::iterator // read/write to container
T::const_iterator // read only access
begin() // returns iterator pointing at the first values
end() // returns iterator pointing at one pos past last element.
cbegin() // read only
cend() // read only
rbegin/end // reverse order
```
  + ### range based loops
      How dows range based for loop work? Vector class provide begin and end class.

    ```c++
    for(std::vector<int>::iterator it = values.begin(); it != values.end(); it++){
        std::cout<< *it <<std::endl;
    }
    ```

> What actually is an iterator?
> It's not a type or a class or an interface, infact, iterator is a concept.
> It's a name for something that has the properties needed by an iterator 
> 1. Supporting comparision using `!=`
> 2. Increment using `++`
> 3. And dereference using `*`
> Anything can be used as an iterator as long as it supports these three operations (think groups in abstract algebra).


---



## Algorithms <a name="algorithms"></a>
Many algorithms expect some criterion, transofrm or operation which has to be supplied as a functor or lambda (eg `for_each`).
```cpp
std::vector<int> vec = {6, 1, 2, 3, 5, 7, 8, 0, 0, 0, 1, 2};
```
 - sort: `std::sort(vec.begin(), vec.end());` // sort modifies the vector
 - reverse:     `std::reverse(vec.begin(), vec.end());`
 - count the number of instances of a number: `std::count(vec.begin(), vec.end(), 0)` // count number of instances of 0
 - max: `int max = *std::max_element(vec.begin(), vec.end()); // max_element is an iterator`
 - min: `int min = *std::min_element(vec.begin(), vec.end()); // max element is an iterator`
  
  + ### transform
  + ### bind
  + ### for_each
  ```cpp
    auto sq = [](int& i) {i= i*i;}; 
    std::for_each(vec.begin(), vec.end(), sq);
    print(vec);
  ```

  + ### count_if, copy_if, find_if, shuffle
```cpp

    auto even = [](int i) {
        if (i%2 == 0) {std::cout<<"T "; return true;}
        else {std::cout<<"F ";return false;}
    };
    
    std::count_if(vec.begin(), vec.end(), even); // does not modify the original vector
    std::cout<<"\n";


    // copy_if copy vector
    std::vector<int> copy_vec(vec.size(), -1);
    std::copy_if(vec.begin(), vec.end(), copy_vec.begin(), [](int& i){ return (i>30); });
    print(copy_vec);

    // find_if 
    std::vector<int>::iterator it = std::find_if (vec.begin(), vec.end(), [](int i){return (i%2==0);});
    std::cout << "First even value: " << *it <<std::endl; 

    // shuffle


    auto rng = std::default_random_engine {};
    std::shuffle(vec.begin(), vec.end(), rng);
    print(vec);

```
Output:
```OUTPUT
6 1 2 3 5 7 8 0 0 0 1 2    Original vector
0 0 0 1 1 2 2 3 5 6 7 8    Sort (Original Vector changed)
8 7 6 5 3 2 2 1 1 0 0 0    Reverse (Original vector changed)
Max: 8 Min: 0
3                          Number of occurances of 0
--------------------
(Reminder) Vector now: 8 7 6 5 3 2 2 1 1 0 0 0 
--------------------
for_each: 64 49 36 25 9 4 4 1 1 0 0 0  // i^2 (modifies original vector (!))
count_if: T F T F F T T F F T T T  // i%2==0 (does not modify the original vector)
copy_if:  64 49 36 -1 -1 -1 -1 -1 -1 -1 -1 -1  // copy to copy_vec if i>30
find_if   64 // first even value
shuffle:  36 1 0 4 0 64 9 0 4 25 49 1 
```
Recap
```
for each: apply some function to each element (lifting)
count if: count elements with certain properties
find if: find first element with such property
copy if: insert applicable elements into other container
shuffle: randomly re-order container contents
sort: sort container according to some criterion
```
<hr>

## Companion Classes <a name="#companion-classes"></a>

+ ### std::pair
`std::pair` is used to store a pair (only 2) of values of different types.
```cpp    #include <tuple>
std::pair<int, std::string> p = std::make_pair(23, "Hello");
std::cout << p.first << ", " << p.second << std::endl;
```
+ ### std::tuple
`std::tuple` kind of extends pair. Instead of storing just two values, std::tuple can be used to store arbitary number of values with arbitary data types.

```cpp
std::tuple<int, std::string, char> t(32, "Test", 't');
std::cout << std::get<0>(t) << std::endl;
std::cout << std::get<1>(t) << std::endl;
std::cout << std::get<2>(t) << std::endl;
```

get<>() function returns the reference to the variable stored in the tuple.
```cpp
int& s = std::get<0>(t);
s = 55; // changes get<0>(t) value to 55
```

Different ways of creating tuple
```cpp
std::tuple<int, std::string, char> t2; // uses default constructor
t2 = std::tuple<int, std::string, char>(11, "alpha", 'd');
t2 = std::make_tuple(2000, "beta", 'c');
```

Comparison
```c++
if (t < t2){ // lexicographical comparision
        t = t2; // assignment possible, member to member copy
    }
```
`std::tuple` can store references (unlike other STL containers (who always use copying or moving(?)))

```cpp
std::string st = "able was i";
std::tuple<std::string&> t3(st); // single memeber tuple stores reference to the string
std::get<0>(t3) = "ere i saw elba"; // st  is now changed
```
PS: to add value to referenced variable inside tuple, create reference wrapper:
```cpp
std::string vader = "Luke, I'm your...";
t3 = std::make_tuple(std::ref(vader)); // create reference wrapper and pass it to make_tuple
```

Unpacking tuple values
Say we want to store the value of t2 in a set of variable `int x; string y; char z`, we can do:
```cpp
std::make_tuple(std::ref(x), std::ref(y), std::ref(z)) = t2;
// OR 
std::tie(x,y,z) = t2;
// with std::tie, we can ignore a value if required.
std::tie(x, std::ignore, z) = t2;
```
Concatinate two tuples.
```cpp
// if std::tuple<int, std::string, char> t2, and std::tuple<std::string> t3 we have
auto t4 = std::tuple_cat(t2, t3) //t4 is a tuple with <int, string, char, string>
```
Tuple type traits.
This prints the tuple size of the type of t4:
```cpp
std::tuple_size<decltype(t4)>::value // 4
std::tuple_element<1, decltype(t4)>::type d; // d is a string (element 1 of type of t4 is a string)
```

> Note: tuple makes more sense as vector of tuples (list of tuples). 
```cpp 
std::vector<std::tuple<int, std::string, char>> tuple_vec;
tuple_vec.push_back(std::make_tuple(1, "Alpha", 'a'));
```
---
## Exceptions <a name="#exceptions"></a>
Error handling mechanism for situations that are not normal but may occur sporadically eg FileNotFound, MatrixIsSingular.
```cpp 
if (...){
    throw std::domain_error(msg);
}
```

+ ### throwing exceptions
```cpp
#include <exception>
...
try {
    TestDest t1(-1); // object created
    if (t1.get_val() < 0){
        throw std::domain_error("Received negative value"); // throwing exception
   }
} catch (std::exception& e) { // exception catched
        std::cerr << "Negative value Exception" << e.what() << std::endl;
        // in pratice do something better than printing the value
}
```
 
**Custom exceptions** may be defined by inheriting from `std::exception`.

```cpp 
class StackException : public std::exception {
	std::string msg;
public:
	StackException(const std::string& m) : msg(m) {}
	const char *what() const noexcept override {
		return msg.c_str();
	}
};

if (...){
    throw StackException("Empty Stack");
}
```
Points to consider:
+ Exceptions are for error conditions that can’t be handled locally
+ A return always returns to the immediate caller, but a throw unwinds
the call stack until a matching catch block is found
+ If none is found at all, the program is aborted (should be avoided if possible)
+ All function calls between the throw statement and the catch block are
stopped prematurely

> This means that local resources have to be handled in those intermediate functions (allocated memory, open file handles, ongoing communication) during stack unwinding. An elegant mechanism to do this automatically is → RAII.    


+ ### assert
     happens at run time: 
 ```cpp
 #include <cassert>
 int i = 20;
 assert(i == 9); // program will crash

 OUTPUT
 a.out: test.cc:6: int main(): Assertion `i==9' failed.
[1]    235265 IOT instruction (core dumped)  ./a.out
 ```
    
    
+ ### static_assert 
    Happens at compile time: 
```cpp
const int i = 20; // value should be visible to the compiler, hence const
static_assert(i == 9, "i not 9");
static_assert(data.size()<10, "Too large");

OUTPUT:
test.cc: In function ‘int main()’:
test.cc:6:20: error: static assertion failed: i not 9
6 |     static_assert(i==9);
  |                   ~^~~
```
    > before C++11, #if !defined(...) #error ... construct was used.


## RAII <a name="raii"></a>
Full Form: Resource Aquisition is Initilization

Based on the properties of constructors and destructors and their interaction with exception handling.
“Destruction is Resource Release” (DIRR) would be more appropriate, but the acronym RAII is now too well-known to change it


Central rules that enable RAII:
1. An object is only fully constructed when its constructor is finished.
2. A compliant constructor tries to leave the system in a state with as few
changes as possible if it can’t be completed successfully.
3. If an object consists of sub-objects, then it is constructed as far as its parts
are constructed.
4. If a scope (block, function. . . ) is left, then the destructors of all successfully
constructed objects are called.
5. An exception causes the program flow to exit all blocks between the throw
and the corresponding catch .

The interplay of these rules, especially the last two, automatically frees resources
before leaks can happen, even when unexpected errors occur.

Main idea of RAII:
* Tie resources (e.g., on the heap) to handles (on the stack)21, and let the
scoping rules handle safe acquisition and release
* Repeat this recursively for resources of resources
* Let the special rules for exceptions and destructors handle
partially-constructed objects


**Motivation:**
Object created on stack are destroyed automatically but have limited size, on the other hand, objects created on heap are expected to be destroyed mannually, and failing to do so will cause memory leak. 

Is there a way to create heap objects on Stack not have to worry about releasing their memory either manuualy or <u>*in case of an exception*</u> (i.e the heap objects gets destoryed as soon as it is out of scope) -> This can be done by RAII

Example:
```cpp  
#include <iostream>
#include <stdexcept>

class TestDest {
public:
  int *a = new int[4]; // on heap
  TestDest() { std::cout << "Created Object" << std::endl; };
  ~TestDest() {
    delete[] a;
    std::cout << "Deleted Array" << std::endl;
  };
};

int main(int argc, char const *argv[]) {
  int a = 5;
  { // new scope
        try {
          TestDest t1; // object created
          throw std::domain_error("Received negative value");
          std::cout << "EXCEPTION" << std::endl; // exception occured
        } catch (std::exception &e) {// exception catched
          std::cerr << "Error"l\n";
        } 
  }// object deleted. memory freed without explicitly deleting it:D
  return 0;
}
```


**Pratical Example: Measure time**
```cpp

#incldue <iostream>

class Timer{
private:
      std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
      std::chrono::duration<float> duration;    
public:
    Timer(){
        start = std::chrono::high_resolution_clock::now();
    }
    ~Timer(){
        end = std::chrono::high_resolution_clock::now();
        duration = end - start;
        std::cout << "" << duration.count() * 1000.0f << "ms " << std::endl;
    }
};

int main(){
    {
        Timer t1;
        ...
    } // Timer will be destroyed once out of scope and destructor will be called
}
```





---
## Smart Pointers <a name="smart-pointers"></a>
SP automates the process of calling delete by using RAII paradigm. Basically, when new is called, delete should follow "automatically" when out of scope. <u>smart pointers can be thought of as a wrapper around raw pointers.</u>

Note: Implementation for smart pointer is is given in `<memory>`

Sample Implementation:
```cpp   
class Entity{
     ...   
}

class ScopedPtr{
public:
    Entity* m_ptr;
    ScopedPtr(Entity* ptr): m_ptr(ptr){}
    ~ScopedPtr(){ delete m_ptr; }
}

// Reminder:
//Entity e; // on stack
//Entity* e = new Entity(); // on heap. Heap allocation returns a memory address

int main(){
    ScopedPtr e(new Entity); // explicit
    // ScopedPtr e = new Entity; // implicit
}

```
Here, `Entity` gets deleted automatically once it goes out of scope, even though it was declared on heap because <b>ScopedPtr was declared on stack.</b>
+ ### Unique Pointer
    + Scoped (once it goes out of scope it will be deleted)
    + Can't copy a unique pointer
        + If a unique pointer is copied, two pointer will point at the same block of memory, and then if one pointer dies, the other (copied) pointer will still point to the block of memory (that has been freed) eventually leading to a `segmentation fault`
    + Unique Pointer's copy constructor is set to delete.
    + Unique Pointer constructor is explicit (` = new Entity` will not work)
    
**Syntax:**
```cpp
std::unique_ptr<Entity> obj(new Entity);
// make_unique
std::unique_ptr<Entity> obj = std::make_unique<class>();
```
Make unique is used for `UniquePtr` to ensure exception safety. It's safer in the sense that if constructor happens to throw an exception, we would not have a dangling pointer with no reference.

The unique pointers can release the ownership by using `.release()`
```cpp    
std::unique_ptr<Animal> dog = std::make_unique<Animal>("Shadow");
Animal* dg = dog.release()
```
Check if pointer is empty: `!dog // true if .release() has had been called` 

Reassign to another pointer `dog.reset(new Animal("Smoky"));`. Note that `dog.reset() ~ dog = nullptr`

Reset can destroy the object, not delete. 

Move schemantics (`std::move`) can also be used to change the pointer. Note that if we move the pointer, the orignal pointer will be deleted. 

+ ### Shared Pointer
    + Can't share a `UniquePtr`, hence shared pointer.
    + Heavier than `UniquePtr`
    + Uses the concept of reference counting, i.e, how many reference to pointer exists, as soon as that reference count reaches 0, the pointer is deleted.
        +   | # of Shared Ptrs  | name                      | Reference Count |
            |-------------------|---------------------------|-----------------|
            | 1                 | sp1                       | 1               |
            | 2                 | sp2 (copied from sp1)     | 2               |
            |                   | del sp1                   | 1               |
            |                   | del sp2                   | 0               |
    + shared pointer can be compiler dependent.


**Syntax**
```cpp 
std::shared_ptr<Entity> shEnt(new Entity); // discouraged
std::shared_ptr<Entity> sharedEntity = std::make_shared<Entity>();
```
`new Entity` is avoided because shared pointer allocates another block of memory (`control block`) where  it stores that reference count, if `new Entity` is created and then passed to shared pointer constructor, then it's two allocation, create entity first and then the control block, it total two allocation(?). 

```cpp 
#include <iostream>
#include <memory>

class Entity
{
private:
    /* data */
public:
    Entity()
    {
        std::cout << "Created Entity" << std::endl;
    };
    ~Entity()hn
    {
        std::cout << "Destroyed Entity" << std::endl;
    }
};

int main()
{
    {
        std::shared_ptr<Entity> e0;// = std::make_shared<Entity>();
        {
            // std::unique_ptr<Entity> entity = new Entity(); will Not work since construvtor is explicit and there's no unique constructor.
            // std::unique_ptr<Entity> entity(); not preffered
            // USE THIS ONE: std::unique_ptr<Entity> entity = std::make_unique<Entity>(); // safer if constructo
            //std::unique_ptr<Entity> e1 = entity; // can't copy. when one dies, another dies as well.
            std::shared_ptr<Entity> sharedEntity = std::make_shared<Entity>();
            e0 = sharedEntity;
            // std::weak_ptr<Entity> weakEntity;
        }// sharedEntity dies, but e0 is still alive and holding a reference to sharedEntity
    }
}
```

+ ### Weak Pointer
    + When a `SharedPtr` is assigend to a `WeakPtr` it will not incerease thre reference count.
    + 


---
## Templates <a name="templates"></a>
Writing generic code. 

+ ### Templates
```cpp 
template<typename T>
T square(T x)
{
return x * x;
}

int i = square<int>(5); // int version
float f = square<float>(27.f) // float version
double d = square<double>(3.14) // double version
```

+ ### Templates and classes
Function definitions aren’t the only use case for templates, one can also automate
the generation of data types. These are known as class templates, since structs are
a special case of classes in C++

```cpp
template<typename T>
struct Pair {T a; T b;};
Pair<int> ip; // a pair of ints
Pair<float> fp; // a pair of floats
// Pair<int> is a data type, and can be used as such
Pair<Pair<int>> ipp; // pair of pair of ints
```
#### Non type template parameters:
There are non-type template parameters. These can also be used as compile-time constants:

```cpp
template<typename T, int N>
T* create_array(){
    T arr[N];
    return arr; 
}
```
Non type can't be float.


#### Structure of class templates
```cpp 
template <typename T> class Measurements {
public:
  Measurements(T val = 0); // :value(val) {} // default constructor
  T get_value();
  void setValue(T val);

private:
  T value;
};

template <typename T> Measurements<T>::Measurements(T val) : value(val) {}
template <typename T> T Measurements<T>::get_value() { return value; }
template <typename T> void Measurements<T>::setValue(T val) { value = val; }
```

Demostration of STL `Stack` container using class templates:
```cpp 
#include <iostream>

template <typename T> 
class Stack {
  int m_size, current;
  T *m_data; // = new T[m_size];

public:
  Stack(int size) : m_size(size) {
    m_data = new T[m_size];
    current = 0;
  }
  ~Stack() { delete[] m_data; }

  void push(const T &value);
  void pop();
  T top();
};

template <typename T> 
void Stack<T>::push(const T &value) {
  m_data[current] = value;
  current++;
}

template <typename T> 
void Stack<T>::pop() {
  if (current == 0) {

  } else {
    current--;
  }
}

template <typename T> 
T Stack<T>::top() { return m_data[current - 1]; }

int main() {
  Stack<int> s(4);
  s.push(10);
  s.push(20);
  s.push(30);
  s.pop();
  std::cout << s.top();
}
```
+ ### Template Template Prameters
**Template parameter itself is a class template**
One may also use templates themselves as arguments for other templates, so-called template template parameters. These can, e.g., be used to allow choosing between different implementations:
```cpp 

template<typename T>
class Sequential_Container{
    ...
}


template<typename KEY,
         typename VALUE,
         template<typename T> class Container_Type>
class SimpleHashTable{
public:
    void add(KEY k, VAL v);
    N get(KEY k);
private:
    Container_Type<KEY> keys;
    Container_Type<VAL> values;
    ...
}

int main(){
    ...
    SimpleHashTable<int, double, Sequential_Container>;
    ...
}


```

here the `Container_Type` is another class which takes the template T, for instance:


Perhaps the best example for template template parameter is the creation of 2D vector.
`std::vector<std::vector<int>> vec;`

> All three types of template parameters, i.e., types, non-type template parameters, and template template parameters, can have defaults, just like function arguments:
```cpp
template<typename KEY,
         typename VALUE,
         template<typename T> class Container_Type = Sequential_Container>
```
+ ### Template Specilization (explicit, partial, implicit)
Sometimes special cases are special enough to break the rules ;)
In essence, some special cases are suposed to be treated differently.

#### Full Specialization: 
```cpp 
template<> // empty brackets
class Stack<std::string> 
// specialization is placed after the class name in angular brackets.
```
In this ^ example, std::string will replace any `type` parameter `T` (duh!)

If we're to define a function outside the class:
```cpp 
std::string Stack<std::string>::top(){ // no template line before it
    ...
}
```

#### Partial Specialization:
If we have more than one type parameters, we may not choose to fix all of them, this is called Partial Specialization.

Sample implementation of STL Pair class with enhancments using template specializations.

```cpp 
#include <iostream>
#include <string>
#include <vector>

template <typename T, typename U> 
class Pair {
  T t;
  U u;

public:
  Pair() : t(), u() {} // construct with default values for a and b;
  Pair(const T &tt, const U &uu) : t(tt), u(uu) {}
  T first() { return t; }
  U second() { return u; }
};

// Partial Specilization with first args as string
// (Say storing key and value)
template<typename U>
class Pair<std::string, U>{
    std::string str;
    U u; 
public:
      Pair() : str(), u() {}
      Pair(const std::string& str, const U& uu):str(str), u(uu){}
      std::string first() {return str;}
      U second() {return u;}
};

// Both template paramters to be of the same type
template <typename T>
class Pair<T, T>{ // only one template param but pair is using that two times
    T tt, uu;
    public:
    Pair(): tt(), uu() {}
    Pair(const T& tt, const T& uu): tt(tt), uu(uu){}
    T first(){return tt;}
    T second(){return uu;}
};

// Specialization with pointers as first type
template<typename T, typename U>
class Pair<T*, U>{
    T* a;
    U b;
public:
    Pair(): a(), b() {}
    Pair(const T& aa, const U& bb){}

    T* first() {return a;};
    U second() {return b;};
};

int main(){
    Pair<int, double> p(12, 21.44);
    // Pair<int, int> pp();
    std::cout << p.first();

    Pair<std::string, double> dict("test", 21.22);
    std::vector<Pair<std::string, double>> dictonary;
    dictonary.emplace_back("Tesla", 100);
}
```

#### Template Specialization for Functions
Template functions can be specalized in the same way as template classes, however, the instantiation can be complicated by overloading an argument deduction (full specialization uses same syntax as angular brackets, but in this case the compiler can use the arguments of the function to determine template parameter types).

Specialization in function template don't take part in overload resolution, only base templates are considered.

```cpp 
template <typename T> 
T max(T t, T u) { 
    return (t > u) ? t : u ;
}
// specialization for int
template<>
int max(int t, int u){
    return (t > u) ? t : u ;
}
//specialization for int pointer
template<>
int* max(int* t, int* u){
    return (*t > *u) ? t : u ;
}

```
For historical reason, function templates cant't be partially specialized but we can almost achive the same effect by overloading a template. 

__
Indivudial member function can be specialized (if required) instead of the entire class - leaving other member functions in their generic form. `template<> int Stack<int>::top() { ... } ` .


```cpp 
// 1. Base template: General case
template<typename U, typename V=U>
struct Pair{};

// 2. Partial Specialization: U=V
template<typename U>
struct Pair<U, U>{};

// 3. Partial Specilization: pointers
template<typename U, typename V>
struct Pair<U*, V*>{};

// 4. Full Specialization: int pointers
template<>
struct Pair<int*, int*>{};

Pair<int*, int*> -> 4
Pair<int*> -> 4 (via 1)
Pair<int, int> -> 2
Pair<int> -> 2
Pair<int*, double*> -> 4

Pair<double*, double*> -> both 2 and 3 (ambigious)
```
Overlapping specialization are to be avoided as they cause compiler error when triggred.

#### Explicit Instantiation
The way in which templates are processed means that they will be instantiated as necessary, but sometimes, we might want to forcefully instantiate a template, this is called explicit instatiation. 
This can be done for both function and class templates by using using `explicit instantiation directive`.

```cpp 
template<typename T>
T max(T a, T b){
    ...
}

// force instantiation of max template. 
template double max<double>(double a, double b)
// it will be created even without being used anywhere.

// SIMILARY for class
template class Stack<int>;

// or instantiate just a class member function
template void Stack<double>::pop();
// this leaves the rest of the class as generic.
```

Usecase: 
1. reduce compile time (Say if we know that Stack<int> will be used a lot we can instantiate in one translation unit and then refer to it with extern in others). The linker will pick it up as a normal external variable.
```cpp
#include "Stack.h"

    extern template class Stack<int>
    void func(){
        Stack<int> s(10);
    }
```
2. Creating library using template types. The template definition that hasn't been instantiated at all will not be included in the final build. By using explicit instantiation we can make sure that they will be includede.


Tl;dr -> forcefully create templates.

+ ### Templates and Inheritance
Inheritance pretty much works the same way as it does with normal classes.
```cpp 
template<typename T, int size=10>
class Array{
    T value[size];
};

// can inherit from the Array class
template<typename T>
class NewArray : public Array<T>{
 // NewArray has to be declared as a template type because the 
 // base class needs a type parameter
};


// We'd use it in the way we expect, providing the type in angle brackets: <>
NewArray<int> new_a;
```

**Inheriting from a specialization of base class**
The base class in this example is fully specified and has a size of 10 (default argument).
```cpp  
class IntArray: public Array<int>{
    // This is not a template type, 
    // since it doesn't have to provide the template param T to base class. 
};

template<int SIZE>
class IntArrayVariableSize : public Array<int, SIZE>{

}

// can do something similar if we want have a constant type but want the type to change.
```

Inheritance often has *protected members*. Templates can make it complicated to asscess those protected variable from derived classes. 

If a name appears in a class but no namespace precedes it (an unqualified
name), then the compiler will look in the following order for a definition:
1. Definitions in the class
2. Definitions in independent base classes
3. Template arguments

Accssing `Base` classe's variable works fine as long as dervied class is also not templatised.
```cpp 
// Works as expected since Derived accesss a specilization of Base
// and is itself not a template
template <typename T> 
class Base {
protected:
  T prot;

public:
  Base() : prot() {} 
};

class Derived : public Base<int> {
public:
  void print() { std::cout << prot << std::endl; }
};
```
However, if the derived class itself is also a template, then it can't access the protected members.
```cpp 
// THROWS ERROR: use of undeclared variable prot
template<typename T>
class Derived : public Base<T> {
public:
  void print() { std::cout << prot << std::endl; } 
};
```
Why does it happen?
    Types of type parameter and values of non type paramteres aren't known at the time when template is defined, but what some constructs mean may depedn on those types and values. This leads to the idea of dependent and non-dependednt names. 
    
When something is dependent (cannot be looked up during template definition), lookup is postponed until instantiation. This works by differnt rules, and one of these rules says that the unqualified names do not get resolved as the member of the Base class, when we're talking about the dependent types, and as a result it needs to be qualified using any of these three techniques: 
```cpp 
Base::prot
this->prot
using Base<T>::prot
```

+ ### Template Metaprogramming

Using properties of templates to manupulate/calcuate at compile time.
It was discovered during the standardization of C++ when it was found that C++ template mechanism was turing complete (template can be used to compute anything that was computable - atleast in theory). First example by Erwin Uruh (1994) who computed the prime numbers with compiler error messages. 

+ ##### Caveats:

    + Dosen't allow mutable state: no valruable or counted loops 
    + Recursion and Recursive template generation
    + Kinda like functional programming.
    + Caculation of constant constants, generation of code fragments, creation of custom types.
    + Minimum runtime overhead, but long build times.
    + Compact and efficient code, hard to debug and understand

```cpp 
template<int N>
struct Factorial{
    enum { value = N * Factorial<N-1>; }
}

template <>
struct Factorial<0>{
    enum { value = 1; }
}
```
Same example without `enum`
```cpp
template<int N, typename T = int>
struct Fact{
    static constexpr T val = N*Fact<N-1>::val;

};

template<typename T>
struct Fact<0, T>{
    static constexpr T val = 1;
};

std::cout << Fact<10>::val;

```
    
+ ### Overloading Templates
Just like overloading functions, but rules are slightly different. 
```cpp 
#include <cstring>
#include <iostream>

template <typename T>
const T &max(const T &a, const T &b) {
  std::cout << "Plain Template" << std::endl;
  return (a > b) ? a : b;
}
// what if i want to compare 3 types
template <typename T> 
const T &max(const T &a, const T &b, const T &c) {
  std::cout << "Plain Template" << std::endl;
  const T &tmp = (a > b) ? a : b;
  return (c > tmp) ? c : tmp;
}
```

If i want to compare pointers, the current implementation will compare addresses in pointer variable, but we want to compare values! Therefore we add:

```cpp
template<typename T>
const T &max(const T* &a, const T* &b, const T* &c) {
    const T* tmp = (*a > *b) ? a : b;
    return (*c > *tmp) ? c : tmp;
}

const char* max(const char* a, const char* b){
    std::cout << "String" << std::endl;
    return (std::strcmp(a,b) > 0 ) ? a : b;
} // this will be called with max("abcd", "ab")

```

Note: Template resolution is very particular about types. In the above example, it NEEDS a const pointer, and will not work for non-const pointer.


Compiler will prefer non template version if avilable rather than instatiating the template.

Type conversion is **not** used in the template paramters
+ ### type_traits
    Common problem with templates is that only certain types might be valid for the template codes that has been written (can't compare string with the code written for int/double/float etc). type_traits are a better way to check type compatibility.
    
type_traits are a way to get information about types so that we can make decisions based on type capability.

Eg: check if the type parameter is a char.
```cpp 
// Simple implementation
// start with a struct with a single boolean value
// by default initialized to false.
template<typename T>
struct is_char{
    static const bool value = false;
};

template<>
struct is_char<char>{
    static const bool value = true;
};

template<typename T>
void foo(T val){
    if(is_char<T>::value){
        // char
    }else{
        // not a char
    }
}

int main(){
    foo(10); // not a char
    foo('c'); // char
}
```
C++11 has defined a number of type traits header that contains a number of useful traits that we can use to check types and capabilities.

```cpp 
#include <type_traits>

template <typename T>
class Test{
    T value;
public:
    Test(T value) : value(value){
        static_assert(std::is_integral<T>::value); // type trait to check int
    }
};

int main(){
    Test<int> t1(10); // no error
    Test<double> t2(0.5); // assertion failed
}

```

    
+ ### SFINAE
Subsitution failure is not an error.
Subsitution failure *generally* happens while choosing the template and is not an error. Failing to instantiate one of the specializations doesn’t terminate the compilation process, that happens only when <u>the pool of possible choices has been exhausted and no viable specialization was found, or several that are equally suitable</u>.

How it works:
1. A traits class checks for the existance of a method.
2. `enable_if` defines a type based on the return value of the traits class.
3. Right function is then picked up by SFINAE.

SINAFE provides a mechanism to select b/w different template specializations at will and is achived by triggring substitution failure on purpose. This is done by using `enable_if`

Example with `enable_if`
```cpp 
template<typename T, typename = std::enable_if_t<std::is_integral<T>::value>>
T function(T a, T b){
    return a+b;
}

int main(){
    auto a = function<int>(1,2); // works
    // ERROR: error: no matching function for call to ‘function<float>(int, int)’
    auto b = function<float>(1,2);  // doesn't work.
    std::cout <<a;
}

```
It can also be displaced as a function argument (so that it also works for other types.)

```cpp 
template<typename T>//, typename = 
bool Equals(T lhs, T rhs, std::enable_if_t<std::is_floating_point<T>::value>* = nullptr){
    return lhs == rhs;
}

template <typename T> 
bool Equals(T lhs, T rhs, std::enable_if_t<!std::is_floating_point<T>::value>* = nullptr){
    // handles imprecision
    return true;
}

int main(){
    Equals(1,2);
}
```
Even though at the end they both end up giving us void pointers, they are not the same - the structure is diffenrent. The signature of `std::enable_if_t<std::is_floating_point<T>::value>* = nullptr` is different than `std::enable_if_t<!std::is_floating_point<T>::value>*` in the same sense as how `vector<int>` is different from `vector<float>`.

```cpp 
// this function is enabled if T is floating point
template<typename T>
std::enable_if_t<std::is_floating_point<T>::value, bool> Equals(T lhs, T rhs){
    return lhs == rhs;
}

// this function is enabled if T is NOT floating point
template <typename T> 
std::enable_if_t<!std::is_floating_point<T>::value, bool> Equals(T lhs, T rhs){
    // handles imprecision
    return true;
}

int main(){
    Equals(1,2);
    Equals(1.2, 2.2);
}
```
Bool given as return type in `std::enable_if<..., bool>` because the return type of the function is not void.


```cpp
#include <cmath>
#include <iostream>
#include <type_traits>


template<typename T, typename = std::enable_if<std::is_integral<T>::value>>
T function(T a, T b){
    return a+b;
}

int main(){
    auto a = function(1.1f,2.2f);
    std::cout <<a;
}
```

Pratical Example:
For solving Linear System of equations we need to pick up a solver. Some classes have methods like `hasMultiplyByInverse` which solves the system efficiently and in specalized manner. We need to do some compile time inspection to check if this method exists.
First define a traits class:
```cpp 
T1: Inverse matrix.
template<typename T1, typename T2>
struct hasMultiplyWithInverse{
    template<typename T, typename U = void>
    struct Helper { enum {value = false }; }
   
   template<typename T, typename U = void>
   // &T::multiplyWithInverse: checks for the existance of 
   // multiplyWithInverse inside T.
    struct Helper<T, decltype(&T::multiplyWithInverse)> { 
        enum {value = True }; 
    }
    
    enum { value = Helper<T1, void (T1::*)(T2&) const>::value};
    // * is a pointer to T1 that takes T2 and returns a void(?)
}
...
...
...

template<typename M, typename V>
typename std::enable_if<hasMultiplyWithInverse<M,V>::value>::type
solve(const M& m, V& v) {
// implement specialized version here, can use multiplyWithInverse
}
template<typename M, typename V>
typename std::enable_if<!hasMultiplyWithInverse<M,V>::value>::type
solve(const M& m, V& v) {
// implement general version here, has to avoid multiplyWithInverse
}


```

+ ### Variadic Templates
Other function used with variables number of arguments: `printf`
compiler knows whwat types are being used at compile time, so we should be able to make use of that information. 
create fn with varaible args, with arg handling klogic at compile time.
Used in Tuple.


```cpp 
template<typename... Args>
void func(Args... args){
    ...
}

// This expands to
template<typename T1, typename T2, typename T3>
void func(T1 arg1, T2 arg2, T3 arg3){
    ...
}
```
Template parameter pack: `typename...`: list of arbitary types
Function paramter pack `Args...` (arguments type matches the name of the  template parameter pack)

Template arguments are unpacked by recursion (not really recursion since number of arguments differ each time). 

- Define a recursive template funciton with a special case to end recusion.

```cpp
template<typename T>
T add(T val){
    return val;
}

template<typename T, typename ...Args>
T add(T val, Args... args){
    return val + add(args...);  
}


int main(){
    int i = add<int>(1,2,3,3,4,5,5,6,67,3,3,3,3,2,3,1,21,1,2,21,1,1,2,21,12,1,1);
    std::cout << i << std::endl;
}
```
in `return val + add(args...);` one argument unpacks as value, and the rest are sent as parameter pack.

`empalce_back` implementation
```cpp 
struct Pair {
  int x, y;

public:
  Pair(int x, int y) : x(x), y(y) {}
};

// arbitary number of args. 
// compiler will look for the constructor having sepecified
// number of args
template <typename T, typename... Args> T *empbk(Args... arg) {
  return new T(arg...);
}

int main() {
  std::vector<Pair> vec;
  vec.push_back(Pair(1, 2));
  auto a = empbk<Pair>(5, 5);
  std::cout << a->y;
  auto a = empbk<Pair>(5, 5, 5); // give an error, no constructor for the args
}
```



+ ### Template argument deduction
```cpp 
template<typename T>
function(T a){
    ...
}

function(5) // template will deduce the type by the argument as int.
function(5.2f) // template will deduce the type by the argument as float.
```

---
## Polymorphism <a name="polymorphism"></a>
Polymorphism: Ability of a object/fn/operator to be displayed in more than one form.


![](https://i.imgur.com/NtCqyyD.jpg)



`Base* obj = new Derived();`
When derived class object is made, Base class constructor is called first. The derived class object contains the base class obj, this allows it to call base cass function (and not the other way around).

Consider,
```cpp
Parent:  Animal
Derived: Dog, cat etc.

void doSomething(Animal* animal);
```
If it was not allowed to assign a base class object to parent reference variable, it would have been required to create seprate functions for Dog and Cat. `void doSomething(Dog* dg); ...`

**With polymorphism we can use:**
```cpp 
void doSomething(Base* b){
    ...
}

Base* b1 = new Child1();
Base* b2 = new Child2();

doSomething(b1);
doSomething(b2);
```
In other words, Inheritance defines an `IS-A` relationship. So we can say, derived class is a base class (or Dog is an Animal), then *every derived object can be treated as a Base (because it quite literally IS-A base)*, and hence `Base* b = new Derived();`. 
Dereferring b allows acess to the base part of Derived(?).


#### More Specifically<a name="morespecific"></a>
The part that creates inheritance is `new Derived()`. LHS has nothing to do with creating instance(?) as long as `IS-A` relationship remains intact.

```
Enemy og = new Ogre();
           ----------
               ^--- This part determines what can be accessed from the object.
```

**Tl;dr**
```
Base* poly = new Derived();

```
poly is treated as a `Base` pointer but it is [actually a pointer to the `Derived` (pointing to the derived)](#morespecific) [Read section: more specificly]

Hence we are creating a `Derived` instance and assigingn it to a `Base` type. 

+ ### Static
    + If there's parameter difference, overloading will decide the function.
    + 
+ ### Dynamic
    + Function Overriding (if derrived class defines same function as defined in its base class, it is known as function overriding)
    + With dynamic polymorphism, if an object of derived class calls a member function which exists in both classes (derived and base), the member function of derived class is invoked and that of base class is ignored.
    + Enables to provide specific implementation of the function which is already provided by the base class.
    + Until `virutal` functions are included there is no dynamic polymorphism.
    Example:
    ```cpp 
    class Animal {
    public:
      virtual std::string sound() = 0;
    };

    class Cat : public Animal {
    public:
      std::string sound() override { return "Meow"; }
    };

    class Dog : public Animal {
    public:
      std::string sound() override { return "Bark"; }
    };

    class Tiger : public Animal {
    public:
      std::string sound() override { return "Roar"; }
    };

    class Pikachu : public Animal {
    public:
      std::string sound() override { return "Pika"; }
    };

    int main(){
        std::vector<Animal*> creatures;

        creatures.push_back(new Dog());
        creatures.push_back(new Tiger());
        creatures.push_back(new Cat());
        creatures.push_back(new Pikachu());

        for(auto& creature: creatures){
            std::cout << creature->sound() << std::endl;
        }
    }

    OUTPUT:
    Bark
    Roar
    Meow
    Pika
    ```
    + implementation done by vtables (using Pointer to Member ).
    ```
    Common Error: undefined reference to `vtable for Animal'
    ```
    + virtual functions -> Dynamic dispatch, implemented by vtables.
    + More on vtables: 
        + Maps all virtual function to base class so that they can actually be mapped to the current overridden function at runtime.
        + This is done by including a member poitner in the actual base class that pointes to the vtables.
        + virtual is complemented by override (not required but provides improved readability and is implementation safe)
        + override will throw an error if we try to override a function which is not marked as virtual.
    + Run time costs:
        + Additional memory for vtables
        + everytime we go through the vtables, we have to determine which function to map to, which also contributes in performace overhead.
    + (?) Virtual Destructors: Can cause memory leak if the destructor in the parent class is not marked as virtual. Since we're not overwrindg the destrictor just adding it (kindof) (?). Just the  base class constructor is called and not the derived constructor as c++ doesn't know that theremight be another method.

+ ### Interface (Pure virutal function)
    Define a function in the base class which does not have an implementation and eforces subclass to make the function. 
```cpp 
virtual void getName = 0;
```
`getName` has to be implemented somewhere in order for us to have an instance of this class.
```cpp 
class Entity {
public:
  virtual std::string getname() { return "Entity"; }
};

class Player : public Entity {
private:
  std::string m_name;

public:
  Player(const std::string &name) : m_name(name) {}
  std::string getname() override { return m_name; }
};

void PrintEntity(Entity *ent) {
  // want c++ to know that entity passed here is a player and ask to call the
  // respective function
  std::cout << ent->getname() << std::endl;
}

int main() {

  // Start referring to player as if it's an Entity
  Entity *e = new Entity();
  PrintEntity(e);
  Player *p = new Player("Test");
  PrintEntity(p);
  Entity *ent = new Player("ALpha");
  PrintEntity(ent);
}
```



+ ### Abstract Base Class
Class that only consits of Interfaces (as a template of sorts).

---
## Threads <a name="thread"></a>
C++ had thread suppport before C\++11, of course, but the availability and characteristics of these threads where dependent on the architecture and operating system, e.g., POSIX threads (pthreads) under UNIX and Linux. C++11 provides a unified interface to thread creation and management, thereby increasing interoperability and platform independence of the resulting code.

There are two different ways of writing such concurrent programs:
    1. low-level code based on threads, using mutexes and locks to manually manage thread interactions and data exchange
    2. higher-level code based on tasks, using futures and promises to abstract away most of the interdependencies


+ ### std::thread
Syntax: `std::thread t1(function_value, args ...)` function can be *any* callable object (`lambda, functor, function pointer` etc.)
`t1.detach()` will run freely on it's own (daemon process) 

Once a child is detached, it'll not join back. 
Check if thread can be joined: `t1.joinable()`. The program will crash if trying to join a non-joinable thread.
```cpp 
#include <iostream>
#include <thread>


void foo(){
    std::cout << "Hello world" << std::endl;
}

int main(){
    std::thread t1(foo);
    // t1.join();
    t1.detach(); // main thread will not wait for t1 to come
    // t1.join(); // error
    if(t1.joinable()){
        t1.join();
    }
}
```
If t1 is destroyed before the thread is joined then the program will terminate. Have to make a call weather to detach or join thread beofre it goes out of scope. Put Parent thread in RAII to make sure that the child thread joins. 


**Passing by Reference & Moving**: 
To pass varaible by reference, use reference wrapper: `std::ref(var)`
Instead of passing by reference, try moving the value (will require function to have Rvalue reference).

Threads can also be moved: `std::thread t3 = std::move(t2);` (A thread cannot be copied, if ownership needs to be transferred, the only way is std::move).

Thread ID: `t1.get_id()`
Max Threads: `std::thread::hardware_concurrency()`
```cpp 
#include <iostream>
#include <thread>

void func() { std::cout << "Hello World"; }

// Functor
class Funct {
public:
  void operator()(int i) {
    for (int i = 0; i >= -100; i--) {
      std::cout << "from t1: " << i << std::endl;
    }
  }
};

class ReferenceTest {
public:
  void operator()(std::string& msg) {
    // std::this_thread.get_id();
    std::cout << " Message is: " << msg   << std::endl;
    msg = "This message is changed inside the fucntion";
  }
};

int main() {
  Funct f1;
  
  //   std::thread t1(f1, 0);
  std::string s = "Hello boy!"; // need to pass by reference
  std::thread t2(ReferenceTest(), std::ref(s)); // change operator() to ravlaue reference and use std::move
  std::thread t3 = std::move(t2);
  t3.join();
  std::cout << std::thread::hardware_concurrency() << s << std::endl;
}
```

+ ### mutex and lock
#### Race Condition: Output of the program dependeson the relative execution order of one or more threads

Mutex: mutex is a synchronization primitive - a mechanism that enforces limits on access to a resource when there are many threads of execution

Tl;dr: `Mutex is used to sync the access of common resource`.

`mu.lock()` is not used because exception safety. `std::lock_guard` ensures release by RAII.
Syntax: 
`mu.lock(); ... mu.unlock()`
`std::lock_guard<std::mutex> guard(mu); // mu is mutex`
```cpp 
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mu;

void shared_print(std::string msg, int id){
    std::lock_guard<std::mutex> guard(mu);
    // mu.lock();
    std::cout << msg << id << std::endl; // only one thread should print at a time.
    // mu.unlock();
}

void function1(){
    for (int i = 0; i>-100; i--){
        // std::cout << "from t1: " << i << std::endl;
        shared_print(std::string("from t1: "), i);
     }
}

int main(){
    std::thread t1(function1);
    for (int i = 0; i < 100; i++){
        // std::cout << "Main: " << i << std::endl;
        shared_print(std::string("main: "), i);
    }

    t1.join();
}
```
**IMPORTANT:** all shared variables need to be encapsulated completely by mutex so that they are not acessible from outside the lock guard.

1. Don't return the mutex variable
2. Dont pass f as an argument to user defined functions as theymight use f without mutex.
3. Ensure thread safetly by function design.


+ ### std::unique_lock
    + Third way to lock a mutex (apart from `.lock()`, and `lock_guard`)
    + Similar to lock_guard but can be unlocked when sync part is over. 
    + Useful for fine-grained locking
    + `std::defer_lock` is used to create locker for the mutex and lock it later.
    + defer_lock combinded with unique_lock can unlock/lock number of times.
    + felxibility comes with a price.
    + lock_guard is faster.


+ ### Condition Variables
    + notifies the other waiting thread that it is done executing its own part.
    + `std::condition_variable cond;` , `cond.notify_one()`, `cond.wait(locker)` (The locker is a mutex variable  - used so that thread is not sleeping with the metex lock. This will unlock it first(?)).
    + Spurious wake: thread will wake up on its own. An extra condition is given to check if the thread is expected to go back to sleep or start execution: `cond.wait(locker,[](){return !queue.empty()})`. if thread wakes up and finds out that the queue is empty, it'll go back to sleep again, otherwise it'll start executing.

+ ### future and promise
`std::async`: a function that returns future. Future represents an object with which we can get something in the future.

```cpp 
// CODE too complex.

#include <condition_variable>
#include <future>
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mu;
std::condition_variable
    cond; // want to make sure that x = result in child thread happens first
          // before parent thread acts upon the variable x.

void factorial(int N, int &x) {
  int result = 1;
  for (size_t i = N; i > 0; i--) {
    result *= i;
  }
  std::lock_guard<std::mutex> lock(mu);
  cond.wait(lock);
  x = result;

  // std::cout << "Factorial: " << result << std::endl; // RETURN the result
  // instead of printing.
}

int main() {
  int x; // since x is a shared variable between the two threads, it needs to be
         // proctected by some mutex
  std::thread t1(factorial, 5, std::ref(x));
  cond.notify_one();

  t1.join();
  std::cout << x << std::endl;
}
```

Standard library provides an easier way to do this job, std::async. std::async is a function that returns future. 
```cpp
std::future<int> fu = std::async(factorial, 5);
```

Future is the channel from which we can get result from the child thread later on. `fu.get()` will wait until the child  finishes. can be called only once.
` x = fu.get();`

 Async may or may not create another thread. and that can be controlled by
another parameter 
```cpp
std::async(std::launch::deferred, factorial, 5);
```
`async` will not create the thread and will defer the execution of the function until it comes across `fu.get()`. IN THE SAME THREAD(?).

`std::async(std::launch::async, factorial, 5)` creates another thread.

Default: `std::async(std::launch::async | std::launch::deferred)` creation of thread depends on implemetation.

```cpp 
// function doesn't need a second parameter but returns a vlaue.
int factorial(int N) { 
  int result = 1;
  for (size_t i = N; i > 0; i--) {
    result *= i;
  }
  return result;
}

int main() {
  int x;
  // Standard library provides an easier way to do this job, std::async.
  // std::async is a function that returns future
  std::future<int> fu = std::async(factorial, 5);

  x = fu.get(); 
  std::cout << x << std::endl;
```

Promise:
Promise to send the value in future. 
```cpp 
int factorial(std::future<int> &f) { // takes future
  int result = 1;
  int N = f.get(); // Once value is recieved, it'll start the execution
  for (size_t i = N; i > 0; i--) {
    result *= i;
  }
  return result;
}

int main() {
  int x;
  std::promise<int> p;
  std::future<int> f = p.get_future();
  std::future<int> fu = std::async(std::launch::async, factorial, std::ref(f));

  std::this_thread::sleep_for(std::chrono::milliseconds(1200));
  std::cout << "Setting Value to 5..." << std::endl;
  p.set_value(5);
  std::cout << "Sleeping..." << std::endl;
  std::this_thread::sleep_for(std::chrono::milliseconds(1020));
  std::cout << "Executing seprate thread" << std::endl;
  x = fu.get();
  
  std::cout << x << std::endl;
}

```

+ ### Packaged Tasks (?)
Package task and can be passed around to different function/obj/threads.
`std::package_task <int<int>> t(func)` 

`t(6)` can be executed in a different context other than the palce where it is created.
```cpp 
int main(){
    std::packaged_task<int(int)> t(factorial);
    // t(5); // can be used in a different context.
    // To get return value, convert to future.
    int x = t.get_future().get();
    return 0;
}
```

**3 ways to get future**
1. async returns a future.
2. promise::get_future();
3. package_task::get_future();


+ ### deadlock

+ ### atomic
An alternative to mutexes and locks is the use of atomics. Data types can be made atomic by wrapping them in a std::atomic<T> , which provides special uninterruptible methods for the usual operations. This solves the lost update problem, because read—modify—write cycles are carried out as single operations 

Atomic value allows to perform an operation on one particular thread ensureing thread safety(?). Doesn't require any thread to be blocked(?). No deadlocks(?)
```cpp
std::atomic<long> varname(...)
varname.load();
```




---
## Misc <a name="misc"></a>
   + ### a. Using
     using provides an alternative to typedefs, which is more general and can also be used to give names to partial template specializations / instantiations.
     ```cpp
     using Number = int; // replaces ``typedef int Number''
     
     // partial specialization or instantiation
     template<typename T>
     using Vector3D = Vector<T,3>; // defines ``Vector3D<T>'
     
     // alias template
     template<typename U, typename V>
     using Matrix = Long::Namespace::SpecialMatrix<U,V>;
     
     // variadic alias template
     // (can also be used to just omit the arguments!)
     template<typename... T>
     using Foo = Bar<T...>; // Foo is alias of Bar     

     ```
    
  + ### typedef
      Make alias `typedef int Number` then, `Number a = 5`
  + ### exception free function
     + C++11 switched to specifying that a function will never throw exceptions, used for optimization purposes. There are two versions:
         + A simple noexcept qualifier, stating that exceptions are never thrown
         + A noexcept qualifier with Boolean argument, typically using an operator
        ```cpp
        // never throws an exception
        int five() noexcept {return 5;}
        ```
   + ### random
       + PRNGs:
          • The Mersenne Twister (Matsumoto and Nishimura)
          • “Minimal standard” linear congrual engine (Park et al.)
          • RANLUX generator (Luscher and James)  etc
       + The generation of random numbers is divided into three distinct steps:
           + Seeding the aforementioned engines, using true random numbers (entropy) or simply system time if the latter is sufficient
         + Generation of uniformly distributed pseudo-random integers using the engines
         + Transformation of these values into discrete or continuous target distributions
         
       ```cpp
        std::random_device rd; // entropy source
        std::mt19937 gen{rd()}; // seed Mersenne Twister
        std::normal_distribution<> dist{}; // standard normal dist
        std::vector<double> vals(1000);
        for (auto& e : vals)
        e = dist(gen); // draw value using generator
       ```
with the same name
    ### c. namespaces
    ### d. trailing return type
    ### e. different ways of initialization in C++
    ### singleton pattern
    ### fold expression
    ### one definition rule
    
  + ### extern
  ```cpp
    #ifndef HEADER_H
    #define HEADER_H

    // any source file that includes this will be able to use "global_x"
    extern int global_x;
  ```
  + ### default and delete, explicit
      + #### default
        + Explicitly defaulted function declaration is a new form of function declaration that is introduced into the C++11 standard which allows you to append the ‘=default;’ specifier to the end of a function declaration to declare that function as an explicitly defaulted function. This makes the compiler generate the default implementations for explicitly defaulted functions, which are more efficient than manually programmed function implementations.
        + For example, whenever we declare a parameterized constructor, the compiler won’t create a default constructor. In such a case, we can use the default specifier in order to create a default one.
             ```cpp
            class A {
            public:

                // parameterized constructor
                A(int x)  {
                    cout << "This is a parameterized constructor";
                }

                // Using the default specifier to instruct the compiler to create
                 the default implementation of the constructor.
                A() = default; 
            };
            ```
      + #### delete
          + To disable the usage of a member function. This is done by appending the =delete; specifier to the end of that function declaration.
          + Any member function whose usage has been disabled by using the `=delete` specifier is known as an expicitly deleted function.
          + Disabling undesirable argument conversion
          Delete can be used on any function.
          ```cpp
          setVal(int a){
              val = a;
          }
          setVal(float) = delete; // will not compile if float.
          ```
      + #### explicit
          Suppose, you have a class `String`:
        ```cpp
        class String {
        public:
            String(int n); // allocate n bytes to the String object
            String(const char *p); // initializes object with char *p
        };
        ```
        Now, if you try: `String mystring = 'x';`

        The character `'x'` will be implicitly converted to `int` and then the `String(int)` constructor will be called. But, this is not what the user might have intended. So, to prevent such conditions, we shall define the constructor as `explicit`:

        ```cpp 
        class String {
        public:
            explicit String (int n); //allocate n bytes
            String(const char *p); // initialize sobject with string p
        };
        ```
  + ### Range based loop over intilizer lists.
      ```cpp
    int main(){
        for (const auto& i : {1,2,3,4,5,6}){
            std::cout << i << ", ";
        }
    }
      ```
