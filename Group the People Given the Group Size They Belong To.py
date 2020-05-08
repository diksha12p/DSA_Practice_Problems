class Solution:
    def groupThePeople(self, groupSizes):
        d = {}
        for i, id in enumerate(groupSizes):
            if id not in d:
                d[id] = [i]
            else:
                d[id].append(i)

        result = []
        for key, ids in d.items():
            start = 0
            while start + key <= len(ids):
                result.append(ids[start:start + key])
                start += key
        return result


sol = Solution()
groupSizes = []
print(sol.groupThePeople(groupSizes))