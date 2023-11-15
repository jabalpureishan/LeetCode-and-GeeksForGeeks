class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p,t,ind,count = len(players),len(trainers),0,0
        for i in players:
            while ind<t and trainers[ind]<i:
                ind += 1
            if ind<t and trainers[ind]>=i:
                ind += 1
                count += 1
        return count

        