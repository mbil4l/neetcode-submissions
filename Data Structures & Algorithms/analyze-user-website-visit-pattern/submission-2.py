import itertools, heapq

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        user_sites = defaultdict(list)

        for timestamp, user, site in sorted(zip(timestamp, username, website)):
            user_sites[user].append(site)
        
        pattern_cnt = defaultdict(int)
        for user, sites in user_sites.items():
            patterns = set(itertools.combinations(sites, 3))
            for pattern in patterns:
                pattern_cnt[pattern] += 1
        
        mxheap = []

        for pattern, cnt in pattern_cnt.items():
            heapq.heappush(mxheap, (-cnt, pattern))
        
        print(mxheap)

        return list(mxheap[0][1])


        
