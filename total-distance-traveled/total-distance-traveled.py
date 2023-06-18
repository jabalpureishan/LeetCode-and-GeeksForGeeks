class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        KM = 0
        count = 0
        while(mainTank>0):
            KM += 10
            mainTank -= 1
            count += 1
            if(count==5):
                if additionalTank>0:
                    mainTank += 1
                    additionalTank -= 1
                count = 0
        return KM
            
        