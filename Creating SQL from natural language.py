# Define respond()
def respond(message):
    # Extract the entities
    entities = ____.____(____)["____"]
    # Initialize an empty params dictionary
    params = {}
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find hotels that match the dictionary
    results = ____
    # Get the names of the hotels and index of the response
    names = [r[0] for r in results]
    n = ____(len(results),3)
    # Select the nth element of the responses array
    return ____[n].____(*names)
