# Title: Most Beautiful Item for Each Query
# Submission ID: 2129883843
# Status: Accepted
# Date: September 3, 2026 at 10:39:37 PM GMT+5:30

class Solution(object):

    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

        items.sort()

        sorted_queries = sorted((query, i) for i, query in enumerate(queries))

        answer = [0] * len(queries)

        max_beauty = 0
        j = 0

        # 3. Process queries from smallest to largest
        for query, index in sorted_queries:

            # Include every item whose price <= query
            while j < len(items) and items[j][0] <= query:
                max_beauty = max(max_beauty, items[j][1])
                j += 1

            answer[index] = max_beauty

        return answer