#include <vector>
#include <iostream>
using namespace std;
#define int do_not_use_int_use_long_long
#define actually_int int

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

vector<long long> dpm;
long long x;
long long n;
vector<long long> k;
vector<long long> p;


long long bin_search(vector<long long> *arry, long long target) {
    long long left = 0;
    long long right = arry->size();
    while (left + 1 < right) {
        long long mid = (left + right) / 2;
        if (arry->at(mid) <= target) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return left;
}

long long dp(long long start) {
    if (start >= n) {
        return 0;
    }
    if (dpm.at(start) != -1) {
        return dpm.at(start);
    }
    long long target = p.at(start) + x;
    long long end = bin_search(&p, target);
    long long ans;
    dpm.at(start) = end - start + dp(end + 1);
    return dpm.at(start);
}

void build_p() {
    p.clear();
    p.reserve(k.size() + 1);
    p.push_back(0); 
    for (long long i = 0; i < k.size(); i++) {
        p.push_back(p.at(i) + k.at(i));
    }
}

long long solve() {
    build_p();
    dpm.clear();
    dpm.reserve(n);
    for(long long i = 0; i < n; i++) {
        dpm.push_back(-1);
    }
    long long ans = 0;
    for(long long i = 0; i < n; i++) {
        ans += dp(i);
    }
    return ans;
}

#undef int
int main() {
#define int do_not_use_int_use_long_long
    long long T;
    cin >> T;
    for(long long t = 0; t < T; t++) {
        cin >> n >> x;
        k.clear();
        k.reserve(n);
        for(long long i = 0; i < n; i++) {
            long long temp;
            cin >> temp;
            k.push_back(temp);
        }
        dbg(k);
        cout << solve() << endl;
    }
}