#include <iostream>
#include <vector>
#define forn(i, n) for (long long i = 0; i < n; i++)
using namespace std;
typedef long long ll;

ll T, N;
vector<ll> a, b;
int main() {
    cin >> T;
    forn(i, T) {
        cin >> N;
        forn(i, N * 2) {
            ll x;
            cin >> x;
            if (a.size() == b.size()) {
                a.push_back(x);
            } else {
                if (x == a[b.size()]) {
                    b.push_back(x);
                } else {
                    a.push_back(x);
                }
            }
        }
        forn(i, N) {
            cout << a[i] << " ";
        }
        cout << endl;
        a.clear();
        b.clear();
    }
}