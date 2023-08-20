#include <stdio.h>
#include <math.h>

#define ll long long

int main(){
    ll a,b,c;
    scanf("%lld%lld%lld",&a,&b,&c);
    if(a<=b && a>=c || a <=c && a>=b){
    printf("%lld",a);
    }
    else if(b>=a && a<=c || b >= c && b<=a){
        printf("%lld",b);
    }
    else 
    printf("%lld",c);
}