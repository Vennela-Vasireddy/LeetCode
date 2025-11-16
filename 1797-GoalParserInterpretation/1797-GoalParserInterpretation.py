# Last updated: 11/15/2025, 6:24:32 PM
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        s=""
        i=0
        while(i<=len(command)-1):
            if(command[i]=='G'):
                s=s+'G'
                i=i+1
            else:
                if(command[i]=='(' and command[i+1]==')'):
                    s=s+'o'
                    i=i+1
                    i=i+1
                else:
                    s=s+'al'
                    i=i+4
        return s

            

        