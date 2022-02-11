import glob
import pandas as pd
import numpy as np
import math

'''
Notes:
Must include file with entries in the tournament folder, then two folders
with all of the prelims and elims in order
'''

def entry_dict(tournament):
    '''make a dictionary with all of the entries at a  with school and names'''
    outputDict = {}
    file_location = \
    glob.glob(tournament + "/*.csv")[0]
    teams = pd.read_csv(file_location, delimiter=",", header=0, usecols=[2, 3])
    teams = teams.to_numpy()
    for team in teams:
        school, names = team[1], team[0]
        if names.split()[0] < names.split()[2]:
            outputDict[school] = [names, school]
        else:
            names_mod = names.split()
            names_mod[0], names_mod[2] = names_mod[2], names_mod[0]
            names_mod = ' '.join(names_mod)
            outputDict[school] = [names_mod, school]
    return outputDict


K = 50


def add_prelims(tournament, teamsDict, elos_dict, bid):
    '''adds the prelims of a tournament to the rankings'''
    files = glob.glob("data/" + tournament + "/Prelims/*.csv")
    if len(files) == 0:
        raise Exception(f"Error in reading prelims from {tournament}.")
    for file in files:
        file = open(file, "r")
        for line in file.readlines()[1:]:
            line = line.split(",")
            team1, team2, judge, result = tuple(line[0:4])
            result = result.strip().lower()
            if "bye" in result or "BYE" in team1 or "BYE" in team2 or "BYE" in judge:
                continue
            if result == "neg" or result == "con":
                team1, team2 = team2, team1  # team 1 is the winning team
            try:
                team1, team2 = teamsDict[team1], teamsDict[team2]  # this line for no school names
                '''team1, team2 = team1[:-3] + " " + teamsDict[team1], team2[:-3] + " " + teamsDict[team2]'''  # this line for school names (buggy)
            except:
                continue
            try:
                elo_team1 = elos_dict[team1[0]][0]
            except:
                elo_team1 = 1500
            try:
                elo_team2 = elos_dict[team2[0]][0]
            except:
                elo_team2 = 1500
            elo_diff = elo_team1 - elo_team2
            winProb = 1.0 / (math.pow(10.0, (-elo_diff / 400.0)) + 1.0)
            shift = K * (1 - winProb) * bid / 8 #(bid/8)^1/2
            elo_team1 += shift
            elo_team2 -= shift
            elos_dict[team1[0]] = [elo_team1,team1[1]]
            elos_dict[team2[0]] = [elo_team2,team2[1]]
        file.close()
    return elos_dict


elos_dict = {}


def add_elims(tournament, teamsDict, elos_dict, bid):
    '''adds the elims of a tournament to the rankings'''
    files = glob.glob("data/" + tournament + "/Elims/*.csv")
    if len(files) == 0:
        raise Exception(f"Error in reading elims from {tournament}.")
    for file in files:
        file = open(file, "r")
        for line in file.readlines()[1:]:
            line = line.split(",")
            try:
                team1, team2, judge, votes, result = tuple(line[0:5])
            except:
                continue
            result = result.strip().lower()
            try:
                margin, result = tuple(result.strip()[1:-1].split())
            except:
                continue
            if "bye" in result or "BYE" in team1 or "BYE" in team2 or "BYE" in judge or "bye" in margin:
                continue
            if result == "neg" or result == "con":
                team1, team2 = team2, team1  # team 1 is the winning team
            try: team1, team2 = teamsDict[team1], teamsDict[team2]
            except: continue
            try:
                elo_team1 = elos_dict[team1[0]][0]
            except:
                elo_team1 = 1500
            try:
                elo_team2 = elos_dict[team2[0]][0]
            except:
                elo_team2 = 1500
            elo_diff = elo_team1 - elo_team2
            winProb = 1.0 / (math.pow(10.0, (-elo_diff / 400.0)) + 1.0)
            shift = K * (1 - winProb) * bid / 8
            try:
                [bw, bl] = margin.split("-")
                shift *= (1 + (int(bw)-1)/(int(bl)+1))
            except:
                continue
            elo_team1 += shift + bid
            elo_team2 -= shift / 2
            elos_dict[team1[0]] = [elo_team1,team1[1]]
            elos_dict[team2[0]] = [elo_team2,team2[1]]
        file.close()
    return elos_dict


def add_tournament(tournament, bid):
    '''adds a tournament to the rankings'''
    dictionary = entry_dict("data/" + tournament)
    add_prelims(tournament, dictionary, elos_dict, bid)
    add_elims(tournament, dictionary, elos_dict, bid)

