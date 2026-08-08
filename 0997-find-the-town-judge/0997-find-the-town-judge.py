class Solution:

  def findJudge(self, n: int, trust: list[list[int]]) -> int:
    if n == 1 and not trust:
      return 1
    if not trust:
      return -1

    # Find all unique people who are trusted by someone
    candidates = {b for a, b in trust}

    # Verify each candidate
    for judge in candidates:
      trusters = set()
      trusts_anyone = False

      for a, b in trust:
        if a == judge:
          trusts_anyone = True
          break  # A judge cannot trust anyone
        if b == judge:
          trusters.add(a)

      # Check if judge trusts nobody and is trusted by all other (n - 1) people
      if not trusts_anyone and len(trusters) == n - 1:
        return judge

    return -1