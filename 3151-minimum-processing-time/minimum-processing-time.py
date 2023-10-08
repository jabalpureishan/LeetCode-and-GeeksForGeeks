class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks,processorTime,Max,ind = sorted(tasks),sorted(processorTime,reverse=True),-1,0
        for i in range(3,len(tasks),4):
            Max = max(Max,tasks[i]+processorTime[ind])
            ind +=1 
        return Max
        