

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

vector<ll> books;

int solve(vector<ll>* books) {
    ll max = 0;
    auto iterator = books->rbegin();
    dbg(*books);
    iterator++;

    while (iterator != books->rend()) {
        if (*iterator > max) {
            max = *iterator;
        }
        iterator++;
    }
    dbg(books->back());
    dbg(max);
    return books->back() + max;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int tc = 1;
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        int n;
        cin >> n;
        books.clear();
        books.reserve(n);
        for (int i = 0; i < n; i++) {
            ll x;
            cin >> x;
            books.push_back(x);
        }
        cout << solve(&books) << endl;
    }
}