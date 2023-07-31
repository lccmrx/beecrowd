try:
    
    while block := int(input()):
        
        while (railwayA := input()) != "0" or station:
            railwayA = [int(i) for i in railwayA.split(" ")]
            station = []
            railwayB = []
            targetTrainSet = [i for i in range(1, block + 1)][::-1]
            targetNextWagon = block
            
            try:
                padding = block * 4
                print(f"{'(START)':<16} | Rail A: {str(railwayA):<{padding}} | Station: {str(station):<{padding}} | Rail B: {str(railwayB):<{padding}}")
                while railwayA or station:
                        
                    wagon = railwayA.pop() if railwayA else 0
                    print(f"(moving wagon {wagon}) | Rail A: {str(railwayA):<{padding}} | Station: {str(station):<{padding}} | Rail B: {str(railwayB):<{padding}}")
                    if wagon is targetNextWagon:
                        railwayB.append(wagon)
                        targetNextWagon -= 1
                        continue
                    
                    while station:
                        wagonFromStation = station.pop()
                        if wagonFromStation is targetNextWagon:
                            railwayB.append(wagonFromStation)
                            targetNextWagon -= 1
                            continue
                        
                        if not railwayA and wagonFromStation is not targetNextWagon:
                            raise Exception("stalemate")
                        
                        station.append(wagonFromStation)
                        break
                        
                    if wagon is targetNextWagon and wagon != 0:
                        railwayB.append(wagon)
                        targetNextWagon -= 1
                        continue

                    if wagon == 0:
                        continue
                    station.append(wagon)

            except Exception as err:
                print("No")
            else:
                print("Yes")
            finally:
                1
                print(f"{'(END)':<16} | Rail A: {str(railwayA):<{padding}} | Station: {str(station):<{padding}} | Rail B: {str(railwayB):<{padding}}")
        else:
            print()
except: pass
