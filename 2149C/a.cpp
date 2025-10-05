#include <bits/stdc++.h>

using namespace std;

unordered_set<int> A;
int main() {
    ios_base::sync_with_stdio(0);

    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    A.reserve(200000);
    for (int t = 1; t <= tc; t++) {
        int n, k;
        cin >> n >> k;
        int c = 0;
        for (int i = 0; i < n; i++) {
            int b;
            cin >> b;
            if (b < k) {
                A.insert(b);
            } else if (b == k) {
                c++;
            }
        }
        int ans = max(c, (int)(k - A.size()));
        cout << ans << endl;
        A.clear();
    }
    return 0;
}