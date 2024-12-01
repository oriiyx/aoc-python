def process_input(filename):
    """
    Reads input file line by line and processes each line.
    Returns list of processed lines.
    """
    result = []

    with open(filename, 'r') as file:
        for line in file:
            # Remove trailing newline/whitespace
            line = line.strip()

            # Example processing - modify as needed:
            # Convert to integer if needed
            # number = int(line)

            # Split line into parts if needed
            # parts = line.split()

            # Add processed line to results
            result.append(line)

    return result