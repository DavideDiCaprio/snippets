#include <array>      
#include <vector>      
#include <list>        
#include <stack>        
#include <set>          
#include <map>         
#include <tuple>        


// Array
int array[5] = {1, 2, 3, 4, 5}; 

// Vector (dynamic array)
std::vector<int> vec = {1, 2, 3, 4, 5};

// List (doubly linked list)
std::list<int> list = {1, 2, 3, 4, 5};

// Stack
std::stack<int> stack;
stack.push(1);
stack.push(2);

// Queue
std::queue<int> queue; 
queue.push(1);
queue.push(2);

// Set
std::set<int> set = {5, 2, 3, 1, 4};  

// Map (key-value)
std::map<std::string, int> map = {{"one", 1}, {"two", 2}, {"three", 3}};

// Tuple
std::tuple<int, double, std::string> tuple = {1, 2.5, "three"};