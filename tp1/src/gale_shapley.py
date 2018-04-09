#!/usr/bin/python

import random
from random import randint
import time
import sys
import csv
import pprint

NUM_PLAYERS = 200
NUM_TEAMS = 20
NUM_PLAYERS_PER_TEAM = 10

sys.setrecursionlimit(15000000)

Players = [None] * NUM_PLAYERS  # Array vacio de longitud NUM_PLAYERS
Teams = [None] * NUM_TEAMS      # Array vacio de longitud NUM_PLAYERS

########################################################################

def ReadCSVToArray(filename):

  ifile = open(filename, "rU")
  reader = csv.reader(ifile, delimiter=",")
  rownum = 0  
  a = []
  for row in reader:
    a.append (row)
    rownum += 1
  ifile.close()
  b = []
  b = a[0]

  #b es un array de strings. Convertimos cada elemento a un int.
  for i in range(len(b)):
    b[i] = int(b[i])
      
  return b


class Player:
# para que sean variables de clase, las declaro afuera. 
# Para que sean variables de instancia, las declaro adentro del __init__
  def __init__(self):
    self.name = None
    self.PreferredTeams = [None] * NUM_TEAMS
    self.currentlyAssignedToATeam = False

  def LoadPreferredTeams(self):
    self.PreferredTeams = ReadCSVToArray("csv/player_"+ str(self.name) +".txt")



class Team:
  def __init__(self):
    self.name=None
    self.PreferredPlayers = [None] * NUM_PLAYERS
    self.CurrentPlayers = [None] * NUM_PLAYERS_PER_TEAM
  
  def LoadPreferredPlayers(self):
    self.PreferredPlayers = ReadCSVToArray("csv/team_"+ str(self.name) +".txt")

  def TeamHasRoomAvailable(self):
    #devuelve True sii hay al menos una posicion libre en el equipo.
    for i in range(0, NUM_PLAYERS_PER_TEAM ):
      if self.CurrentPlayers[i] is None:
        return True
    return False

  def GetPlayerRelativeRank(self, player):
    #itero sobre toda la lista de mis PreferredPlayers
    # por lo general, un rank mayor es peor jugador.
    # es decir, si A tiene Rank 23 y B tiene rank 58, A es mejor que B.
    rank = 1
    for i in range(0, NUM_PLAYERS):
      #print ("cmp", self.PreferredPlayers[i], " vs ", player)
      if str(self.PreferredPlayers[i])==str(player):
        return rank
      rank = rank+1
    return rank
          
  def GetTheWorstPlayerInCurrentTeam(self):
    #devuelve el peor jugador del equipo, el cual sera reemplazado
    worstplayer = None
    maxrank = 0
    for i in range(0, NUM_PLAYERS_PER_TEAM):
      if self.CurrentPlayers[i] is not None:
        rank = self.GetPlayerRelativeRank(self.CurrentPlayers[i])
        if (rank > maxrank):
          maxrank = rank
          worstPlayer = self.CurrentPlayers[i]
    return worstPlayer

  def PlayerIsABetterFit(self, player):
    #devuelve True sii el player suministrado es un mejor match para este equipo.
    if self.TeamHasRoomAvailable():
      return True     #si hay algun lugar libre en el equipo, retornamos True
    #sino:
    #obtengo quien es el peor jugador, y su ranking:
    worstPlayer = self.GetTheWorstPlayerInCurrentTeam()
    worstPlayerRank = self.GetPlayerRelativeRank(worstPlayer)

    #obtengo el ranking del jugador que quiero proponer:
    proposedPlayerRank = self.GetPlayerRelativeRank(player)

    #si el jugador que voy a agregar tiene menor rank que el peor jugador
    #(es decir, si es mejor), lo agrego.
    if (proposedPlayerRank < worstPlayerRank):
      return True
    return False

  def ReplaceWorstPlayerOrVacancyByOther(self, player):
    global Players
    if self.TeamHasRoomAvailable():
      for i in range(0, NUM_PLAYERS_PER_TEAM):
        if self.CurrentPlayers[i] is None:
          self.CurrentPlayers[i]=player
          Players[player].currentlyAssignedToATeam = True
          print("asignamos el jugador " + str(player) + " al equipo " + str(self.name) + ", porque habia lugar en el equipo.")
          PrintCurrentStatus()
          return

      
    worstPlayer = self.GetTheWorstPlayerInCurrentTeam()
    worstPlayerRank = self.GetPlayerRelativeRank(worstPlayer)
    #busco al worstPlayer:
    for i in range(0, NUM_PLAYERS_PER_TEAM):
      if self.CurrentPlayers[i]==worstPlayer:
        self.CurrentPlayers[i]=player
        Players[worstPlayer].currentlyAssignedToATeam = False   #"libero" al jugador echado
        Players[player].currentlyAssignedToATeam = True #marco como tomado al jugador incorporado
        print("asignamos el jugador " + str(player) + " al equipo " + str(self.name) + ", porque era mejor que el jugador " + str(worstPlayer)  )
        PrintCurrentStatus()
        return

def PrintCurrentStatus():
  global Teams
  global Players
  for i in range(0, NUM_TEAMS):
    print(Teams[i].CurrentPlayers)

        
def ThereAreYetUnassignedPlayers():
  global Players
  #devuelve True sii existe al menos un jugador no asignado todavia.
  for i in range(0, NUM_PLAYERS):
    if (Players[i].currentlyAssignedToATeam==False):
      return True
  return False

def ResetAllPlayersStatus():
  for i in range(0, NUM_PLAYERS):
    Players[i].currentlyAssignedToATeam=False


def RunGale():
  #nuestra modificacion del algoritmo de GaleShapley
  #mientras haya jugadores por asignar (jugadores libres):
  while ( ThereAreYetUnassignedPlayers() ):
    print ("ThereAreYetUnassignedPlayers()")
    for i in range(0, NUM_PLAYERS):
      if Players[i].currentlyAssignedToATeam==False:  #para todos los jugadores todavia libres
        print(i)
        for j in range(0, NUM_TEAMS):
          if Teams[j].PlayerIsABetterFit(i):
            print ("is a better fit!")
            Teams[j].ReplaceWorstPlayerOrVacancyByOther(i)
            break


def RunPunto2():
  global Players
  global Teams
    
  #primero importamos los archivos de preferencias de los Jugadores:
  for i in range(0, NUM_PLAYERS):
    Players[i] = Player()
    Players[i].name = i
    Players[i].LoadPreferredTeams()

  #pprint.pprint (Players[1].PreferredTeams)
  pprint.pprint(Players)

    #ahora importamos los archivos de preferencias de los Equipos:
  for i in range(0, NUM_TEAMS):
    Teams[i] = Team()
    Teams[i].name = i
    Teams[i].LoadPreferredPlayers()
  
  pprint.pprint(Teams)

  RunGale()



def main():
  RunPunto2()

if __name__ == '__main__':
  main()