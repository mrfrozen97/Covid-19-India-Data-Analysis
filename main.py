"""
Author - mr_frozen
This ccode basically plots the graphs of covid 19 for India analysis in 3 parts.
1)Ovberall analysis countrywise
2)Statewise analtsis of active cases
3)Combined comparison of states and UT's
This comparison just gelps us visualise which state is doing better \abnd which one needs to improve. Because raw data
can sometimes be misleading because all states do not have same populaton, In fact some states have very high population
comparatively cases, vice versa. So I hace also taken into account the population in the last section .


Be careful while using it becaues i have used some folder nam,es to save the graphs. U have to fiorst reate this folders before running it.


"""





import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect



# Read the csv file
data = pd.read_csv("covid_19.csv")


# The sort is a array which contains name of each state......
sort =[x for x, df in data.groupby('Region')]
print(sort)

#This code selects a given state from entire data and creates a new csv file storing data state/union terrotary wise

for i in sort:
    temp = data.loc[data['Region']==i]
    temp.to_csv("./sorted_data/" + i+".csv" )






#The code below draws a graph for goa state . This is just a sample to understand the code for multiple graphs
#I used this below code as my frame and then iterated it with for loop for all states to det graph for all states and UTs



#Dont forgetr to create a folder named sorted_data
goa = pd.read_csv("./sorted_data/Goa.csv")
#print(goa)

#plotting a normal graph of date vs confirmed cases, active cases, recovered and dead
#give appropriatre labels
plt.plot(goa['Date'], goa['Confirmed Cases'], label = 'Confirmed')
plt.plot(goa['Date'], goa['Cured/Discharged'], label ='Recovered')
plt.plot(goa['Date'], goa['Active Cases'], label='Active')
plt.plot(goa['Date'], goa['Death'], label = 'Total Deaths')

#since i have rotated the x labels verticlly some of the part of labels goes out of graph, so below line of code adjust this.
plt.subplots_adjust(bottom=0.143)
plt.title("Goa Confirmed cases", fontdict={"fontsize": 20}, color = '#000080')
plt.yticks(range(0,max(goa['Confirmed Cases'])+500,1500))
plt.xticks(goa['Date'][::10], rotation = 'vertical')
plt.xlabel("Date (DD/MM/YY)", fontdict={"fontsize":20}, color = '#FF8C00')
plt.ylabel("Number of cases", fontdict={"fontsize":20}, color = '#FF8C00')
plt.grid()

plt.annotate('Death: '+ str(int(max(goa['Death']))), (len(goa['Date']),max(goa['Death'])), textcoords = 'offset points', xytext = (0,4), ha= 'center')
plt.annotate('Confirmed: ' + str(int(max(goa['Confirmed Cases']))), (len(goa['Date']),max(goa['Confirmed Cases'])), textcoords = 'offset points', xytext = (-60,5))
plt.annotate('Cured: ' + str(int(max(goa['Cured/Discharged']))), (len(goa['Date']),max(goa['Cured/Discharged'])), textcoords = 'offset points', xytext = (-44,5))
plt.annotate('Active: ' + str(int(goa['Active Cases'][len(goa['Date']) - 1])), (len(goa['Date']),goa['Active Cases'][len(goa['Date']) - 1]), textcoords = 'offset points', xytext = (-35,10))

figure = plt.gcf()
figure.set_size_inches(20,10)
plt.legend(prop={'size': 15})
plt.savefig("./graphs./summary_graph/Goa_graph1", bbox_inches = 'tight')
plt.show()








#This ocde iterates through all the states from sort and draws and saves their graph in a folder




abc = sort.index('Lakshadweep')
sort.pop(abc)

