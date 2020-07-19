#include <iostream>
#include <vector>
#define forn(i, n) for (long long i = 0; i < n; i++)
using namespace std;
typedef long long ll;

ll T, N;
ll ns[200000];
int main() {
    cin >> T;
    forn(i, T) {
        cin >> N;
        forn(i, N) {
            cin >> ns[i];
        }
        bool goingDown = false;
        bool solved = false;
        for (ll i = N- 1; i >= 1 && !solved; i--) {
            if (ns[i - 1] < ns[i]) {
                goingDown = true;
            } 
            if (goingDown && ns[i - 1] > ns[i]) {
                cout << i << endl;
                solved = true;
            }
        }
        if (!solved) {
            cout << 0 << endl;
        }
    }
}