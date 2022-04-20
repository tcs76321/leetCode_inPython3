class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        dirs.reverse()
        newdirs = []
        updirs = 0
        
        for d in dirs:
            if d == '.' or d == '':
                continue
            elif d == '..':
                updirs = updirs + 1
                continue
            elif updirs > 0:
                updirs = updirs - 1
                continue
            newdirs.insert(0, d)
            
        result = ''
        for dd in newdirs:
            result = result + '/' + dd
        
        if result == '':
            return '/'
        return result
