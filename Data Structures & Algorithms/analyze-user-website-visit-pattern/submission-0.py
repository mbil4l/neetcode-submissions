class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            user_visits[u].append(w)

        pattern_count = defaultdict(int)
        for u, sites in user_visits.items():
            patterns = set(combinations(sites, 3))
            for p in patterns:
                pattern_count[p] += 1

        best_pattern = None
        max_cnt = -1
        for p in sorted(pattern_count.keys()):
            if pattern_count[p] > max_cnt:
                max_cnt = pattern_count[p]
                best_pattern = p

        return list(best_pattern)