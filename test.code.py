filename,operation=map(str,input("Input filename, operation ").split(','))
data=[]
with open(filename) as f: # Добавиим содержание файла список
    for line in f:
        data.append([int(x) for x in line.split()])
for i in data:  #  обходим элемент списка  and logic
    for j in range(1):
        if operation == '+':
            res=i[0]+i[1]
            if res<0:
                with  open('negative_data.txt','a+') as ng:
                   ng.write(str(res)+ '\t')  
                   ng.close  
            else:
                 with  open('positive_data.txt','a+') as ps:
                   ps.write(str(res)+'\t')  
                   ps.close  
        elif operation =='*':
            res=i[0]*i[1]
            if res<0:
                with  open('negative_data.txt','a+') as ng:
                   ng.write(str(res)+ '\t')  
                   ng.close  
            else:
                 with  open('positive_data.txt','a+') as ps:
                   ps.write(str(res)+'\t')  
                   ps.close  
        elif operation == '/':
            res=i[0]/i[1]
            if res<0:
                with  open('negative_data.txt','a+') as ng:
                   ng.write(str(res)+ '\t')  
                   ng.close  
            else:
                 with  open('positive_data.txt','a+') as ps:
                   ps.write(str(res)+'\t')  
                   ps.close  
        elif operation == '-':
            res=i[0]-i[1]
            if res<0:
                with  open('negative_data.txt','a+') as ng:
                   ng.write(str(res)+ '\t')  
                   ng.close  
            else:
                 with  open('positive_data.txt','a+') as ps:
                   ps.write(str(res)+'\t')  
                   ps.close  


