class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos,neg = set(positive_feedback),set(negative_feedback)
        ans = {}
        for i in range(len(report)):
            #print("report[i]",report[i])
            curr = report[i].split(" ")
            #print("curr:",curr)
            for j in curr:
                if j in pos:
                    ans[student_id[i]] = ans.get(student_id[i],0) + 3
                elif j in neg:
                    ans[student_id[i]] = ans.get(student_id[i],0) - 1
                else:
                    ans[student_id[i]] = ans.get(student_id[i],0)
        new = sorted(ans.items(),key=lambda x:x[0])
        new = sorted(new,key=lambda x:x[1],reverse=True)
        print("new:",new)
        if new==[]:
            return new
        final = []
        for i in range(k):
            final.append(new[i][0])
        return final
