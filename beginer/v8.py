int Nth_of_AP(int a, int d, int N) 
{  
    
    // Nth term t(n) = a(1) + (n-1)*d 
    return (a + (N - 1) * d); 
      
} 
  

int main()  
{ 
    // starting number 
    int a = 2;  
      
   
    int d = 1;  
      
    // N th term to be find 
    int N = 5;  
      
   
    cout << "The "<< N  
         <<"th term of the series is : "
         << Nth_of_AP(a,d,N); 
  
    return 0; 
} 
