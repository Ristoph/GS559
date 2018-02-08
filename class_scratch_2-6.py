## functions: def and return are keywords
#def <funcname>(<inputvar>)

def make_dict(my_filename):
    score_dict = {}
    my_file = open(my_filename, 'r')
    for line in my_file:
        fields = line.strip().split("\t")
        score_dict[fields[0]] = float(fields[1])
    my_file.close()
    return score_dict