ddTeams = []
with open("PF_CT_Roster.csv", "r") as fp:
    for line in fp:
        ddTeams += [line.split(",")[0].strip()]
ddTeams = ddTeams[1:]

def write_to_csv(elosList):
    '''write the rankings to the csv'''
    add = ""
    counter = 0
    for team, eloSchool in elosList:
        elo, school = eloSchool[0],eloSchool[1]
        counter += 1
        #school = " ".join(team.split()[:-3])
        names = " ".join(team.split())
        if names in ddTeams:
            add += str(counter) + "," + school + "," + names + "," + str(round(elo * 1000) / 1000) + ",Y\n"
        else:
            add += str(counter) + "," + school + "," + names + "," + str(round(elo*1000)/1000) + ",N\n"
    with open("Rankings.csv","w") as fp:
        fp.write(add[:-1])

#9/10
add_tournament("Grapevine", 4)
#9/11
add_tournament("UK", 8)

#9/17
add_tournament("Yale", 8)
#9/18
add_tournament("JackHowe", 4)

#9/24
add_tournament("Milpitas", 2)
add_tournament("Valley", 2)
add_tournament("HolyCross", 1)
#9/25
add_tournament("Bellaire", 4)

add_tournament("Georgetown", 1) #10/08
add_tournament("Presentation", 4) #10/08
add_tournament("StJames", 1) #10/08
add_tournament("NovaTitan", 2) #10/09

#10/15
#add_tournament("Bronx", 8) NOT ENTERED BC ENTRIES NOT PUBLIC https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=20399
add_tournament("CSU", 1) 

#10/22
add_tournament("Plano", 2)

#10/29
add_tournament("BlueKey", 8)
#add_tournament("TimAverill", 2) NOT ENTERED BC ENTRIES NOT PUBLIC https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=21177

#11/05
add_tournament("AppleValley", 8)
#11/06
add_tournament("Lincoln", 1)
add_tournament("Michigan", 1)

#11/11
add_tournament("KatyTaylor", 2)
#11/12
add_tournament("Hockaday", 2)
add_tournament("PeachState", 2)
add_tournament("Badgerland", 2)
#11/13
add_tournament("Roosevelt", 1)
add_tournament("Scarsdale", 2)
add_tournament("Capitol", 1)
add_tournament("CypressBay", 4)

#11/19
add_tournament("JohnLewis", 2)
add_tournament("Villiger", 2)
#11/20
add_tournament("Glenbrooks", 8) 

#12/02
add_tournament("Alta", 4)
#12/03
add_tournament("Princeton", 8)
add_tournament("LaCostaCanyon", 4)
add_tournament("Longhorn", 2)
#add_tournament("MillardWest", 1) #12/04 NOT ENTERED BC ENTRIES NOT PUBLIC https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=21183

#12/10
add_tournament("Dowling", 4) 
add_tournament("Ridge", 2)
add_tournament("IsidoreNewman", 1)

add_tournament("Blake", 8) #12/17

#01/07
add_tournament("ASU", 8)
add_tournament("Sunvite", 8)
add_tournament("PugetSound", 1)
add_tournament("UHouston", 1)
add_tournament("MyersPark", 4)

#01/14
add_tournament("Durham", 2)
add_tournament("JamesLogan", 4)
#01/15
add_tournament("Lex", 4)

#1/22
add_tournament("Peninsula", 1)

#01/28
add_tournament("Emory", 8)
add_tournament("Seattle", 1)
add_tournament("Columbia", 4)

#02/04
add_tournament("Pennsbury", 2)
#add_tournament("Colleyville", 1) #02/04 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=21913 NOT ENTERED BC OCTOS AND FINALS RESULTS NOT PUBLISHED

#02/05
add_tournament("UNLV", 4)

#add_tournament("Penn", 8) #02/11 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=20489
#add_tournament("PalmClassic", 8) #02/12 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=22663

#add_tournament("Harvard", 8) #02/18 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=21532
#add_tournament("Bingham", 2) #02/18 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=22150
#add_tournament("Millard", 4) #02/18 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=22727
#add_tournament("Berkeley", 8) #02/19 https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=19701

#add_tournament("Lakeland", 1) #03/04 https://www.tabroom.com/index/tourn/fields.mhtml?tourn_id=22747&event_id=201367


elos = sorted(elos_dict.items(), key=lambda item: item[1], reverse=True)
write_to_csv(elos)





