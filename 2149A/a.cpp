#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);

    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int a;
        cin >> a;
        int number_of_negative = 0;
        int ans = 0;
        for (int i = 0; i < a; i++) {
            int b;
            cin >> b;
            if (b == 0) {
                ans++;
            } else if (b == -1) {
                number_of_negative++;
            }
        }
        if (number_of_negative % 2 == 1) {
            ans += 2;
        }
        cout << ans << endl;
    }
    return 0;
}