for state in sort:
    st = pd.read_csv("./sorted_data/" + state + ".csv")
    # print(goa)
    plt.plot(st['Date'], st['Confirmed Cases'], label='Confirmed')
    plt.plot(st['Date'], st['Cured/Discharged'], label='Recovered')
    plt.plot(st['Date'], st['Active Cases'], label='Active')
    plt.plot(st['Date'], st['Death'], label='Total Deaths')

    # since i have rotated the x labels verticlly some of the part of labels goes out of graph, so below line of code adjust this.

    plt.subplots_adjust(bottom=0.143)
    plt.title(state + " covid-19 analysis", fontdict={"fontsize": 20}, color='#000080')
    plt.yticks(range(0, max(st['Confirmed Cases']) + 1000, int(max(st['Confirmed Cases'])/20)))
    plt.xticks(st['Date'][::10], rotation='vertical')
    plt.xlabel("Date (DD/MM/YY)", fontdict={"fontsize": 20}, color='#FF8C00')
    plt.ylabel("Number of cases", fontdict={"fontsize": 20}, color='#FF8C00')
    plt.grid()

    plt.annotate('Death: ' + str(int(max(st['Death']))), (len(st['Date']), max(st['Death'])), textcoords='offset points', xytext=(0, 4), ha='center')
    plt.annotate('Confirmed: ' + str(int(max(st['Confirmed Cases']))), (len(st['Date']), max(st['Confirmed Cases'])), textcoords='offset points', xytext=(-60, 5))
    plt.annotate('Cured: ' + str(int(max(st['Cured/Discharged']))), (len(st['Date']), max(st['Cured/Discharged'])), textcoords='offset points', xytext=(-44, 5))
    plt.annotate('Active: ' + str(int(st['Active Cases'][len(st['Date']) - 1])),(len(st['Date']), st['Active Cases'][len(st['Date']) - 1]), textcoords='offset points',xytext=(-35, 10))

    figure = plt.gcf()
    figure.set_size_inches(20, 10)
    plt.legend(loc = 'upper left' ,prop={'size': 15})
    plt.savefig("./graphs/summary_graph/" + state + " graph1", bbox_inches='tight')
    plt.close()



death_rate = []
y_ticks = []
t = 0.0

stateUT = list(sort)

stateUT[sort.index("Andaman and Nicobar Islands")] = "AN Islands"
stateUT[sort.index('Dadra and Nagar Haveli and Daman and Diu')] = "DNHDD"
stateUT[sort.index('Jammu and Kashmir')] = "J and K"
stateUT.pop(sort.index("State assignment pending"))
sort.pop(sort.index('State assignment pending'))

#for i in stateUT:
#    print(i)


for i in range(18):
    t = t + 0.2
    y_ticks.append(t)

for state in sort:
         st = pd.read_csv("./sorted_data/" + state + ".csv")
         confirmed = max([int(st['Confirmed Cases'][len(st['Date']) - 1]), 1])
         death = int(st['Death'][len(st['Date']) - 1])
       #  print(state + ": " +str(float(death/confirmed * 100)) )
         death_rate.append(float(death/confirmed * 100))

plt.bar(stateUT, death_rate, zorder = 3)
plt.subplots_adjust(bottom=0.25)
plt.xticks(rotation = 'vertical')
plt.yticks(y_ticks)
plt.ylabel("Death rate (in %)", fontdict={"fontsize":15}, color = '#ff5722')
plt.xlabel("States and Union Territories", fontdict={"fontsize":15}, color = '#ff5722')
plt.title("Death rate(%) comparison", fontdict={"fontsize":20}, color = '#7b1fa2')
plt.grid(axis='y', color = '#cfd8dc', zorder = 0)

figure = plt.gcf()
figure.set_size_inches(20, 10)


plt.savefig("./graphs/compare/States,UT graph1", bbox_inches='tight')
plt.show()











#for i in stateUT:
 #   print(i)


 # Population parameter is added to calculate parameters per capita
population = [380581, 49577103, 1383727, 31205576, 104099452, 1055450, 25545198, 586956, 16787941, 1458545, 60439692,
              25351462, 6864602, 1383230550, 12267302, 32988134, 61095297, 33406061, 274000, 64473, 72626809, 112374333,
              2855794, 2966889, 1097206, 1978502, 41974218, 1247953, 27743338, 68548437, 610577, 72147030,
              35003674, 3673917, 199812341, 10086292, 91276115, 7713000000]





