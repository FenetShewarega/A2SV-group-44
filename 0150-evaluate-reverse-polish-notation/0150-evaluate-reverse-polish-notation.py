class Solution(object):
      def evalRPN(self, tokens):
        operatorQ=[]
        operandQ=[]
        for opStr in tokens:
            if re.match(r'[+-]?\d',opStr):
                operandQ.append(opStr)
            elif(["+","-","*","/"].count(opStr)!=-1):
                operatorQ.insert(0,opStr)
            if (len(operandQ)>=2 and len(operatorQ)>=1):
                operator=operatorQ.pop()
                operand1=string.atof(operandQ.pop())
                operand2=string.atof(operandQ.pop())
                if(operator=="+"):
                    operandQ.append(operand2+operand1)
                elif(operator=="-"):
                    operandQ.append(operand2-operand1)
                elif(operator=="*"):
                    operandQ.append(operand2*operand1)
                elif(operator=="/"):
                    if (operand1!=0):
                        operandQ.append(int(operand2/operand1))
        return int( operandQ.pop())
