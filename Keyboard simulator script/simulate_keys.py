from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

myString = '''
#include<iostream> 
using namespace std; 

int maxSubArraySum(int a[], int size) 
{ 
int max_so_far = a[0]; 
int curr_max = a[0]; 

for (int i = 1; i < size; i++) 
{ 
		curr_max = max(a[i], curr_max+a[i]); 
		max_so_far = max(max_so_far, curr_max); 
} 
return max_so_far; 
} 

/* Driver program to test maxSubArraySum */
int main() 
{ 
int a[] = {-2, -3, 4, -1, -2, 1, 5, -3}; 
int n = sizeof(a)/sizeof(a[0]); 
int max_sum = maxSubArraySum(a, n); 
cout << "Maximum contiguous sum is " << max_sum; 
return 0; 
} 
'''
time.sleep(2)
# keyboard.type(myString)

for s in myString:

    if s=='\n' :
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    elif s=='\t': #we don't need to do anything as ide already provides tab
        # keyboard.press(Key.tab)
        # keyboard.release(Key.tab)
        pass
    
    else:
        keyboard.press(s)
        keyboard.release(s)
    
    time.sleep(0.08)

#there might be extra }}} just remove them
