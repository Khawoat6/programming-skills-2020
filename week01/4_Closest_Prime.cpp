#include <iostream>
#include <stdlib.h>
using namespace std;


bool prime (int a)
{
    int counter=0;
        for(int i=2; i<=a/2; i++)
    if (a%i==0) 
        counter++;
    
    if (counter==0) 
        return true;
    else
        return false;
}

int main() 
{
    int num, n,p;
    cin>>num; 
    
    for (p=num; !prime(p);p--);
        
    for (n=num; !prime(n);n++);
    
    if(abs(p-num) < abs(n-num))
        cout<<abs(p-num);
    else if (num == 1)
        cout << "1";
    else
        cout<<abs(n-num);


}

