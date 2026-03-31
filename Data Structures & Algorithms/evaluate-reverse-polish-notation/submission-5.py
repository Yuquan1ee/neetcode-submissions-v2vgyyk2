class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        holding_list = []
        
        for i in tokens:
            is_parentesis = False
            try:
                num = int(i)
                holding_list.append(num)
            except:
                is_parentesis = True
            if (is_parentesis):
                num2 = holding_list.pop()
                num1 = holding_list.pop()
                print(num2)
                print(num1)
                if i == "+":
                    num1 = num1 + num2
                elif i == "-":
                    num1 = num1-num2
                elif i == "*":
                    num1 = num1 * num2
                else:
                    num1 = num1 / num2
                print(int(num1))
                holding_list.append(int(num1))
                
            
        return int(holding_list[0])
                