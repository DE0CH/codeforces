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
#define iPair pair<ll, ll>
#define INF LONG_LONG_MAX

ll min(ll a, ll b) {
    return a < b ? a : b;
}

ll max(ll a, ll b) {
    return a > b ? a : b;
}

vector<ll> dijkstra(ll n, vector<vector<iPair>> edges, ll start) {
    priority_queue<iPair> queue;
    vector<ll> dist;
    dist.resize(n, INF);
    dist.at(start) = 0;
    queue.push({0, start});
    while(!queue.empty()) {
        auto [d, u] = queue.top();
        queue.pop();
        for (auto [w, v] : edges[u]) {
            ll alt = dist[u] + w;
            if (alt < dist[v]) {
                dist[v] = alt;
                queue.push({alt, v});
            }
        }
    }
    return dist;
}

vector<ll> solve(ll n, vector<vector<iPair>> edges, vector<bool> horses, ll start) {
    vector<vector<iPair>> new_edges;
    for (ll i = 0; i < n * 2; i++) {
        vector<iPair> vv;
        new_edges.push_back(vv);
    }
    for (ll i = 0; i < n; i++) {
        for (auto [w, u] : edges.at(i)) {
            new_edges[i].push_back({w, u});
            new_edges[i + n].push_back({w / 2, u + n});
            if (horses.at(i)) {
                new_edges[i].push_back({0, i + n});
            }
        }
    }
    vector<ll> s = dijkstra(n * 2, new_edges, start);
    vector<ll> ans;
    ans.resize(n, 0);
    for (ll i = 0; i < n; i++) {
        ans.at(i) = min(s.at(i), s.at(i + n));
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        ll n, m, h;
        cin >> n >> m >> h;
        vector<ll> horses_index;
        for(ll i = 0; i < h; i++) {
            ll s;
            cin >> s;
            s--;
            horses_index.push_back(s);
        }
        vector<bool> horses;
        horses.resize(n, false);
        for (auto i : horses_index) {
            horses.at(i) = true;
        }
        vector<vector<iPair>> edges;
        for (ll i = 0; i < n; i++) {
            vector<iPair> vv;
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
        vector<ll> s1 = solve(n, edges, horses, 0);
        vector<ll> s2 = solve(n, edges, horses, n - 1);
        ll ans = INF;
        for (ll i = 0; i < n; i++) {
            ans = min(ans, max(s1.at(i), s2.at(i)));
        }
        if (ans < INF) {
            cout << ans << endl;
        } else {
            cout << -1 << endl;
        }
    }
}