t = 0
cases_per_pop = []
for i in sort:
    st = pd.read_csv("./sorted_data/" + i + ".csv")
    cases_per_pop.append(int(st['Confirmed Cases'][len(st['Date']) - 1]) / population[t] *1000)
    #print(i+ ": " + str(population[t]))
    t = t+1

plt.bar(stateUT, cases_per_pop, zorder = 3)
plt.xticks(rotation = 'vertical')
plt.yticks(range(0,22))
plt.subplots_adjust(bottom=0.25)
plt.ylabel("Confirmed cases (per 1000 people)", fontdict={"fontsize":15}, color = '#ff5722')
plt.xlabel("States and Union Territories", fontdict={"fontsize":15}, color = '#ff5722')
plt.title("Confirmed cases per population comparison", fontdict={"fontsize":20}, color = '#7b1fa2')
plt.grid(axis='y', color = '#cfd8dc', zorder = 0)
fig = plt.gcf()
fig.set_size_inches(20,10)
plt.savefig("./graphs/compare/States,UT confirmed cases per population", bbox_inches='tight')

plt.show()










t = 0
m = 0
ma = []
for i in range(16):
    ma.append(m)
    m = m+0.3
cases1_per_pop = []
for i in sort:
    st = pd.read_csv("./sorted_data/" + i + ".csv")
    cases1_per_pop.append(int(max(st['Active Cases'])) / population[t] * 1000)
    #print(i+ ": " + str(population[t]))
    t = t+1

plt.bar(stateUT, cases1_per_pop, zorder = 3)
plt.xticks(rotation = 'vertical')
plt.yticks(ma)
plt.subplots_adjust(bottom=0.25)
plt.ylabel("Active cases (per 1000 people)", fontdict={"fontsize":15}, color = '#ff5722')
plt.xlabel("States and Union Territories", fontdict={"fontsize":15}, color = '#ff5722')
plt.title("Active cases per population comparison", fontdict={"fontsize":20}, color = '#7b1fa2')
plt.grid(axis='y', color = '#cfd8dc', zorder = 0)
fig = plt.gcf()
fig.set_size_inches(20,10)
plt.savefig("./graphs/compare/States,UT Active cases per population", bbox_inches='tight')

plt.show()





#Here I ahve first calculated daily rise by substracting pair of consecutive elements of confirmed cases. And after cal
# -culation I have also plotted this graph state wise and date wise to get and idea of which state is getting 
#  better/worst....................



for state in sort:
    st = pd.read_csv("./sorted_data/" + state + ".csv" )
    dailyc = list(st['Confirmed Cases'])
    dailyc1 = list(st['Confirmed Cases'])
    dailyc.pop(0)
    daily_cases = []
    for i in range(len(st['Confirmed Cases']) - 1):
             daily_cases.append(dailyc[i] - dailyc1[i])
    date = list(st['Date'])
    date.pop(0)
    plt.plot(date, daily_cases, label = " Daily rise", color="#f4511e")
    plt.xticks(date[::7], rotation ='vertical')
    plt.subplots_adjust(bottom=0.25)
    plt.grid()
    plt.legend(loc = 'upper left', prop={'size':15})
    plt.title(state + " Daily rise in cases", fontdict={"fontsize": 20}, color="#6200ea")
    plt.xlabel("Date(DD/MM/YY)", fontdict={"fontsize": 15}, color="Orange")
    plt.ylabel("Daily Cases increase", fontdict={"fontsize": 15}, color="Orange")
    plt.yticks(range(0, max([max(daily_cases) + int(max(daily_cases)/10), 2]), max([int(max(daily_cases)/20) , 1])))

    fig = plt.gcf()
    fig.set_size_inches(20,10)
    plt.savefig("./graphs/daily_cases/" + state + " daily rise", bbox_inches='tight')
    plt.show()

    plt.close()
