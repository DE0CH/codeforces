#include <bits/stdc++.h>
using namespace std;

#define ll long long

int gcd(ll a, ll b, ll& x, ll& y) {
    x = 1, y = 0;
    ll x1 = 0, y1 = 1, a1 = a, b1 = b;
    while (b1) {
        ll q = a1 / b1;
        tie(x, x1) = make_tuple(x1, x - q * x1);
        tie(y, y1) = make_tuple(y1, y - q * y1);
        tie(a1, b1) = make_tuple(b1, a1 - q * b1);
    }
    return a1;
}

ll modinv(ll a, ll m) {
    ll x, y;
    ll g = gcd(a, m, x, y);
    if (g != 1) {
        throw runtime_error("No solution!");
    }
    else {
        x = (x % m + m) % m;
        return x;
    }
}