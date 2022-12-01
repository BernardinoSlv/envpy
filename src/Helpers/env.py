def env(variable):
    with open(".env", "r") as file:
        variables = {}

        for line in file.readlines():
            if not line.find("#") or not line.strip().find("\n") or not len(line.strip()): 
                continue
            lineSplit = line.replace("\n", "").replace("\"", "").replace("'", "").strip().split("=")

            if type(lineSplit[1]) is float:
                value = float(value)

            try:
                value = eval(lineSplit[1])
            except:
                value = lineSplit[1]

            if (value == "true" or value == "True"):
                value = True
            elif (value == "false" or value == "False"):
                value = False
                
            variables[lineSplit[0]] = value

        # print(variables)
        return variables[variable]