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
pair<vector<ll>, vector<ll>> dijkstra(ll n, vector<vector<ipair>> edges, ll start) {
    set<ipair> queue;
    vector<ll> dist;
    vector<ll> prev;
    dist.resize(n, INF);
    prev.resize(n, INF);
    dist.at(start) = 0;
    queue.insert({0, start});
    while(!queue.empty()) {
        auto top = queue.begin();
        auto [d, u] = *top;
        queue.erase(top);
        for (auto [w, v] : edges[u]) {
            ll alt = dist[u] + w;
            if (alt < dist[v]) {
                dist[v] = alt;
                prev[v] = u;
                queue.insert({alt, v});
            }
        }
    }
    return {dist, prev};
}

int main() {
    // https://codeforces.com/problemset/problem/20/C
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll n, m;
    cin >> n >> m;
    vector<vector<ipair>> edges;
    for (ll i = 0; i < n; i++) {
        vector<ipair> vv;
        edges.push_back(vv);
    }
    for (ll i = 0; i < m; i++) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--;
        v--;
        edges.at(u).push_back({w, v});
        edges.at(v).push_back({w, u});
    }
    auto [_, prev] = dijkstra(n, edges, 0);
    vector<ll> path;
    ll element = n-1;
    while (element != 0 && element != INF) {
        path.push_back(element);
        element = prev[element];
    }
    if (element == INF) {
        cout << -1 << endl;
    } else {
        cout << 1 << " ";
        for (auto it = path.rbegin(); it != path.rend(); it++) {
            cout << *it + 1 << " ";
        }
        cout << endl;
    }
}