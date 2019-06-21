
def counttrios(output):
    compatibility_trios = 0
    one_step_mutation_trios = 0
    two_step_mutation_trios = 0
    something_else_trios = 0
    if output[0] == 0 and output[1] == 0:
        compatibility_trios = compatibility_trios + 1
    elif output[0] == 1 or output[1] == 1:
        one_step_mutation_trios = one_step_mutation_trios + 1
    elif output[0] == 2 or output[1] == 2:
        two_step_mutation_trios = two_step_mutation_trios + 1
    else:
        something_else_trios = something_else_trios + 1
    return [compatibility_trios, one_step_mutation_trios, two_step_mutation_trios, something_else_trios]





