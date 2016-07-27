import csv
from math import sqrt
class LinearRegression:
    filename=''
    def rsumvalue(self,inputList,numCol):
        rsum=[0]*numCol
        print("Total Rows: "+str(len(inputList)))
        for row in inputList:
            i=0
            for value in row:
                rsum[i]=rsum[i]+float(value)
                i=i+1
        return rsum

    def avgvalue(self,rsum,numCol,numRow):
        avg=[0]*numCol
        for i in range(0,numCol):
            avg[i]=rsum[i]/numRow
        return avg

    def xmeanvalue(self,inputList,avg,numCol):
        xmean=[0]*numCol
        for row in inputList:
            i=0
            for value in row:
                xmean[i]=xmean[i]+float((float(value)-avg[i])*(float(value)-avg[i]))
                i=i+1
        return xmean

    def sdvalue(self,xmean,numCol,numRow):
        sd=[0]*numCol
        for i in range(0,numCol):
            sd[i]=float(sqrt(xmean[i]))/numRow
        return sd
        
    def scaledCsv(self,inputList,avg,sd,numCol,lastCol):
        outputFile=open('scaledfile.csv','w',newline='')
        filename='scaledfile.csv'
        fwrite=csv.writer(outputFile)
        k=0
        for row in inputList:
            i=0
            listnew=[]
            for value in row:
                listnew.append(float(value)-avg[i]/sd[i])
                i=i+1
            listnew.append(lastCol[k])
            k=k+1
            fwrite.writerow(listnew)
        outputFile.close()

    def predictionCoeff(self,inputList,lastCol,numCol,coeff):
        
        pred=0
        pr=0.0
        alpha=0.01
        k=0 #for looping lastCol matrix
        for row in inputList:
            pr=coeff[0]*1 #important as x[0] is taken as 1
            i=1 #for looping coeff matrix
            for value in row:
                pr=pr+(float(coeff[i]*float(value)))
                i=i+1

            coeff[0]=coeff[0]- float(float(alpha)*(pr-float(lastCol[k]))*float(1))
            i=1
            for value in row:
                coeff[i] =coeff[i]-float(float(alpha)*(pr-float(lastCol[k])-pred)*float(value))
                i=i+1
            k=k+1
        print("Coeffecient Matrix: "+str(coeff))
        return coeff
    
    def predictValues(self,inputList,lastCol,numRow,coeff):
        outputFile=open('predict.csv','w',newline='')
        fwrite=csv.writer(outputFile)
        vallist=[]
        for index in range(0,numRow):
            vallist=inputList[index]        
            p=coeff[0]*1
            i=1
            for val in vallist:
                k=(float(coeff[i])*float(val))
                p=p+k
                #print(p)
                i=i+1
            #print(pr)
            #pred=float(1/(1+float(pow(2.71,p))))
            
            r=[]
            r.append(p)
            r.append(lastCol[index])
            fwrite.writerow(r)
        outputFile.close()
    
    def computeError(self):
         
        inputFile=open('predict.csv')
        fread=csv.reader(inputFile)
        inputList=list(fread)
        error=0
        for row in inputList:
            error=error+abs(float(row[0])-float(row[1]))
        inputFile.close()
        return error
    
    def main(self):
        filename=input('Enter filename: ')
        scale=input('Scaling required? Y/N: ')
        if scale=='Y' or scale=='y':
            
            inputFile=open(filename,'r')
            fread=csv.reader(inputFile)
            inList=list(fread)
            numCol=len(inList[0])
            numRow=len(inList)
            inputList=[]
            lastCol=[]
            limit=numCol-1
            for w in inList:
                inputList.append(w[0:limit])
                lastCol.append(w[-1])

        
            rsum,avg,sd,xmean=[0]*numCol,[0]*numCol,[0]*numCol,[0]*numCol
            #x-mean/sd
            rsum=self.rsumvalue(inputList,numCol)
            avg=self.avgvalue(rsum,numCol,numRow)       
            xmean=self.xmeanvalue(inputList,avg,numCol)
            sd=self.sdvalue(xmean,numCol,numRow)
            self.scaledCsv(inputList,avg,sd,numCol,lastCol)
        
        inputFile=open(filename,'r')
        fread=csv.reader(inputFile)
        inList=list(fread)
        inputList=[]
        lastCol=[]
        numCol=len(inList[0])
        numRow=len(inList)
        
        limit=numCol-1
        for w in inList:
            inputList.append(w[0:limit])
            lastCol.append(w[-1])

            
        coeff=[0]*numCol
        
        coeff=self.predictionCoeff(inputList,lastCol,numCol,coeff)
        self.predictValues(inputList,lastCol,numRow,coeff)
        error=self.computeError()
        print(error)
        maxlimit=14
        count=0
        while True:
            coeff=self.predictionCoeff(inputList,lastCol,numCol,coeff)
            self.predictValues(inputList,lastCol,numRow,coeff)
            error1=self.computeError()
            print(error1)
            count=count+1
            if error<error1 and count>maxlimit:
                break
            error=error1
            
        
        print('Enter values separated by , :')
        vallist = [float(x) for x in input().split(',')]

      
        p=coeff[0]*1
        i=1
        for val in vallist:
            prod=(float(coeff[i])*float(val))
            p=p+prod
            i=i+1
            
        #pred=float(1/(1+float(pow(2.71,p))))
        print("Predicted value: "+str(p))
          
