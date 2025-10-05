#include <bits/stdc++.h>

using namespace std;

unordered_set<long long> A;
int main() {
    ios_base::sync_with_stdio(0);

    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        A.clear();
        long long a = 0;
        cin >> a;
        for (int m = 0; m < a; m++) {
            long long k;
            cin >> k;
            A.insert(k);
        }
        cout << A.size() * 2 -1 << endl;
    }
    return 0;
}