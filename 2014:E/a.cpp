#include <bits/stdc++.h>
 
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
 
#define ll long long
#define ipair pair<ll, ll>
#define INF LONG_LONG_MAX
#define MAXN 2e5
 
vector<vector<ipair>> adj(2*MAXN);
vector<bool> horses(MAXN);
vector<ll> p(2*MAXN);
vector<ll> s1(2*MAXN);
vector<ll> s2(2*MAXN);

inline ll min(ll a, ll b) {
    return a < b ? a : b;
}
 
inline ll max(ll a, ll b) {
    return a > b ? a : b;
}

void dijkstra(ll n, ll s, vector<ll> & d, vector<ll> & p) {
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    priority_queue<ipair, vector<ipair>, greater<ipair>> q;
    q.push({0, s});
    while (!q.empty()) {
        ll v = q.top().second;
        ll d_v = q.top().first;
        q.pop();
        if (d_v != d[v])
            continue;

        for (auto edge : adj[v]) {
            ll len = edge.first;
            ll to = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push({d[to], to});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        ll n, m, h;
        cin >> n >> m >> h;
        for (ll i = 0; i < n * 2; i++) {
            adj.at(i).clear();
        }
        for(ll i = 0; i < h; i++) {
            ll s;
            cin >> s;
            s--;
            adj.at(s).push_back({0, s + n});
        }
        for (ll i = 0; i < m; i++) {
            ll u, v, w;
            cin >> u >> v >> w;
            u--;
            v--;
            adj.at(u).push_back({w, v});
            adj.at(v).push_back({w, u});
            adj.at(u + n).push_back({w / 2, v + n});
            adj.at(v + n).push_back({w / 2, u + n});
        }
        dijkstra(2*n, 0, s1, p);
        dijkstra(2*n, n-1, s2, p);
        ll ans = INF;
        for (ll i = 0; i < n; i++) {
            ans = min(ans, max(min(s1.at(i), s1.at(i + n)), min(s2.at(i), s2.at(i + n))));
        }
        if (ans < INF) {
            cout << ans << endl;
        } else {
            cout << -1 << endl;
        }
    }
}