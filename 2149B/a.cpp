#include <bits/stdc++.h>

using namespace std;

vector<int> A;
int main() {
    ios_base::sync_with_stdio(0);

    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    A.reserve(200000);
    for (int t = 1; t <= tc; t++) {
        int a;
        cin >> a;
        for (int i = 0; i < a; i++) {
            int b;
            cin >> b;
            A.push_back(b);
        }
        int ans = 0;
        sort(A.begin(), A.end());
        for (int j = 0; j < a/2; j++) {
            ans = max(ans, A.at(j*2+1) - A.at(j*2));
        }
        cout << ans << endl;
        A.clear();
    }
    return 0;
}