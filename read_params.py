#read_params.py

def solar_params():
    file=["parameters.dat"]
    solar_params=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="S":
                    solar_params.append(linestring[1])
                    solar_params.append(linestring[2])
        f.closed
        True
        solar_params.pop(0) #removes the first point (zero) in the list
    return solar_params

def inner_params():
    file=["parameters.dat"]
    inner_params=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="I":
                    inner_params.append(linestring[1])
                    inner_params.append(linestring[2])
        f.closed
        True
        inner_params.pop(0) #removes the first point (zero) in the list
    return inner_params

def outer_params():
    file=["parameters.dat"]
    outer_params=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="O":
                    outer_params.append(linestring[1])
                    outer_params.append(linestring[2])
                    outer_params.append(linestring[3])
        f.closed
        True
        outer_params.pop(0) #removes the first point (zero) in the list
    return outer_params