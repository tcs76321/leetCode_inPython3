class Solution:
    def isValid(self, s: str) -> bool:
        orderPriorityBracket = []
        
        softBracket = 0
        pointBracket = 0
        hardBracket = 0
        
        for e in s[0:len(s):1]:
            if e == '(':
                softBracket += 1
                orderPriorityBracket.append('soft')
                
            elif e == '{':
                pointBracket += 1
                orderPriorityBracket.append('point')
                
            elif e == '[':
                hardBracket += 1
                orderPriorityBracket.append('hard')
                
            elif e == ')':
                if orderPriorityBracket.pop() != 'soft':
                    return False
                
                softBracket -= 1
                if softBracket < 0:
                    return False
                
            elif e == '}':
                if orderPriorityBracket.pop() != 'point':
                    return False
                
                pointBracket -= 1
                if pointBracket < 0:
                    return False
                
            elif e == ']':
                if orderPriorityBracket.pop() != 'hard':
                    return False
                
                hardBracket -= 1
                if hardBracket < 0:
                    return False
                
        if softBracket == 0 and pointBracket == 0 and hardBracket == 0:
            return True
        
