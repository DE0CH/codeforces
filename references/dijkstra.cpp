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

vector<vector<ipair>> adj(MAXN);
vector<ll> d(MAXN);
vector<ll> p(MAXN);

void dijkstra(ll n, ll s, vector<ll> & d, vector<ll> & p) {
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    set<ipair> q;
    q.insert({0, s});
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());

        for (auto edge : adj[v]) {
            int len = edge.first;
            int to = edge.second;

            if (d[v] + len < d[to]) {
                q.erase({d[to], to});
                d[to] = d[v] + len;
                p[to] = v;
                q.insert({d[to], to});
            }
        }
    }
}

int main() {
    // https://codeforces.com/problemset/problem/20/C
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll n, m;
    cin >> n >> m;
    for (ll i = 0; i < n; i++) {
        adj.at(i).clear();
    }
    for (ll i = 0; i < m; i++) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--;
        v--;
        adj.at(u).push_back({w, v});
        adj.at(v).push_back({w, u});
    }
    dijkstra(n, 0, d, p);
    vector<ll> path;
    ll element = n-1;
    dbg(d);
    dbg(p);
    while (element != 0 && element != -1) {
        path.push_back(element);
        element = p[element];
    }
    if (element == -1) {
        cout << -1 << endl;
    } else {
        cout << 1 << " ";
        for (auto it = path.rbegin(); it != path.rend(); it++) {
            cout << *it + 1 << " ";
        }
        cout << endl;
    }
}