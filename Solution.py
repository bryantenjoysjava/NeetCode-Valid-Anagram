class Solution:
    @staticmethod
    def isAnagram(s, t):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False

        for count_value in count.values():
            if count_value != 0:
                return False
        return True


t1 = "racecar"
s1 = "carrace"
t2 = "jam"
s2 = "jar"

print(Solution.isAnagram(t1,s1))
print(Solution.isAnagram(t2,s2))


