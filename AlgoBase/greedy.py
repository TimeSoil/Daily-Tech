def statecovered(state_needed, stations):

    final_station = set()


    while state_needed:
        best_station = None
        state_covered = set()

        for station, states in stations.items():
            covered = states & state_needed

            if len(covered) > len(best_station):
                best_station = station
                state_covered = covered
        state_needed -= state_covered
        final_station.add(best_station)
    return final_station

if __name__ == '__main__':
    stations={}
    stations['kone'] = set(['ID', 'NV', 'UT'])
    stations['ktwo'] = set(['ID', 'WA', 'MT'])
    stations['kthree'] = set(['OR', 'NV', 'CA'])
    stations['kfour'] = set(['NV', 'UT'])
    stations['kfive'] = set(['CA', 'AZ'])

    state_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

    final = statecovered(state_needed, stations)
    print(final)