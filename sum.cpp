#include<iostream>

using namespace std;

    class demo{
        
        public:
            int len, d;
            demo(){
                len=0;
                d=0;
            }
        
    };

int main(){
    
    int t;
    cin>>t;
    
    

    for(int k=0; k<t; k++){

        int n;
        cin>>n;
        demo obj[n];
        int sum=0;

        for(int i=0; i<n; i++){
            
            cin>>obj[i].len;
            cin>>obj[i].d;
            sum += obj[i].len * obj[i].d;
            
        }
        int m = sum;
        int sums =0;
        while(m > 0 || sums > 9){
            
            if(m == 0){
                m = sums;
                sums = 0;
            }
            sums += m % 10;
            m = m/10;
            
        }
        
    cout<<sums<<endl;

}
        
    
    return 0;
}