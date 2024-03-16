#include <bits/stdc++.h>
#include <unordered_set>
#include <vector>
#define ll long long
using namespace std;

int main() {
    ll t;
    cin >> t;
    while (t--) {
        ll n, k;
        cin >> n >> k;
        unordered_set<ll> a_two_times;
        unordered_set<ll> a_one_time_t;
        unordered_set<ll> a_one_time;
        unordered_set<ll> b_two_times;
        ll s[2*n];
        unordered_set<ll> b_one_time_t;
        for (ll i = 0; i < 2*n; i++) {
            cin >> s[i];
        }
        for (ll i = 0; i < n; i++) {
            if (a_one_time_t.find(s[i]) == a_one_time_t.end()) {
                a_one_time_t.insert(s[i]);
            } else {
                a_two_times.insert(s[i]);
            }
        }
        for (ll i = 0 ; i < n; i++) {
            if (a_two_times.find(s[i]) == a_two_times.end()) {
                a_one_time.insert(s[i]);
            }
        }
        for (ll i = n; i < 2*n; i++) {
            if (b_one_time_t.find(s[i]) == b_one_time_t.end()) {
                b_one_time_t.insert(s[i]);
            } else {
                b_two_times.insert(s[i]);
            }
        }
        vector<ll> a_one_time_v(a_one_time.begin(), a_one_time.end());
        vector<ll> a_two_times_v(a_two_times.begin(), a_two_times.end());
        ll m = a_two_times_v.size();
        vector<ll> b_two_times_v(b_two_times.begin(), b_two_times.end());

        for (ll i = 0; i < min(k, m); i++) {
            cout << a_two_times_v[i] << " ";
            cout << a_two_times_v[i] << " ";
        }
        for (ll i = 0; i < 2*k - 2*m && i < a_one_time_v.size(); i++) {
            cout << a_one_time_v[i] << " ";
        }
        cout << endl;

        for (ll i = 0; i < min(k, m); i++) {
            cout << b_two_times_v[i] << " ";
            cout << b_two_times_v[i] << " ";
        }
        for (ll i = 0; i < 2*k - 2*m && i < a_one_time_v.size(); i++) {
            cout << a_one_time_v[i] << " ";
        }
        cout << endl;
    }
}
