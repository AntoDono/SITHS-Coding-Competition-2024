#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5;
const int MODULO = 1e9;

int n;
long long fib[maxn];

ifstream fin("input.txt");

int main(){
    fin >> n;

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i < maxn; i ++){
        fib[i] = fib[i-1] % MODULO + fib[i-2] % MODULO; // Gotta mod here too because fib will be very large
        fib[i] %= MODULO;
    }

    long ans = 0;

    for (int i = 0; i < n; i ++){
        int index;
        fin >> index;
        ans += fib[index-1];
        ans %= MODULO;
    }

    cout << ans << endl;
}   