def beers(number_of_workers, beer_types, workers_loved_beer):
    workers_loved_beer = workers_loved_beer.split()
    workers_loved_beer = sorted(workers_loved_beer, key=count_y)
    types_of_beer = 0
    beers_sett = []

    for i in range(number_of_workers):
        possible_sett = []

        for j in range(beer_types):
            if workers_loved_beer[i][j] == "Y":
                possible_sett.append(j)

        if len(possible_sett) == beer_types:
            continue

        else:
            if any(item in beers_sett for item in possible_sett) == False:
                beers_sett.extend(possible_sett)
                types_of_beer += 1

    if types_of_beer == 0:
        return 1

    else:
        return types_of_beer


def count_y(string):
    return string.count("Y")
