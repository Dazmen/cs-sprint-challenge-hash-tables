def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_cache = {weights[i] : i for i in range(len(weights))}
    
    for w in range(length):
        missing_weight =  limit - weights[w]

        if missing_weight in weight_cache:
            high_index = max(w, weight_cache[missing_weight])
            low_index = min(w, weight_cache[missing_weight])
            return (high_index, low_index)
        # So highest valued index means the index number itself.....not the value at that index..... 


    return None

    # REMEMBER, ONLY NEED TO RETURN TWO INDICIES, NOT ALL MATCHING

    #### NEW PLAN #3 ##########
    # store weights in cache as {weight:index}
    # loop through weights list
    # limit - weights[i] = the missing weight
    # look for missing weight in weight_cache
    ### if it there we have both indexes
    ### do some minor sorting logic for tuple format
    ### if it isn't, do nothing!
    ### bingo-bango this should finally be over with

    