using namespace std; 
  
void Nminelements(vector<int>list1, int N) 
{ 
    vector<int> final_list; 
    int n = list1.size(); 
    for (int i = 0; i < N; i++)  
    { 
        int min1 = 9999999; 
        for (int j = 0; j < n; j++) 
        { 
            if (list1[j] < min1) 
                min1 = list1[j]; 
        } 
          
       
        // from list so that it do 
        // not come in calculation again          
        list1.erase(remove(list1.begin(),  
                           list1.end(), min1),  
                           list1.end()); 
        final_list.push_back(min1); 
    } 
    for(int i = 0; i < final_list.size(); i++) 
    cout << final_list[i] << " "; 
}  
int main() 
{ 
    vector<int> list1 = {4, 78, 34, 10,  
                         8, 21, 11, 231}; 
    int N = 2; 
    Nminelements(list1, N); 
} 
