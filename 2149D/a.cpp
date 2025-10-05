#include <bits/stdc++.h>
#include <math.h>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif


long long solve(string s, char c);

int main() {
    ios_base::sync_with_stdio(0);

    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n;
        cin >> n >> ws;
        string s;
        getline(cin, s);
        cout << min(solve(s, 'a'), solve(s, 'b')) << endl;
    }
    return 0;
}

long long solve(string s, char c) {
    int number_of_c = 0;
    for (auto cc = s.begin(); cc != s.end(); cc++){
        if (*cc == c) {
            number_of_c++;
        }
    }
    dbg(number_of_c);
    if (number_of_c <= 1) {
        return 0;
    }
    int i = 0;
    int pos;
    for (auto cc = s.begin(); cc != s.end(); cc++) {
        if (i == number_of_c / 2) {
            pos = cc - s.begin();
        }
        if (*cc == c) {
            i++;
        }
    }
    dbg(pos);
    long long ans = 0;
    i = 0;
    for (auto cc = s.begin(); cc != s.end(); cc++) {
        if (*cc == c){

            dbg("abc", pos);
            dbg("abc", (cc - s.begin()));
            ans += abs(pos - (cc - s.begin())) - abs(i - (number_of_c / 2));
            i++;
        }
    }
    dbg(ans);
    return ans;
}